import {
  Box,
  Button,
  Flex,
  FormControl,
  FormErrorMessage,
  FormLabel,
  Input,
  Link,
  Spinner,
  Stack,
  Text,
  Image,
  useToast
} from "@chakra-ui/react";
import { Field, Form, Formik } from "formik";
import * as Yup from "yup";
// import { useStore } from "../../../hooks/useStore";
import _ from "lodash";
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";
import { CheckIcon } from "@chakra-ui/icons";
import { FaInstagram, FaFacebook, FaTwitter } from "react-icons/fa";
import { useState } from "react";
import FirstAidImage from '../../assets/first-aid2.jpg'
import { useStore } from "../../hooks/useStore";

const initialValues = {
  email: "",
  password: "",
};

const SignupSchema = Yup.object().shape({
  email: Yup.string().email("Invalid email").required("Email is Required"),
  password: Yup.string()
    .min(6, "Password too short")
    .required("Password is Required"),
});

const Login = () => {
  const navigate = useNavigate();
  const toast = useToast()
  const authLoading = useStore((state) => state.authLoading);
  const signInUser = useStore((state) => state.signInUser);

  const handleSubmit = (userCredentials) => {
    signInUser(userCredentials).then((res) => {

      if (res?.detail) {
        toast.error(`${res?.detail}`, {
          duration: 5000,
          position: "top-center",
          style: { background: "#d00000", color: "#fff" },
        });
      } else {
        toast({
          title: "Success ☺️",
          description: "Hey Welcome back!",
          status: "success",
          duration: 9000,
          isClosable: true,
        });
        navigate("/");
      }
    });

    console.log(userCredentials)
  };

  return (
    <Flex direction={{ base: "column", md: "row" }}>
      <Box
        w={{ base: "100%", md: "40%" }}
        h={{ base: "auto", md: "90vh" }}
        display={{ base: "flex", md: "flex" }}
        justifyContent={"center"}
        alignItems={"center"}
      >
        <Box w={{ base: "100%", md: "95%", lg: "95%", xl: "95%" }} p={"8"}>
          <Flex
            alignItems={"center"}
            gap={"2"}
            display={{ base: "flex", md: "base" }}
          >
            {/* <Image w={"8"} color={"white"} src={KiqapuIconBlack} alt={"logo"} /> */}
            <Text fontWeight={"bold"} fontSize={"2rem"} marginBottom={'20'}>
              F<span style={{color: '#D78521'}}>A.</span>
            </Text>
          </Flex>

          <Text fontSize={"2xl"} marginY={"6"}>
            👋 Login to First Aid
          </Text>
          <Formik
            initialValues={initialValues}
            validationSchema={SignupSchema}
            onSubmit={handleSubmit}
          >
            <Form>
              <Stack direction="column" spacing={8}>
                <Field name="email">
                  {({ field, form }) => (
                    <FormControl
                      isInvalid={form.errors.email && form.touched.email}
                    >
                      <FormLabel>Email address</FormLabel>
                      <Input {...field} type="email" id="email" />
                      <FormErrorMessage>
                        {form.errors.email &&
                          form.touched.email &&
                          form.errors.email}
                      </FormErrorMessage>
                    </FormControl>
                  )}
                </Field>

                <Field name="password">
                  {({ field, form }) => (
                    <FormControl
                      isInvalid={form.errors.password && form.touched.password}
                    >
                      <FormLabel>Password</FormLabel>
                      <Input {...field} type="password" id="password" />
                      <FormErrorMessage>
                        {form.errors.password &&
                          form.touched.password &&
                          form.errors.password}
                      </FormErrorMessage>
                    </FormControl>
                  )}
                </Field>

                {/* <Text>Forgot password?</Text> */}

                <Button type="submit" bg={"#D78521"} colorScheme={'white'}>
                  {authLoading ? <Spinner /> : "Login to First Aid"}
                </Button>

                <Text>
                  Don't have an account?{" "}
                  <Link
                    colorScheme={"green"}
                    color={"#D78521"}
                    fontWeight={"bold"}
                    href="/register"
                  >
                    Create an account
                  </Link>
                </Text>
              </Stack>
            </Form>
          </Formik>
        </Box>
      </Box>
      <Flex
        bgColor="#52b788"
        w={{ base: "100%", md: "60%" }}
        h={{ base: "auto", md: "100vh" }}
        p={{ base: "4", md: "10" }}
        direction="column"
        justifyContent="space-between"
        display={{ base: "none", md: "flex" }} // Hide on small screens, display on tablet and larger screens
        backgroundImage={FirstAidImage}
        backgroundSize="cover" // Make the image cover the container
        backgroundPosition="center" // Center the image within the container
      >
        <Flex direction={"column"}>
          <Flex alignItems={"center"} gap={"2"}>
            {/* <Image w={"8"} color={"white"} src={KiqapuIcon} alt={"logo"} /> */}
            {/* <Text fontWeight={"bold"} fontSize={"2rem"}>
              First Aid .
            </Text> */}
          </Flex>


          {/* <Text
            fontSize="6xl"
            lineHeight={"1.2"}
            fontWeight={"bolder"}
            marginY={"8"}
          >
            Simple, Powerful Fundraising.
          </Text> */}

          {/* <Box marginY={"4"}>
            <Flex alignItems={"center"} gap={"2"} marginY={"0.5"}>
              {" "}
              <CheckIcon color={"white"} />{" "}
              <Text fontWeight={"bold"}>Seamless UI Interaction</Text>
            </Flex>
            <Flex alignItems={"center"} gap={"2"} marginY={"0.5"}>
              {" "}
              <CheckIcon color={"white"} />{" "}
              <Text fontWeight={"bold"}>Simple to Use and Customize</Text>
            </Flex>
            <Flex alignItems={"center"} gap={"2"} marginY={"0.5"}>
              {" "}
              <CheckIcon color={"white"} />{" "}
              <Text fontWeight={"bold"}>Real Time Feedback</Text>
            </Flex>
            <Flex alignItems={"center"} gap={"2"} marginY={"0.5"}>
              {" "}
              <CheckIcon color={"white"} />{" "}
              <Text fontWeight={"bold"}>Great Customer Support</Text>
            </Flex>
          </Box> */}

          {/* <Button
            w={{ base: "100%", md: "80%", lg: "80%", xl: "50%" }}
            borderRadius={"20"}
            size={"lg"}
            marginTop={"10"}
          >
            Get in Touch with Us
          </Button> */}
        </Flex>

        <Flex alignItems={"center"} gap={"8"}>
          <Text></Text>
          <Text fontSize={"1.5rem"}>
            <FaInstagram color="#343a40" />
          </Text>
          <Text fontSize={"1.5rem"}>
            <FaFacebook color="#343a40" />
          </Text>
          <Text fontSize={"1.5rem"}>
            <FaTwitter color="#343a40" />
          </Text>
        </Flex>
      </Flex>
    </Flex>
  );
};

export default Login;