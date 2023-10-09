import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import SignUp from "./SignUp";
import Home from "./Home";
import Login from "./Login";
import NavBar from "./NavBar";
import ProjectsList from "./ProjectsList";

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch("/check_session").then((r) => {
      if (r.ok) {
        r.json().then((user) => setUser(user));
      }
    });
  }, []);

  function handleLogin(user) {
    setUser(user);
  }

  function handleLogout() {
    fetch("/logout", { method: "DELETE" }).then((r) => {
      if (r.ok) {
        setUser(null);
      }
    });
  }

  return (
    <>
      <NavBar user={user} onLogout={handleLogout} />
      {user ? (
        <Route path="/">
          <ProjectsList />
        </Route>
      ) : (
        <main>
          <Switch>
            <Route path="/signup">
              <SignUp onLogin={setUser} />
            </Route>
            <Route path="/login">
              <Login onLogin={handleLogin} />
            </Route>
            <Route path="/">
              <Home />
            </Route>
          </Switch>
        </main>
      )}
    </>
  );
}

export default App;
