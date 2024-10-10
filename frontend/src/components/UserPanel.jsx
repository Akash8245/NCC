import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function UserPanel() {
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const verifyCookie = async () => {
      const response = await fetch('http://127.0.0.1:8000/login/', {
        method: 'GET',
        credentials: 'include', // Ensure cookies are sent
      });

      const data = await response.json();
      if (response.ok) {
        setMessage(data.message); // You are logged in
      } else {
        setMessage('Please login!');
        navigate('/login'); // Redirect to login if no cookie found
      }
    };

    verifyCookie();
  }, [navigate]);

  return (
    <div>
      <h2>User Panel</h2>
      <p>{message}</p>
    </div>
  );
}
