import React from 'react';

const EffectControls = ({ effects, selectedEffect, onEffectChange, params, onParamChange }) => {
    if (!effects.length) return <div>Loading effects...</div>;

    const currentEffect = effects.find(e => e.id === selectedEffect);

    return (
        <div className="space-y-6">
            <div>
                <label className="block text-sm font-medium text-gray-400 mb-2">Effect</label>
                <div className="grid grid-cols-2 gap-2">
                    {effects.map((effect) => (
                        <button
                            key={effect.id}
                            onClick={() => onEffectChange(effect.id)}
                            className={`p-3 rounded-lg text-sm font-medium transition-colors ${selectedEffect === effect.id
                                    ? 'bg-violet-600 text-white'
                                    : 'bg-gray-800 text-gray-400 hover:bg-gray-700'
                                }`}
                        >
                            {effect.name}
                        </button>
                    ))}
                </div>
            </div>

            {currentEffect && (
                <div className="space-y-4">
                    <h3 className="text-sm font-medium text-gray-300">Parameters</h3>
                    {currentEffect.params.map((param) => (
                        <div key={param.name} className="space-y-1">
                            <div className="flex justify-between text-xs text-gray-500">
                                <span>{param.label}</span>
                                <span>{params[param.name] || param.default}</span>
                            </div>
                            <input
                                type="range"
                                min={param.min}
                                max={param.max}
                                step={param.step || 0.1}
                                value={params[param.name] !== undefined ? params[param.name] : param.default}
                                onChange={(e) => onParamChange(param.name, parseFloat(e.target.value))}
                                className="w-full h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer accent-violet-500"
                            />
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default EffectControls;
