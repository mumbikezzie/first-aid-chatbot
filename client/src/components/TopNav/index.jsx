import { MoonIcon, SunIcon } from "@chakra-ui/icons";
import {
  Avatar,
  Box,
  Button,
  Divider,
  Flex,
  IconButton,
  Spacer,
  Stack,
  Text,
  useColorMode,
  Wrap,
  WrapItem,
} from "@chakra-ui/react";
import _ from "lodash";
import { User, User2Icon } from "lucide-react";
import { useNavigate } from "react-router-dom";
import { useStore } from "../../hooks/useStore";

function TopNav() {
  const { colorMode, toggleColorMode } = useColorMode();

  const navigate = useNavigate();
  const posUser = useStore((state) => state.user);

  return (
    <Flex maxW="100%" w="100vw" h={'80px'} px={4} boxShadow={'sm'} alignItems={'center'}>
      <Box fontWeight={"bold"} fontSize={"2rem"}>
        F<span style={{ color: "#D78521" }}>A.</span>
      </Box>
      <Spacer />
      <Wrap pt="2" cursor={'pointer'}>
        <WrapItem mt={1} pr={4} onClick={() => navigate("/profile")}>
          <IconButton
            aria-label="loguout"
            variant="ghost"
            _hover={{ bg: "none" }}
            icon={<User />}
          />
          <Box>
            <Box fontSize="14px" fontWeight="extrabold">
              {!_.isEmpty(posUser) ? `${posUser.first_name.toUpperCase()}` : ``}
            </Box>
            <Box fontSize="14px">
              {!_.isEmpty(posUser) ? `${posUser.email}` : ``}
            </Box>
          </Box>
        </WrapItem>

        <Divider orientation="vertical" height={"auto"} />

        <WrapItem mt={1} pl={4}>
          <Button onClick={toggleColorMode}>
            {colorMode === "light" ? <MoonIcon /> : <SunIcon />}
          </Button>
        </WrapItem>
      </Wrap>
    </Flex>
  );
}

export default TopNav;
