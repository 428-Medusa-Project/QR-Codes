import { useEffect } from 'react';

const RedirectToWiki = () => {
  useEffect(() => {
    // Perform the redirection to Wikipedia
    window.location.href = 'https://www.wikipedia.org/';
  }, []);

  return (
    <div>
      <h1>Redirecting to Wikipedia...</h1>
    </div>
  );
};

export default RedirectToWiki;
