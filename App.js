import React, { useEffect, useState } from "react";
import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  Container,
  Grid,
  Box,
  Card,
  CardContent,
  IconButton,
  Tooltip,
} from "@mui/material";
import FacebookIcon from "@mui/icons-material/Facebook";
import TwitterIcon from "@mui/icons-material/Twitter";
import LinkedInIcon from "@mui/icons-material/LinkedIn";
import LightModeIcon from "@mui/icons-material/LightMode";
import DarkModeIcon from "@mui/icons-material/DarkMode";
import Swal from "sweetalert2";
import "animate.css/animate.min.css";
import "./App.css";
import CustomSurplusAvatars from "./CustomSurplusAvatars.js";
import Background from "./Background.jpg";

function App() {
  const [darkMode, setDarkMode] = useState(
    () => JSON.parse(localStorage.getItem("darkMode")) || false
  );

  useEffect(() => {
    localStorage.setItem("darkMode", JSON.stringify(darkMode));
  }, [darkMode]);

  useEffect(() => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("animate__animated", "animate__fadeIn");
        }
      });
    });

    document.querySelectorAll(".animate-on-scroll").forEach((el) => {
      observer.observe(el);
    });

    return () => observer.disconnect();
  }, []);

  useEffect(() => {
    const showTermsAndConditions = async () => {
      const { value: accept } = await Swal.fire({
        title: "Terms and Conditions",
        input: "checkbox",
        inputValue: 1,
        inputPlaceholder: "I agree with the terms and conditions",
        confirmButtonText: "Continue",
        inputValidator: (result) => !result && "You need to agree with T&C",
        showClass: {
          popup: "animate__animated animate__backInDown",
        },
        hideClass: {
          popup: "animate__animated animate__fadeOutUp",
        },
      });

      if (accept) {
        Swal.fire({
          title: "You agreed with T&C :)",
          showClass: { popup: "animate__animated animate__fadeInDown" },
          hideClass: { popup: "animate__animated animate__fadeOutUp" },
        });
      }
    };

    showTermsAndConditions();
  }, []);

  const handleRedirect = () => {
    window.location.href = " http://192.168.154.107:8502";
  };

  const handleRedirect2 = () => {
    window.location.href = "http://192.168.154.107:8501   ";
  };

  const toggleDarkMode = () => {
    setDarkMode((prev) => !prev);
  };

  return (
    <Box className={darkMode ? "dark-theme" : "light-theme"}>
      {/* Header */}
      <AppBar
        position="sticky"
        color="transparent"
        elevation={4}
        sx={{
          backdropFilter: "blur(20px)",
          transition: "all 0.5s ease-in-out",
        }}
      >
        <Toolbar>
          <Typography
            variant="h6"
            component="div"
            sx={{
              flexGrow: 1,
              textAlign: "center",
              color: darkMode ? "#fff" : "#000",
            }}
          >
            CropPredict
          </Typography>
          <Tooltip title="Toggle Dark/Light Mode">
            <IconButton onClick={toggleDarkMode}>
              {darkMode ? (
                <LightModeIcon sx={{ color: "#fff" }} />
              ) : (
                <DarkModeIcon />
              )}
            </IconButton>
          </Tooltip>
        </Toolbar>
      </AppBar>

      {/* Hero Section */}
      <Box
        id="home"
        sx={{
          minHeight: "100vh",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          textAlign: "center",
          backgroundImage: `linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url(${Background})`,
          backgroundSize: "cover",
          backgroundPosition: "center",
          color: "White",
        }}
      >
        <Box>
          <Typography
            variant="h2"
            className="animate__animated animate__fadeInDown"
          >
            Predict Your Crop Yield
          </Typography>
          <Typography
            variant="h6"
            className="animate__animated animate__fadeInUp animate__delay-1s"
            sx={{ mt: 2 }}
          >
            We utilize data-driven insights to maximize agricultural
            productivity.
          </Typography>
          <Button
            variant="contained"
            color="primary"
            onClick={handleRedirect}
            sx={{
              mt: 5,
              px: 5,
              py: 2,
              backgroundColor: "#007BFF",
              "&:hover": {
                backgroundColor: "#0056b3",
              },
            }}
            className="animate__animated animate__pulse animate__infinite"
          >
            Go to Prediction Tool
          </Button>
          <br />
          <Button
            variant="contained"
            color="primary"
            onClick={handleRedirect2}
            sx={{
              mt: 5,
              px: 5,
              py: 2,
              backgroundColor: "#007BFF",
              "&:hover": {
                backgroundColor: "#0056b3",
              },
            }}
            className="animate__animated animate__pulse animate__infinite"
          >
            Go to Prediction Tool for India
          </Button>
        </Box>
      </Box>

      {/* Features Section */}
      <Container id="features" sx={{ py: 8 }}>
        <Typography
          variant="h3"
          align="center"
          sx={{ mb: 5 }}
          className="animate-on-scroll"
        >
          Features
        </Typography>
        <Grid container spacing={4} className="animate-on-scroll">
          <Grid item xs={12} sm={6} md={3}>
            <Card
              elevation={3}
              sx={{
                p: 3,
                transition: "0.3s",
                "&:hover": { transform: "scale(1.05)" },
              }}
            >
              <CardContent>
                <Typography variant="h5" gutterBottom>
                  Data Analytics
                </Typography>
                <Typography>
                  We provide deep insights into historical data to make accurate
                  predictions.
                </Typography>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} sm={6} md={3}>
            <Card
              elevation={3}
              sx={{
                p: 3,
                transition: "0.3s",
                "&:hover": { transform: "scale(1.05)" },
              }}
            >
              <CardContent>
                <Typography variant="h5" gutterBottom>
                  Soil Analysis
                </Typography>
                <Typography>
                  We analyze soil conditions to determine the best crop options.
                </Typography>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} sm={6} md={3}>
            <Card
              elevation={3}
              sx={{
                p: 3,
                transition: "0.3s",
                "&:hover": { transform: "scale(1.05)" },
              }}
            >
              <CardContent>
                <Typography variant="h5" gutterBottom>
                  Area Analysis
                </Typography>
                <Typography>
                  We analyze area conditions to determine the best crop options.
                </Typography>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12} sm={6} md={3}>
            <Card
              elevation={3}
              sx={{
                p: 3,
                transition: "0.3s",
                "&:hover": { transform: "scale(1.05)" },
              }}
            >
              <CardContent>
                <Typography variant="h5" gutterBottom>
                  Weather Predictions
                </Typography>
                <Typography>
                  Our app utilizes weather forecasts to optimize farming
                  decisions.
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        </Grid>
      </Container>

      {/* Testimonials Section */}
      <Box
        id="testimonials"
        sx={{ py: 8, backgroundColor: darkMode ? "#333" : "#f5f5f5" }}
      >
        <Container>
          <Typography
            variant="h3"
            align="center"
            gutterBottom
            className="animate-on-scroll"
          >
            What Our Users Say
          </Typography>
          <Grid container spacing={4} justifyContent="center">
            <Grid item xs={12} md={4} className="animate-on-scroll">
              <Card
                elevation={3}
                sx={{
                  p: 3,
                  textAlign: "center",
                  transition: "0.3s",
                  "&:hover": { transform: "scale(1.05)" },
                }}
              >
                <CardContent>
                  <Typography variant="body1">
                    "This tool helped me increase my yield by 20%"
                  </Typography>
                  <Typography variant="caption" display="block">
                    Rakesh
                  </Typography>
                </CardContent>
              </Card>
            </Grid>

            {/* Avatar Group */}
            <Grid
              item
              xs={12}
              md={8}
              className="animate-on-scroll"
              sx={{ display: "flex", justifyContent: "center" }}
            >
              <CustomSurplusAvatars darkMode={darkMode} />
            </Grid>
          </Grid>
        </Container>
      </Box>

      {/* Footer */}
      <Box
        component="footer"
        sx={{
          backgroundColor: darkMode ? "#222" : "#333",
          color: "#fff",
          py: 3,
        }}
      >
        <Container>
          <Grid container justifyContent="space-between" alignItems="center">
            <Typography variant="body2">
              &copy; {new Date().getFullYear()} CropPredict. All rights
              reserved.
              Credits:-
              Sayantan,Tamajit,Sushmita,Prithisha & Chandrima.
            </Typography>
            <Box>
              <IconButton href="#" color="inherit">
                <FacebookIcon />
              </IconButton>
              <IconButton href="#" color="inherit">
                <TwitterIcon />
              </IconButton>
              <IconButton href="#" color="inherit">
                <LinkedInIcon />
              </IconButton>
            </Box>
          </Grid>
        </Container>
      </Box>
    </Box>
  );
}

export default App;
