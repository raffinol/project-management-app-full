import { Link } from "react-router-dom";

function Home({ user, setUser }) {
  function handleLogoutClick() {
    fetch("/logout", { method: "DELETE" }).then((r) => {
      if (r.ok) {
        setUser(null);
      }
    });
  }

    if (user) {
      return (
        <>
          <h1>Welcome, {user.username}!</h1><br></br>
          <button onClick={handleLogoutClick}> Logout</button>
        </>
      );
    } else {
      return (
        <>
            <h2>Please Login or Sign Up</h2>
            <Link to="/signup">Signup</Link><br></br>            
            <Link to="/login">Login</Link>   
        </>
      );
      
    }
  }
  
  export default Home;