import { create } from "zustand";
import { devtools, persist, createJSONStorage } from "zustand/middleware";
import _ from "lodash";
import toast from "react-hot-toast";

// const BASEURL = process.env.REACT_APP_BASE_URL;
const BASEURL = "http://localhost:8000/api/v1";

export const useStore = create()(
  devtools(
    persist(
      (set) => ({
        authLoading: false,
        isAuthenticated: false,
        user: null,

        // USER MANAGEMENT

        signInUser: async (userDetails) => {
          try {
            set({ authLoading: true });
            const signInUrl = `${BASEURL}/user/login/access-token`;

            // create the form data
            const userCredentials = new FormData();

            userCredentials.append("username", userDetails.email);
            userCredentials.append("password", userDetails.password);

            const response = await fetch(signInUrl, {
              method: "POST",
              body: userCredentials,
              headers: {
                // Set the appropriate headers for form data
                // Note that you don't need to specify 'Content-Type' here, as FormData sets it automatically
              },
            });

            if (response.ok) {
              set({ authLoading: false });
              const result = await response.json();
              if (!_.isEmpty(result)) {
                // destructre the various params
                const { access_token, user } = result;
                // set the access token to local
                window.localStorage.setItem(
                  "first_aid_access_token",
                  access_token
                );
                set({ user: user });
                return user;
              }
            } else {
              set({ authLoading: false });
              return response.json();
            }
          } catch (error) {
            set({ authLoading: false });
            const errorMessage = error.message
              ? error.message
              : "An error occurred. Please contact support!";
            toast.error(errorMessage, {
              duration: 5000,
              position: "top-center",
              style: { background: "#d00000", color: "#fff" },
            });
            return error;
          }
        },

        signUpUser: async (userDetails) => {
          try {
            set({ authLoading: true });
            const signUpUrl = `${BASEURL}/users`;

            const response = await fetch(signUpUrl, {
              method: "POST",
              body: JSON.stringify(userDetails),
              headers: {
                "Content-Type": "application/json",
                // Set the appropriate headers for form data
                // Note that you don't need to specify 'Content-Type' here, as FormData sets it automatically
              },
            });

            if (response.ok) {
              set({ authLoading: false });
              const result = await response.json();
              if (!_.isEmpty(result)) {
                return result;
              }
            } else {
              set({ authLoading: false });
              return response.json();
            }
          } catch (error) {
            set({ authLoading: false });
            const errorMessage = error.message
              ? error.message
              : "An error occurred. Please contact support!";
            toast.error(errorMessage, {
              duration: 5000,
              position: "top-center",
              style: { background: "#d00000", color: "#fff" },
            });
            return error;
          }
        },

        signOutUser: async () => {
          try {
            window.localStorage.removeItem("first_aid_access_token");
            window.localStorage.removeItem("first_aid_storage");
            return { message: "successs" };
          } catch (error) {
            console.log(error);
            const errorMessage = error.message
              ? error.message
              : "An error occurred. Please contact support!";
            toast.error(errorMessage, {
              duration: 5000,
              position: "top-center",
              style: { background: "#d00000", color: "#fff" },
            });
            set({ loading: false });
          }
        },

        // CHAT MANAGENMENT
        chats: [],
        chat: null,

        sendMessage: async (messageDetails) => {
          try {
            const sendmessageUrl = `${BASEURL}/first-aid/chat-me`;
            const token = window.localStorage.getItem("first_aid_access_token");

            const response = await fetch(sendmessageUrl, {
              method: "POST",
              headers: {
                authorization: `Bearer ${token}`,
                "Content-Type": "application/json",
              },
              body: JSON.stringify(messageDetails),
            });

            if (response.ok) {
              const result = await response.json();

              if (result.message === "Sorry,I don't understand that.") {
                let x = {
                  senderMessage: messageDetails.text,
                  replyMessage: result.message,
                };

                set({ chats: [x] });
              } else {
                console.log(result.message);

                let x = {
                  senderMessage: result.message[0].sender_message,
                  replyMessage: result.message[0].reply_message,
                };

                set({ chats: [x] });
              }

              return result;
            } else {
              const result = await response.json();
              return result;
            }
          } catch (error) {
            set({ authLoading: false });
            const errorMessage = error.message
              ? error.message
              : "An error occurred. Please contact support!";
            toast.error(errorMessage, {
              duration: 5000,
              position: "top-center",
              style: { background: "#d00000", color: "#fff" },
            });
            return error;
          }
        },
      }),
      {
        name: "first-aid-storage",
        storage: createJSONStorage(() => window.localStorage),
      }
    )
  )
);
