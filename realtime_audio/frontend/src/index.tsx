import React from 'react';
import { createRoot } from 'react-dom/client';
import RealtimeAudio from './RealtimeAudio';

// Mount the component to the DOM
const container = document.getElementById('root');
if (container) {
  const root = createRoot(container);
  root.render(<RealtimeAudio />);
}