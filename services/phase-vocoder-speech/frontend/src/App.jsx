import React, { useState, useEffect } from 'react';
import { Upload, Play, Pause, Download, Music, Wand2 } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import AudioVisualizer from './components/AudioVisualizer';
import EffectControls from './components/EffectControls';
import { uploadAudio, processAudio, getEffects } from './lib/api';

function App() {
  const [fileId, setFileId] = useState(null);
  const [audioUrl, setAudioUrl] = useState(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [effects, setEffects] = useState([]);
  const [selectedEffect, setSelectedEffect] = useState('robot');
  const [params, setParams] = useState({});
  const [isProcessing, setIsProcessing] = useState(false);
  const [processedAudioUrl, setProcessedAudioUrl] = useState(null);

  // Define base URL for audio resources
  const BASE_URL = import.meta.env.PROD ? '' : 'http://localhost:8000';

  // Load available effects on mount
  useEffect(() => {
    getEffects().then(setEffects).catch(console.error);
  }, []);

  // Update params when effect changes
  useEffect(() => {
    const effect = effects.find(e => e.id === selectedEffect);
    if (effect) {
      const defaultParams = {};
      effect.params.forEach(p => defaultParams[p.name] = p.default);
      setParams(defaultParams);
    }
  }, [selectedEffect, effects]);

  const handleFileUpload = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    try {
      const { file_id, filename } = await uploadAudio(file);
      setFileId(file_id);
      setAudioUrl(`${BASE_URL}/audio/uploaded/${filename}`);
      setProcessedAudioUrl(null); // Reset processed audio
    } catch (error) {
      console.error("Upload failed", error);
      alert("Upload failed");
    }
  };

  const handleProcess = async () => {
    if (!fileId) return;
    setIsProcessing(true);
    try {
      const { url } = await processAudio(fileId, selectedEffect, params);
      setProcessedAudioUrl(`${BASE_URL}${url}?t=${Date.now()}`);
      setIsPlaying(false);
    } catch (error) {
      console.error("Processing failed", error);
      alert("Processing failed");
    } finally {
      setIsProcessing(false);
    }
  };

  const handleParamChange = (name, value) => {
    setParams(prev => ({ ...prev, [name]: value }));
  };

  // Determine which URL to visualize/play
  const currentUrl = processedAudioUrl || audioUrl;

  return (
    <div className="min-h-screen bg-neutral-950 text-white font-sans selection:bg-violet-500 selection:text-white overflow-hidden">
      {/* Background Gradients */}
      <div className="fixed inset-0 pointer-events-none">
        <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-violet-900/20 blur-[120px] rounded-full" />
        <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-fuchsia-900/20 blur-[120px] rounded-full" />
      </div>

      <div className="relative max-w-6xl mx-auto px-6 py-12 h-screen flex flex-col">
        {/* Header */}
        <header className="flex items-center justify-between mb-12">
          <div className="flex items-center gap-3">
            <div className="p-2 bg-gradient-to-br from-violet-600 to-fuchsia-600 rounded-xl shadow-lg shadow-violet-900/20">
              <Music className="w-6 h-6 text-white" />
            </div>
            <h1 className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-white to-gray-400">
              Audio Vocoder
            </h1>
          </div>
        </header>

        <main className="flex-1 grid grid-cols-1 lg:grid-cols-12 gap-8 min-h-0">
          {/* Main Visualizer Area */}
          <div className="lg:col-span-8 flex flex-col gap-6 min-h-0">
            <div className="flex-1 bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-8 flex flex-col justify-center relative overflow-hidden group">
              {!currentUrl ? (
                <div className="text-center space-y-4">
                  <div className="w-20 h-20 bg-white/5 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:scale-110 transition-transform duration-300">
                    <Upload className="w-8 h-8 text-gray-400" />
                  </div>
                  <h3 className="text-xl font-medium text-white">Upload Audio</h3>
                  <p className="text-gray-400 text-sm max-w-xs mx-auto">
                    Drag and drop or click to upload your audio file (.wav, .mp3)
                  </p>
                  <label className="mt-4 inline-flex px-6 py-3 bg-white text-black font-semibold rounded-full cursor-pointer hover:bg-gray-200 transition-colors">
                    Choose File
                    <input type="file" className="hidden" accept="audio/*" onChange={handleFileUpload} />
                  </label>
                </div>
              ) : (
                <div className="w-full space-y-8">
                  <div className="flex items-center justify-between mb-4">
                    <span className="text-xs font-mono text-violet-400 uppercase tracking-wider">
                      {processedAudioUrl ? 'Processed Signal' : 'Original Signal'}
                    </span>
                    {currentUrl && (
                      <div className="flex gap-2">
                        <a href={currentUrl} download className="p-2 hover:bg-white/10 rounded-full transition-colors text-white/50 hover:text-white" title="Download">
                          <Download size={20} />
                        </a>
                        <button onClick={() => setFileId(null) || setAudioUrl(null) || setProcessedAudioUrl(null)} className="text-xs text-red-400 hover:text-red-300">Clear</button>
                      </div>
                    )}
                  </div>

                  <div className="bg-black/20 rounded-2xl p-6 border border-white/5">
                    <AudioVisualizer
                      url={currentUrl}
                      isPlaying={isPlaying}
                      onTogglePlay={(playing) => setIsPlaying(playing)} // Optional: sync play state if visualizer finishes
                    />
                  </div>

                  <div className="flex justify-center gap-6">
                    <button
                      onClick={() => setIsPlaying(!isPlaying)}
                      className="p-4 bg-white text-black rounded-full hover:scale-105 active:scale-95 transition-all shadow-xl shadow-white/10"
                    >
                      {isPlaying ? <Pause fill="currentColor" /> : <Play fill="currentColor" className="ml-1" />}
                    </button>
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* Sidebar Controls */}
          <div className="lg:col-span-4 flex flex-col gap-6">
            <div className="bg-white/5 backdrop-blur-xl border border-white/10 rounded-3xl p-6 flex-1">
              <div className="flex items-center gap-2 mb-6">
                <Wand2 className="w-5 h-5 text-violet-400" />
                <h2 className="text-lg font-semibold">Controls</h2>
              </div>

              <div className="space-y-8">
                <EffectControls
                  effects={effects}
                  selectedEffect={selectedEffect}
                  onEffectChange={setSelectedEffect}
                  params={params}
                  onParamChange={handleParamChange}
                />

                <div className="pt-6 border-t border-white/10">
                  <button
                    onClick={handleProcess}
                    disabled={!fileId || isProcessing}
                    className={`w-full py-4 rounded-xl font-semibold flex items-center justify-center gap-2 transition-all ${!fileId
                      ? 'bg-gray-800 text-gray-500 cursor-not-allowed'
                      : isProcessing
                        ? 'bg-violet-700 text-white cursor-wait'
                        : 'bg-gradient-to-r from-violet-600 to-fuchsia-600 text-white shadow-lg shadow-violet-900/25 hover:shadow-violet-900/40 hover:scale-[1.02] active:scale-[0.98]'
                      }`}
                  >
                    {isProcessing ? 'Processing...' : 'Apply Processing'}
                  </button>
                </div>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
}

export default App;
