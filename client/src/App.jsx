import { Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Profile from "./pages/Profile";
import SignUp from "./pages/SignUp";
import { PrivateRouteGuard, PublicRouteGuard } from "./utils/auth";

function App() {
  return (
    <>
      <Routes>
        <Route
          path="/"
          element={
            <PrivateRouteGuard>
              <Home />
            </PrivateRouteGuard>
          }
        />

        <Route
          path="/login"
          element={
            <PublicRouteGuard>
              <Login />
            </PublicRouteGuard>
          }
        />

        <Route
          path="/register"
          element={
            <PublicRouteGuard>
              <SignUp />
            </PublicRouteGuard>
          }
        />

        <Route
          path="/profile"
          element={
            <PrivateRouteGuard>
              <Profile />
            </PrivateRouteGuard>
          }
        />
      </Routes>
    </>
  );
}

export default App;
