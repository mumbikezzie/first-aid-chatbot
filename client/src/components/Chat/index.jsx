import PropTypes from "prop-types";
import { Avatar, Box, Flex, Text, useColorModeValue } from "@chakra-ui/react";
import AvatarImage from "../../assets/9334410.jpg";

export const Chat = ({ messages }) => {
  // Get the appropriate background color based on the current color mode
  const senderBgColor = useColorModeValue("gray.100", "gray.700");
  const replyBgColor = useColorModeValue("green.100", "green.700");

  return (
    <Box w="50%" marginX={"auto"} py="1rem" px="1rem" borderRadius="1rem">
      {/* Render each message in the chat */}
      {messages.map((message, index) => (
        <Box key={index} mb="1rem" display="flex" flexDirection="column">
          {/* Render the sender's message */}
          <Box
            bg={senderBgColor}
            borderRadius="0.5rem"
            p="0.8rem"
            alignSelf="flex-start"
            maxWidth={"70%"}
          >
            <Flex gap={1} justifyContent={'flex-start'} alignItems={'center'}>
              <Avatar src={AvatarImage} size={'xs'} />
              <Box
                fontSize="0.8rem"
                fontWeight="bold"
                textAlign={"left"}
              >
                You:
              </Box>
            </Flex>

            <Text fontSize="md" textAlign={"right"} marginY={'1rem'}>
              {message.senderMessage}
            </Text>
          </Box>

          {/* Render the reply message */}
          <Box
            bg={replyBgColor}
            borderRadius="0.5rem"
            p="1rem"
            alignSelf="flex-end"
            maxWidth={"70%"}
          >
              <Flex gap={1} justifyContent={'flex-end'} alignItems={'center'}>
              <Box
                fontSize="0.8rem"
                fontWeight="bold"
                textAlign={"left"}
              >
                FirstAid:
              </Box>
              <Avatar bg={'gray.500'} name="First Aid" size={'xs'} />
            </Flex>

            <Text fontSize="lg" textAlign={"left"} marginY={'1rem'}>
              {message.replyMessage}
            </Text>
          </Box>
        </Box>
      ))}
    </Box>
  );
};

Chat.propTypes = {
  messages: PropTypes.array,
};
