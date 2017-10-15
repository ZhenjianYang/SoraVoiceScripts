from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C3303_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C3303_1 ._SN',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_1BA3",         # 01, 1
        "Function_2_1BC9",         # 02, 2
        "Function_3_1BF4",         # 03, 3
        "Function_4_1C24",         # 04, 4
        "Function_5_1C59",         # 05, 5
        "Function_6_1C7E",         # 06, 6
        "Function_7_1CA8",         # 07, 7
        "Function_8_1CD2",         # 08, 8
        "Function_9_1CF7",         # 09, 9
        "Function_10_1DCD",        # 0A, 10
        "Function_11_1EA8",        # 0B, 11
        "Function_12_1F83",        # 0C, 12
        "Function_13_205E",        # 0D, 13
        "Function_14_2139",        # 0E, 14
        "Function_15_2214",        # 0F, 15
        "Function_16_2E92",        # 10, 16
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C4")
    Return()

    label("loc_C4")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_D3")
    OP_A2(0x0)

    label("loc_D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_157")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as met Jimmy in the previous game\x01",      # 0
            "Don't change\x01",                               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_151"),
        (SWITCH_DEFAULT, "loc_157"),
    )


    label("loc_151")

    OP_A2(0x0)
    Jump("loc_157")

    label("loc_157")

    ClearChrFlags(0x8, 0x80)
    OP_72(0x0, 0x4)
    SetChrPos(0x8, 9460, 40, 112460, 90)
    SetChrPos(0x10, 9460, -40, 124460, 0)

    def lambda_189():
        TurnDirection(0x0, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_189)

    def lambda_197():
        TurnDirection(0x1, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_197)

    def lambda_1A5():
        TurnDirection(0x2, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1A5)

    def lambda_1B3():
        TurnDirection(0x3, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_1B3)
    WaitChrThread(0x3, 0x1)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_209")

    ChrTalk(    #0
        0x101,
        (
            "#1004FAh!\x02\x03",

            "Th-That's...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23A")

    label("loc_209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_225")

    ChrTalk(    #1
        0x106,
        "#052FHe's...\x02",
    )

    CloseMessageWindow()
    Jump("loc_23A")

    label("loc_225")


    ChrTalk(    #2
        0x103,
        "#023FThat's...!\x02",
    )

    CloseMessageWindow()

    label("loc_23A")

    OP_6D(11140, 0, 112460, 3000)

    NpcTalk(    #3
        0x8,
        "Man",
        "*pant* *pant* *pant*\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #4
        0x8,
        "Man",
        "Okay, I-I've managed to pull the chest up...\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x24F4, 0xA, 0x1B1A2, 0x7D0, 0x0)
    OP_8E(0x8, 0x2B84, 0xFFFFFFCE, 0x1B1A2, 0x7D0, 0x0)
    OP_8C(0x8, 0, 400)
    Sleep(1000)

    NpcTalk(    #5
        0x8,
        "Man",
        "No doubt about it. I finally found it...\x02",
    )

    CloseMessageWindow()
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)

    NpcTalk(    #6
        0x8,
        "Man",
        "#5P#4SYEAAAH! I FINALLY FOUND IT!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    ChrTalk(    #7
        0x10,
        "#4S#4P...finally found it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        "#3S#4P...found it! #2S...nd it! #1S...it!\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_8C(0x8, 270, 400)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x8)
    Sleep(400)
    OP_62(0x8, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)
    OP_8C(0x8, 0, 400)
    Sleep(2000)

    NpcTalk(    #9
        0x8,
        "Man",
        (
            "#5P#4SJIMMY, YOU'RE AMAZING!\x01",
            "I LOVE YOU!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #10
        0x10,
        "#4S#4P...amazing! I love you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        "#3S#4P...love you! #2S...ve you! #1S...you!\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    OP_63(0x8)

    NpcTalk(    #12
        0x8,
        "Man",
        (
            "Ah... I guess this isn't the\x01",
            "time to be goofing around.\x02",
        )
    )

    CloseMessageWindow()
    AddParty(0x47, 0xFA, 0xFF)
    SetChrFlags(0x148, 0x8)
    OP_43(0x101, 0x0, 0x1, 0x1)
    OP_43(0xF7, 0x0, 0x1, 0x2)
    OP_43(0xF8, 0x0, 0x1, 0x3)
    OP_43(0xF9, 0x0, 0x1, 0x4)

    NpcTalk(    #13
        0x8,
        "Man",
        (
            "I'd better check the contents before\x01",
            "some monster shows up...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_57B():
        OP_6D(11140, 0, 110010, 2000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_57B)
    WaitChrThread(0xF9, 0x0)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0x8, 0x0)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x8, 0x0, 0x0, 0x0, 0x258, 0x1388)
    Sleep(500)
    OP_63(0x8)
    TurnDirection(0x8, 0x101, 400)

    NpcTalk(    #14
        0x8,
        "Man",
        "Wh-Whoa!!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #15
        0x8,
        "Man",
        "Who are you guys?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_782")

    ChrTalk(    #16
        0x101,
        (
            "#1007F#4PForget that! Wh-What the heck are\x01",
            "you doing playing around in a place\x01",
            "like this? Are you nuts?\x02\x03",

            "*sigh* Oblivious as always.\x01",
            "You haven't changed a bit.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #17
        0x8,
        "Man",
        "Huh? You... You're...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1006F#4PHey, Jimmy. It's been a while.\x02\x03",

            "When did I take that job\x01",
            "of yours back in Ruan...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "Oh, man! That takes me back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        "So, uh, what brings you here?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8ED")

    label("loc_782")


    ChrTalk(    #21
        0x101,
        (
            "#1007F#4PForget that! What the heck are\x01",
            "you doing playing around in a\x01",
            "place like this? Are you nuts?\x02\x03",

            "I can't believe how oblivious\x01",
            "you are.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #22
        0x8,
        "Man",
        "Oblivious...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #23
        0x8,
        "Man",
        (
            "Nah. I'm just not worried. I do this\x01",
            "adventurer stuff all the time.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #24
        0x8,
        "Man",
        "So, who are you all?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1006F#4PWe're bracers.\x02\x03",

            "You're Jimmy, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        "Yup, I'm Jimmy. What about it?\x02",
    )

    CloseMessageWindow()

    label("loc_8ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_949")

    ChrTalk(    #27
        0x106,
        (
            "#050F#2PYour lodging put out a\x01",
            "search request.\x02\x03",

            "So, we came looking for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A3")

    label("loc_949")


    ChrTalk(    #28
        0x103,
        (
            "#020F#2PYour place of lodging issued\x01",
            "a search request.\x02\x03",

            "So, we came looking for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A3")


    ChrTalk(    #29
        0x8,
        (
            "Oh, you came all the way from\x01",
            "Zeiss, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        "Well, sorry, but I can't go back yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "I'm about to make the discovery\x01",
            "of the century!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A64")

    ChrTalk(    #32
        0x107,
        "#064FYou mean...that chest?\x02",
    )

    CloseMessageWindow()
    Jump("loc_ACF")

    label("loc_A64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A9F")

    ChrTalk(    #33
        0x104,
        "#033FAre you speaking of that chest?\x02",
    )

    CloseMessageWindow()
    Jump("loc_ACF")

    label("loc_A9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ACF")

    ChrTalk(    #34
        0x105,
        "#044FDo you mean that chest?\x02",
    )

    CloseMessageWindow()

    label("loc_ACF")


    ChrTalk(    #35
        0x8,
        (
            "Yeah, I managed to pull it\x01",
            "up just a moment ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1004F#4PPull it up? Like, from the lake?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "Yeah, talk about a crazy hiding\x01",
            "spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "Still, that's what I'd expect for the\x01",
            "great pirate Schirmer's treasure.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C7C")
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #39
        0x101,
        (
            "#1004F#4PWhaaat?!\x02\x03",

            "THAT'S the treasure you've been \x01",
            "looking for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        "Heh heh heh, no doubt about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "I've followed a long trail and\x01",
            "many old maps to get here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DC3")

    label("loc_C7C")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #42
        0x101,
        (
            "#1004F#4PWhaaat?! Really?!\x02\x03",

            "#1016F...Okay, honestly, I'm not really following.\x01",
            "Who is this pirate whatshisface?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #43
        0x8,
        (
            "You...\x01",
            "You don't know the\x01",
            "great pirate Schirmer?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "Unbelievable. How can you call\x01",
            "yourself a citizen of Ruan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        "#1016F#4PUm... This is Zeiss.\x02",
    )

    CloseMessageWindow()

    label("loc_DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_E52")

    ChrTalk(    #46
        0x106,
        (
            "#551F#2PLook, I don't care whose damn\x01",
            "treasure it is, just hurry up.\x02\x03",

            "If we hang around here, the\x01",
            "monsters are gonna notice us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB2")

    label("loc_E52")


    ChrTalk(    #47
        0x103,
        (
            "#025F#2PLook, I don't care, just hurry.\x02\x03",

            "If we linger, the monsters\x01",
            "are sure to notice us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB2")


    ChrTalk(    #48
        0x8,
        "Whoa, yeah, right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "A-All right. I'm gonna do it!\x01",
            "I'm gonna open the chest!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)
    OP_94(0x1, 0x8, 0x0, 0xC8, 0x3E8, 0x0)
    Sleep(1000)
    OP_70(0x0, 0x3C)
    OP_22(0x2B, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)

    ChrTalk(    #50
        0x101,
        (
            "#1002F#4PWh-Why're you quiet all of\x01",
            "a sudden?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8)
    OP_94(0x1, 0x8, 0x0, 0xC8, 0x3E8, 0x0)

    ChrTalk(    #51
        0x8,
        "#6PG-Give me a second.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        "#6PWhaaa...? What is this...?\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    Sleep(1000)
    OP_22(0xAC, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x8, 0x0, 0x0, 0xFFFFFE70, 0x258, 0x1388)

    ChrTalk(    #53
        0x8,
        (
            "#6PWh-Whoaaa!\x01",
            "Phew! That sure surprised me.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x101, 0x0, 0x1, 0x5)
    OP_43(0xF7, 0x0, 0x1, 0x6)
    OP_43(0xF8, 0x0, 0x1, 0x7)
    OP_43(0xF9, 0x0, 0x1, 0x8)
    Sleep(2000)
    OP_44(0x101, 0x0)
    OP_44(0xF7, 0x0)
    OP_44(0xF8, 0x0)
    OP_44(0xF9, 0x0)

    ChrTalk(    #54
        0x101,
        (
            "#1004F#4PUh... Anyone else hear that?\x02\x03",

            "#1020FOh, man. This is sooo a trap,\x01",
            "isn't it?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1101")

    ChrTalk(    #55
        0x106,
        "#057F#2PDunno, but I've got a bad feeling.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1138")

    label("loc_1101")


    ChrTalk(    #56
        0x103,
        "#022F#2PI don't know, but I have a bad feeling...\x02",
    )

    CloseMessageWindow()

    label("loc_1138")

    OP_22(0x24B, 0x0, 0x32)
    Sleep(200)
    OP_22(0x24B, 0x0, 0x32)
    Sleep(500)
    OP_22(0x24B, 0x0, 0x46)
    Sleep(200)
    OP_22(0x24B, 0x0, 0x46)
    Sleep(200)
    OP_22(0x24B, 0x0, 0x46)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11DB")
    OP_8C(0x108, 180, 400)
    Fade(500)
    SetChrChipByIndex(0x108, 20)
    OP_0D()

    ChrTalk(    #57
        0x108,
        (
            "#070FLooks like your bad feeling\x01",
            "was right on the mark.\x02\x03",

            "#072FHere they come!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12AE")

    label("loc_11DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1242")
    OP_8C(0x104, 180, 400)
    Fade(500)
    SetChrChipByIndex(0x104, 14)
    OP_0D()

    ChrTalk(    #58
        0x104,
        (
            "#035FHeh, your premonition was\x01",
            "correct.\x02\x03",

            "The enemy is upon us!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12AE")

    label("loc_1242")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12AE")
    OP_8C(0x105, 180, 400)
    Fade(500)
    SetChrChipByIndex(0x105, 16)
    OP_0D()

    ChrTalk(    #59
        0x105,
        (
            "#042FThat bad feeling of yours\x01",
            "was right on the mark.\x02\x03",

            "Here they come!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12AE")

    OP_43(0x8, 0x1, 0x1, 0x10)

    def lambda_12BB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_12BB)

    def lambda_12C9():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_12C9)

    def lambda_12D7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_12D7)

    def lambda_12E5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_12E5)

    def lambda_12F3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_12F3)
    WaitChrThread(0x8, 0x1)
    OP_1D(0x29)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    OP_43(0xA, 0x1, 0x1, 0x9)
    OP_43(0xB, 0x1, 0x1, 0xA)
    OP_43(0xC, 0x1, 0x1, 0xB)
    OP_43(0xD, 0x1, 0x1, 0xC)
    OP_43(0xE, 0x1, 0x1, 0xD)
    OP_43(0xF, 0x1, 0x1, 0xE)

    def lambda_1350():
        OP_6D(11140, 0, 95380, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1350)
    WaitChrThread(0x101, 0x1)
    Sleep(2500)
    SetChrPos(0x8, 10000, 20, 111560, 135)
    SetChrPos(0x101, 10430, -70, 109710, 225)
    SetChrPos(0xF7, 11930, -70, 109190, 180)
    SetChrPos(0xF8, 13420, -30, 109960, 135)
    SetChrPos(0xF9, 13630, -30, 111710, 135)
    SetChrChipByIndex(0x101, 8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_13D5")
    SetChrChipByIndex(0x106, 12)
    Jump("loc_13DA")

    label("loc_13D5")

    SetChrChipByIndex(0x103, 10)

    label("loc_13DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13ED")
    SetChrChipByIndex(0x107, 18)

    label("loc_13ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1400")
    SetChrChipByIndex(0x104, 14)

    label("loc_1400")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1413")
    SetChrChipByIndex(0x105, 16)

    label("loc_1413")


    def lambda_1419():
        OP_6D(11140, 0, 111010, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1419)
    WaitChrThread(0x101, 0x1)
    OP_8F(0x8, 0x24A4, 0x28, 0x1B620, 0x3E8, 0x0)

    ChrTalk(    #60
        0x8,
        "Wh-Whoa! There are tons of 'em!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x9, 7000, -3500, 119800, 135)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x9, 800)

    ChrTalk(    #61
        0x101,
        "#1005F#2PJimmy! Behind you--!\x02",
    )

    CloseMessageWindow()

    def lambda_14D0():
        OP_6D(8400, 0, 116840, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14D0)

    def lambda_14E8():
        OP_6B(2480, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14E8)

    def lambda_14F8():
        OP_6C(0, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_14F8)
    Sleep(400)

    def lambda_150D():

        label("loc_150D")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_150D")

    QueueWorkItem2(0xF7, 2, lambda_150D)

    def lambda_151E():

        label("loc_151E")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_151E")

    QueueWorkItem2(0xF8, 2, lambda_151E)

    def lambda_152F():

        label("loc_152F")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_152F")

    QueueWorkItem2(0xF9, 2, lambda_152F)
    WaitChrThread(0x101, 0x1)
    OP_22(0xE3, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #62
        0x8,
        "Huh?!\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp012_00.eff")
    LoadEffect(0x1, "monster\\\\msc0591.eff")
    LoadEffect(0x2, "monster\\\\msc0590.eff")
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_15AA():
        OP_67(0, 5840, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15AA)

    def lambda_15C2():
        OP_6D(8300, 0, 115820, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_15C2)

    def lambda_15DA():
        OP_6B(2640, 2000)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_15DA)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x800)
    ClearChrFlags(0x9, 0x80)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1604():
        OP_96(0xFE, 0x21A2, 0x28A, 0x1BABC, 0x1F40, 0xFA0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1604)

    def lambda_1622():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1622)
    OP_22(0xE4, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 7000, -1500, 119800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    def lambda_1673():
        OP_99(0xFE, 0x1, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1673)
    WaitChrThread(0x9, 0x0)
    OP_22(0xE5, 0x0, 0x64)
    OP_7C(0x0, 0x258, 0xBB8, 0xC8)

    def lambda_169E():
        OP_96(0xFE, 0x2620, 0x1E, 0x1B4CC, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_169E)

    def lambda_16BC():
        OP_9E(0xFE, 0x14, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_16BC)

    def lambda_16D6():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x3E8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_16D6)

    def lambda_16F4():
        OP_99(0xFE, 0x4, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_16F4)
    WaitChrThread(0x9, 0x2)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 0)
    WaitChrThread(0x9, 0x0)
    ClearChrFlags(0x9, 0x800)
    OP_22(0xE5, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xBB8, 0x64)

    def lambda_1733():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1733)

    def lambda_1751():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1751)
    WaitChrThread(0x8, 0x0)
    OP_44(0x8, 0x1)
    OP_44(0xF7, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)
    OP_8C(0x101, 315, 0)
    OP_8C(0xF7, 315, 0)
    OP_8C(0xF8, 315, 0)
    OP_8C(0xF9, 315, 0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)

    def lambda_17A4():
        OP_6D(10100, 0, 112800, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_17A4)

    def lambda_17BC():
        OP_6C(356000, 2000)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_17BC)

    def lambda_17CC():
        OP_6B(3340, 2000)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_17CC)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)

    def lambda_17E6():

        label("loc_17E6")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_17E6")

    QueueWorkItem2(0x9, 3, lambda_17E6)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x8, 0x2AA8, 0xFFFFFFCE, 0x1B198, 0xBB8, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #63
        0x8,
        "#2PWH-WHOA! Over here too!!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    Sleep(1000)
    SetChrFlags(0x9, 0x800)
    OP_44(0x9, 0x3)
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 0)
    OP_99(0x9, 0x0, 0x5, 0x5DC)
    Sleep(200)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF8, 0x1)
    OP_99(0x9, 0x5, 0x7, 0x5DC)
    ClearChrFlags(0x9, 0x800)
    SetChrFlags(0x9, 0x8000)
    SetChrSubChip(0x9, 0)

    def lambda_18A0():

        label("loc_18A0")

        OP_99(0xFE, 0x0, 0x1, 0x5DC)
        OP_48()
        Jump("loc_18A0")

    QueueWorkItem2(0x9, 3, lambda_18A0)

    def lambda_18B3():

        label("loc_18B3")

        OP_7C(0x32, 0x0, 0xBB8, 0x64)
        OP_48()
        Jump("loc_18B3")

    QueueWorkItem2(0x9, 2, lambda_18B3)
    PlayEffect(0x2, 0x1, 0x9, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(    #64
        0x101,
        (
            "#1019F#2PAnother evil penguin.\x01",
            "Surprise, surprise.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1966")

    ChrTalk(    #65
        0x107,
        "#065FWhaa-whaaawhaaa...!\x02",
    )

    CloseMessageWindow()

    label("loc_1966")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19B9")

    ChrTalk(    #66
        0x108,
        (
            "#070FHmph... I guess that's the\x01",
            "new lord of this little domain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_19E9")

    ChrTalk(    #67
        0x106,
        "#054F#2PHeads up! Here it comes!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A15")

    label("loc_19E9")


    ChrTalk(    #68
        0x103,
        "#024F#2PWatch out! It's coming for us!\x02",
    )

    CloseMessageWindow()

    label("loc_1A15")

    OP_63(0x8)
    OP_82(0x1, 0x2)
    OP_44(0x9, 0x2)
    OP_44(0x9, 0x3)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 24)
    SetChrSubChip(0x9, 0)

    def lambda_1A3C():
        OP_96(0xFE, 0x2E04, 0x0, 0x1AFB8, 0x3E8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1A3C)

    def lambda_1A5A():
        OP_99(0xFE, 0x0, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1A5A)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(200)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    SetChrPos(0x10, 11780, 0, 110520, 0)
    TurnDirection(0xA, 0x10, 0)
    TurnDirection(0xB, 0x10, 0)
    TurnDirection(0xC, 0x10, 0)
    TurnDirection(0xD, 0x10, 0)
    TurnDirection(0xE, 0x10, 0)
    TurnDirection(0xF, 0x10, 0)

    def lambda_1AC7():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1AC7)

    def lambda_1ADD():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1ADD)

    def lambda_1AF3():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1AF3)

    def lambda_1B09():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1B09)

    def lambda_1B1F():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1B1F)

    def lambda_1B35():
        OP_94(0x1, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1B35)
    Sleep(200)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    Battle(0x1EA, 0x0, 0x1, 0x0, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1B9B"),
        (SWITCH_DEFAULT, "loc_1B9E"),
    )


    label("loc_1B9B")

    OP_B4(0x0)
    Return()

    label("loc_1B9E")

    Call(1, 15)
    Return()

    # Function_0_AA end

    def Function_1_1BA3(): pass

    label("Function_1_1BA3")

    SetChrPos(0x101, 11700, -30, 102960, 0)
    OP_8E(0x101, 0x2DB4, 0xFFFFFFB0, 0x1AA4A, 0x7D0, 0x0)
    Return()

    # Function_1_1BA3 end

    def Function_2_1BC9(): pass

    label("Function_2_1BC9")

    Sleep(400)
    SetChrPos(0xF7, 11100, -10, 102320, 0)
    OP_8E(0xF7, 0x2B5C, 0xFFFFFFD8, 0x1A59A, 0x7D0, 0x0)
    Return()

    # Function_2_1BC9 end

    def Function_3_1BF4(): pass

    label("Function_3_1BF4")

    Sleep(400)
    Sleep(200)
    SetChrPos(0xF8, 12540, -50, 103220, 0)
    OP_8E(0xF8, 0x30FC, 0xFFFFFFCE, 0x1A77A, 0x7D0, 0x0)
    Return()

    # Function_3_1BF4 end

    def Function_4_1C24(): pass

    label("Function_4_1C24")

    Sleep(400)
    Sleep(200)
    Sleep(600)
    SetChrPos(0xF9, 11970, -40, 102840, 0)
    OP_8E(0xF9, 0x2EC2, 0xFFFFFFD8, 0x1A216, 0x7D0, 0x0)
    Return()

    # Function_4_1C24 end

    def Function_5_1C59(): pass

    label("Function_5_1C59")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C7D")
    OP_8C(0x101, 315, 400)
    Sleep(200)
    OP_8C(0x101, 45, 400)
    Sleep(500)
    Jump("Function_5_1C59")

    label("loc_1C7D")

    Return()

    # Function_5_1C59 end

    def Function_6_1C7E(): pass

    label("Function_6_1C7E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CA7")
    Sleep(100)
    OP_8C(0xF7, 270, 400)
    Sleep(200)
    OP_8C(0xF7, 89, 400)
    Sleep(300)
    Jump("Function_6_1C7E")

    label("loc_1CA7")

    Return()

    # Function_6_1C7E end

    def Function_7_1CA8(): pass

    label("Function_7_1CA8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CD1")
    Sleep(100)
    OP_8C(0xF8, 89, 400)
    Sleep(200)
    OP_8C(0xF8, 270, 400)
    Sleep(400)
    Jump("Function_7_1CA8")

    label("loc_1CD1")

    Return()

    # Function_7_1CA8 end

    def Function_8_1CD2(): pass

    label("Function_8_1CD2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CF6")
    OP_8C(0xF9, 45, 400)
    Sleep(200)
    OP_8C(0xF9, 315, 400)
    Sleep(500)
    Jump("Function_8_1CD2")

    label("loc_1CF6")

    Return()

    # Function_8_1CD2 end

    def Function_9_1CF7(): pass

    label("Function_9_1CF7")

    SetChrPos(0xA, 12070, 0, 82290, 0)
    OP_62(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xA, 0x2F26, 0x28, 0x16DB4, 0x1388, 0x0)
    OP_8E(0xA, 0x22CE, 0x28, 0x17ACA, 0x1388, 0x0)
    OP_62(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xA, 0x22CE, 0x14, 0x189E8, 0x1388, 0x0)
    OP_8E(0xA, 0x2E54, 0xFFFFFFF6, 0x197B2, 0x1388, 0x0)
    OP_62(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xA, 0x2E54, 0xFFFFFFF6, 0x19C30, 0x1388, 0x0)
    OP_8E(0xA, 0x3CE6, 0xFFFFFFF6, 0x1B0D0, 0x1388, 0x0)
    TurnDirection(0xA, 0x101, 400)
    OP_63(0xA)
    OP_22(0x24B, 0x0, 0x50)
    OP_43(0xA, 0x0, 0x6, 0x2)
    Return()

    # Function_9_1CF7 end

    def Function_10_1DCD(): pass

    label("Function_10_1DCD")

    Sleep(500)
    OP_62(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    SetChrPos(0xB, 12070, 0, 82290, 0)
    OP_8E(0xB, 0x2F26, 0x28, 0x16DB4, 0x1388, 0x0)
    OP_8E(0xB, 0x22CE, 0x28, 0x17ACA, 0x1388, 0x0)
    OP_62(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xB, 0x22CE, 0x14, 0x189E8, 0x1388, 0x0)
    OP_8E(0xB, 0x2E54, 0xFFFFFFF6, 0x197B2, 0x1388, 0x0)
    OP_62(0xB, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xB, 0x2E54, 0xFFFFFFF6, 0x19C30, 0x1388, 0x0)
    OP_8E(0xB, 0x20E4, 0xFFFFFFF6, 0x1A86A, 0x1388, 0x0)
    TurnDirection(0xB, 0x101, 400)
    OP_63(0xB)
    OP_22(0x24B, 0x0, 0x50)
    OP_43(0xB, 0x0, 0x6, 0x2)
    Return()

    # Function_10_1DCD end

    def Function_11_1EA8(): pass

    label("Function_11_1EA8")

    Sleep(1000)
    OP_62(0xC, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    SetChrPos(0xC, 12070, 0, 82290, 0)
    OP_8E(0xC, 0x2F26, 0x28, 0x16DB4, 0x1388, 0x0)
    OP_8E(0xC, 0x22CE, 0x28, 0x17ACA, 0x1388, 0x0)
    OP_62(0xC, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xC, 0x22CE, 0x14, 0x189E8, 0x1388, 0x0)
    OP_8E(0xC, 0x2E54, 0xFFFFFFF6, 0x197B2, 0x1388, 0x0)
    OP_62(0xC, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xC, 0x2E54, 0xFFFFFFF6, 0x19C30, 0x1388, 0x0)
    OP_8E(0xC, 0x3ADE, 0xFFFFFFCE, 0x1A93C, 0x1388, 0x0)
    TurnDirection(0xC, 0x101, 400)
    OP_63(0xC)
    OP_22(0x24B, 0x0, 0x50)
    OP_43(0xC, 0x0, 0x6, 0x2)
    Return()

    # Function_11_1EA8 end

    def Function_12_1F83(): pass

    label("Function_12_1F83")

    Sleep(1500)
    OP_62(0xD, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    SetChrPos(0xD, 12070, 0, 82290, 0)
    OP_8E(0xD, 0x2F26, 0x28, 0x16DB4, 0x1388, 0x0)
    OP_8E(0xD, 0x22CE, 0x28, 0x17ACA, 0x1388, 0x0)
    OP_62(0xD, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xD, 0x22CE, 0x14, 0x189E8, 0x1388, 0x0)
    OP_8E(0xD, 0x2E54, 0xFFFFFFF6, 0x197B2, 0x1388, 0x0)
    OP_62(0xD, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xD, 0x2E54, 0xFFFFFFF6, 0x19C30, 0x1388, 0x0)
    OP_8E(0xD, 0x27A6, 0xFFFFFFEC, 0x1A2C0, 0x1388, 0x0)
    TurnDirection(0xD, 0x101, 400)
    OP_63(0xD)
    OP_22(0x24B, 0x0, 0x50)
    OP_43(0xD, 0x0, 0x6, 0x2)
    Return()

    # Function_12_1F83 end

    def Function_13_205E(): pass

    label("Function_13_205E")

    Sleep(2000)
    OP_62(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    SetChrPos(0xE, 12070, 0, 82290, 0)
    OP_8E(0xE, 0x2F26, 0x28, 0x16DB4, 0x1388, 0x0)
    OP_8E(0xE, 0x22CE, 0x28, 0x17ACA, 0x1388, 0x0)
    OP_62(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xE, 0x22CE, 0x14, 0x189E8, 0x1388, 0x0)
    OP_8E(0xE, 0x2E54, 0xFFFFFFF6, 0x197B2, 0x1388, 0x0)
    OP_62(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xE, 0x2E54, 0xFFFFFFF6, 0x19C30, 0x1388, 0x0)
    OP_8E(0xE, 0x3584, 0xFFFFFFEC, 0x1A3D8, 0x1388, 0x0)
    TurnDirection(0xE, 0x101, 400)
    OP_63(0xE)
    OP_22(0x24B, 0x0, 0x50)
    OP_43(0xE, 0x0, 0x6, 0x2)
    Return()

    # Function_13_205E end

    def Function_14_2139(): pass

    label("Function_14_2139")

    Sleep(2500)
    OP_62(0xF, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    SetChrPos(0xF, 12070, 0, 82290, 0)
    OP_8E(0xF, 0x2F26, 0x28, 0x16DB4, 0x1388, 0x0)
    OP_8E(0xF, 0x22CE, 0x28, 0x17ACA, 0x1388, 0x0)
    OP_62(0xF, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xF, 0x22CE, 0x14, 0x189E8, 0x1388, 0x0)
    OP_8E(0xF, 0x2E54, 0xFFFFFFF6, 0x197B2, 0x1388, 0x0)
    OP_62(0xF, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_8E(0xF, 0x2E54, 0xFFFFFFF6, 0x19C30, 0x1388, 0x0)
    OP_8E(0xF, 0x2E36, 0xFFFFFFEC, 0x1A108, 0x1388, 0x0)
    TurnDirection(0xF, 0x101, 400)
    OP_63(0xF)
    OP_22(0x24B, 0x0, 0x50)
    OP_43(0xF, 0x0, 0x6, 0x2)
    Return()

    # Function_14_2139 end

    def Function_15_2214(): pass

    label("Function_15_2214")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    RemoveParty(0x47, 0xFF)
    SetMapFlags(0x10)
    OP_72(0x0, 0x4)
    OP_6F(0x0, 60)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 9960, 20, 109000, 0)
    SetChrPos(0x101, 10430, -70, 106710, 0)
    SetChrPos(0xF7, 11930, -70, 106190, 0)
    SetChrPos(0xF8, 13420, -30, 106960, 135)
    SetChrPos(0xF9, 13630, -30, 108710, 135)
    TurnDirection(0xF8, 0x8, 0)
    TurnDirection(0xF9, 0x8, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_6D(12660, -40, 109960, 0)
    OP_67(0, 5920, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #69
        0x101,
        "#1007F#2PW-Well, that was certainly...a thing.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2389")

    ChrTalk(    #70
        0x107,
        "#067F#4PIt sure was a, um, flashy bird.\x02",
    )

    CloseMessageWindow()

    label("loc_2389")


    ChrTalk(    #71
        0x8,
        (
            "#5P*pant* *pant*\x01",
            "I thought I was a goner!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2422")

    ChrTalk(    #72
        0x108,
        (
            "#070F#4PWell, we managed to push them back.\x02\x03",

            "Let's retreat before more come.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x108, 400)
    Jump("loc_2526")

    label("loc_2422")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24AC")

    ChrTalk(    #73
        0x104,
        (
            "#030F#4PHeh, we managed to push them back, hmm?\x02\x03",

            "Still, it seems best if we were\x01",
            "to make our exit...swiftly.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 400)
    Jump("loc_2526")

    label("loc_24AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2526")

    ChrTalk(    #74
        0x105,
        (
            "#040F#4PWe managed to repel them, but...\x02\x03",

            "We should probably leave\x01",
            "before we're attacked again.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 400)

    label("loc_2526")


    ChrTalk(    #75
        0x8,
        "#5PR-Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        "#5PO-Okay, then, I'll be quick.\x02",
    )

    CloseMessageWindow()
    OP_8B(0x8, 0x2B5C, 0x1B792, 0x190)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_25BE")

    ChrTalk(    #77
        0x106,
        (
            "#052F...Hold up.\x02\x03",

            "#050FLeave that to us. There could\x01",
            "be another trap.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2619")

    label("loc_25BE")


    ChrTalk(    #78
        0x103,
        (
            "#022FNo, wait a moment.\x02\x03",

            "Why don't you leave that to us?\x01",
            "There could be another trap.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2619")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0x8, 0xF7, 400)

    ChrTalk(    #79
        0x8,
        "#5PY-Yeah, good point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        "#1006F#2PWell, then, here we go.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_66(0x0)

    def lambda_2687():
        OP_6D(11140, -50, 111010, 3000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2687)
    OP_8E(0x101, 0x2CEC, 0xFFFFFFE2, 0x1A504, 0x7D0, 0x0)

    def lambda_26B3():

        label("loc_26B3")

        TurnDirection(0x8, 0x101, 400)
        OP_48()
        Jump("loc_26B3")

    QueueWorkItem2(0x8, 1, lambda_26B3)

    def lambda_26C4():

        label("loc_26C4")

        TurnDirection(0xF7, 0x101, 400)
        OP_48()
        Jump("loc_26C4")

    QueueWorkItem2(0xF7, 1, lambda_26C4)

    def lambda_26D5():

        label("loc_26D5")

        TurnDirection(0xF8, 0x101, 400)
        OP_48()
        Jump("loc_26D5")

    QueueWorkItem2(0xF8, 1, lambda_26D5)

    def lambda_26E6():

        label("loc_26E6")

        TurnDirection(0xF9, 0x101, 400)
        OP_48()
        Jump("loc_26E6")

    QueueWorkItem2(0xF9, 1, lambda_26E6)
    OP_8E(0x101, 0x2B66, 0xFFFFFFD8, 0x1B42C, 0x7D0, 0x0)
    OP_8C(0x101, 0, 400)
    OP_44(0x8, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    WaitChrThread(0x8, 0x0)
    OP_66(0x1)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)

    ChrTalk(    #81
        0x101,
        (
            "#1015F#7PHmm... Nothing seems off, really.\x02\x03",

            "I think we're okay, but...\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #82
        "Retrieved #2C#16ISilver Dew Orb#0C. \x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #83
        0x101,
        (
            "#1018F#7PAll right, the dubious pirate treasure\x01",
            "has been secured.\x02\x03",

            "#1004FWait, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        "Wh-What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#1002F#7PThere's...a scrap of paper in here.\x02\x03",

            "It looks like a letter.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Fade(500)
    SetChrChipByIndex(0x101, 23)
    OP_0D()
    Sleep(400)

    ChrTalk(    #86
        0x101,
        "#1011F#6PLet's see...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #87
        (
            "\x07\x05'In memory of my seventieth birthday\x01",
            "--and my retirement from piracy--\x01",
            "here lies my Silver Dew Orb.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #88
        (
            "\x07\x05'This gem holds the power to warn its bearer of\x01",
            "all approaching danger. I can say my living to\x01",
            "this day is thanks to none other than this jewel.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #89
        (
            "\x07\x05'However, I have grown old and weary of being\x01",
            "bothered by the 'knights' who come seeking it.'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #90
        (
            "\x07\x05'And so I sink it into this lake. You who have\x01",
            "found it, do as you please. However, as I wrote,\x01",
            "this treasure comes with its own troubles...'\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #91
        "\x07\x05- Schirmer\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()

    ChrTalk(    #92
        0x101,
        "#1002F#6PThe end.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x2B66, 0xFFFFFFCE, 0x1B01C, 0x1770, 0x0)
    TurnDirection(0x8, 0x101, 400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0x8, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x8, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x8, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x8, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x8, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x8, 0xB4, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x8, 0x0, 0xC8, 0x1B58, 0x0)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x1B58, 0x0)

    ChrTalk(    #93
        0x8,
        (
            "#4PHoly crap! L-Let me see it!\x01",
            "Pleeease!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #94
        0x101,
        (
            "#1016F#6POkay, okay, calm down.\x02\x03",

            "Zeiss first, then I'll let you have it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2CFB")

    ChrTalk(    #95
        0x106,
        (
            "#053FThough if you'd rather fight that weird\x01",
            "monster again, we can hang around...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D5A")

    label("loc_2CFB")


    ChrTalk(    #96
        0x103,
        (
            "#027FThough if you'd rather fight that strange\x01",
            "monster again, we can stay a bit longer...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D5A")


    def lambda_2D60():
        OP_8C(0x8, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2D60)
    Sleep(250)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #97
        0x8,
        "#3PP-Pass!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        "#3PGoing is good!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DD7")

    ChrTalk(    #99
        0x108,
        (
            "#070FYes, very good.\x02\x03",

            "Let's go, then!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E62")

    label("loc_2DD7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E19")

    ChrTalk(    #100
        0x104,
        (
            "#030FA wise decision.\x02\x03",

            "Yes, let us be gone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E62")

    label("loc_2E19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E62")

    ChrTalk(    #101
        0x105,
        (
            "#040FYes, that seems wise.\x02\x03",

            "Well, then. Let's be off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E62")


    ChrTalk(    #102
        0x101,
        "#1006FYeah, let's.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T3120   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_2214 end

    def Function_16_2E92(): pass

    label("Function_16_2E92")

    OP_24(0xAC, 0x5A)
    Sleep(100)
    OP_24(0xAC, 0x50)
    Sleep(100)
    OP_24(0xAC, 0x46)
    Sleep(100)
    OP_24(0xAC, 0x3C)
    Sleep(100)
    OP_24(0xAC, 0x32)
    Sleep(100)
    OP_24(0xAC, 0x28)
    Sleep(100)
    OP_24(0xAC, 0x1E)
    Sleep(100)
    OP_24(0xAC, 0x14)
    Sleep(100)
    OP_24(0xAC, 0xA)
    Sleep(100)
    OP_23(0xAC)
    Return()

    # Function_16_2E92 end

    SaveToFile()

Try(main)
