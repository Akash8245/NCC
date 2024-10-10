import React from 'react'
import { Link } from 'react-router-dom'

export default function Home() {
  return (
    <div>
      Home Page
      <br />
      <Link to="/login">Go to Login</Link>
    </div>
  )
}
