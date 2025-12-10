import React, { useEffect, useRef, useState } from 'react';
import WaveSurfer from 'wavesurfer.js';

const AudioVisualizer = ({ url, isPlaying, onTogglePlay }) => {
    const waveformRef = useRef(null);
    const wavesurfer = useRef(null);

    useEffect(() => {
        if (!waveformRef.current) return;

        wavesurfer.current = WaveSurfer.create({
            container: waveformRef.current,
            waveColor: '#4b5563', // gray-600
            progressColor: '#8b5cf6', // violet-500
            cursorColor: '#c4b5fd', // violet-300
            barWidth: 2,
            barGap: 3,
            barRadius: 3,
            height: 128,
            normalize: true,
            minPxPerSec: 100,
        });

        wavesurfer.current.on('finish', () => {
            // Handle finish if needed (e.g. stop playing state)
            if (onTogglePlay) onTogglePlay(false);
        });

        return () => {
            wavesurfer.current.destroy();
        };
    }, []);

    useEffect(() => {
        if (wavesurfer.current && url) {
            wavesurfer.current.load(url);
        }
    }, [url]);

    useEffect(() => {
        if (wavesurfer.current) {
            isPlaying ? wavesurfer.current.play() : wavesurfer.current.pause();
        }
    }, [isPlaying]);

    return <div ref={waveformRef} className="w-full" />;
};

export default AudioVisualizer;
