import { Box, Flex } from "@chakra-ui/react"
import { Chat } from "../../components";
import SearchInput from "../../components/SearchInput"
import TopNav from "../../components/TopNav"
import { useStore } from "../../hooks/useStore";

const Home = () => {

  const sendFirstAidMessage = useStore((state) => state.sendMessage)
  const myChats = useStore((state) => state.chats)

  // Dummy data for the chat messages
  const messages = [
    {
      senderMessage: "Hello!",
      replyMessage: "Hi there!",
    },
    {
      senderMessage: "How are you?",
      replyMessage: "I'm good, thank you!",
    },
    {
      senderMessage: "Hello!",
      replyMessage: "Hi there!",
    },
    {
      senderMessage: "How are you?",
      replyMessage: "I'm good, thank you!",
    },{
      senderMessage: "Hello!",
      replyMessage: "Hi there!",
    },
    {
      senderMessage: "How are you?",
      replyMessage: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Suscipit, velit!",
    },
    // Add more messages as needed
  ];

  const submitMessage = (text) => {

    // hit the backend endpiint 
    if (text) {
      sendFirstAidMessage({text}).then(res => {
        console.log("this is my res", res)
      })
    }
  }

  return (
    <>
      <TopNav />


      {/* Render the Chat component */}
      <Box marginTop="2rem" textAlign="center" minHeight={'70vh'} maxHeight={'70vh'} overflowY={'scroll'}>
        <Chat messages={myChats} />
      </Box>

      <Flex alignItems={'flex-end'} w={'50%'} h={'10vh'} marginX={'auto'} marginY={'4'}>
        <SearchInput handleClick={submitMessage} />
      </Flex>

      {/* Render Chat component at the top */}
      {/* <Box position="fixed" top="0" left="50%" transform="translateX(-50%)" zIndex="999">
        <Chat messages={messages} /> */}
      {/* </Box> */}

      {/* Render SearchInput component at the bottom
      <Box position="fixed" bottom="0" left="50%" transform="translateX(-50%)" zIndex="999">
        <SearchInput />
      </Box> */}
    </>
  )
}

export default Home