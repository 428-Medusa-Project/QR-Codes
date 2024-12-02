import { useEffect } from 'react';
import { useParams } from 'react-router-dom';

const Redirect = () => {
  const { to } = useParams(); 
  useEffect(() => {
    if (to) {
      const decodedUrl = decodeURIComponent(to);
      window.location.href = decodedUrl;
    }
  }, [to]);

  return (
    <div>
      <h1>Redirecting...</h1>
    </div>
  );
};

export default Redirect;
