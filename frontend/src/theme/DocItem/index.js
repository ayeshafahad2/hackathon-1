// frontend/src/theme/DocItem/index.js
import React from 'react';
import OriginalDocItem from '@theme-original/DocItem';
import ChapterControls from '../../components/Chapter/ChapterControls';

export default function DocItem(props) {
  const { content: DocContent } = props;
  const metadata = DocContent?.metadata;

  return (
    <>
      <OriginalDocItem {...props} />
      {/* Add chapter controls at the beginning of each chapter if metadata is available */}
      {metadata && (
        <div style={{ marginTop: '2rem' }}>
          <ChapterControls
            chapterId={metadata.unversionedId || metadata.slug || 'unknown'}
            chapterTitle={metadata.title || 'Untitled'}
            content={DocContent.content?.substring?.(0, 1000) + "..." || "..."} // First 1000 chars as sample
            onContentUpdate={() => window.location.reload()} // Simple refresh for demo
          />
        </div>
      )}
    </>
  );
}