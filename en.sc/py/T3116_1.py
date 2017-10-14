from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T3116_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3116_1 ._SN',
            '',
            '',
            '',
            '',
            '',
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
        "Function_1_813",          # 01, 1
        "Function_2_86A",          # 02, 2
        "Function_3_CAC",          # 03, 3
        "Function_4_1B29",         # 04, 4
        "Function_5_1D28",         # 05, 5
        "Function_6_201E",         # 06, 6
        "Function_7_2162",         # 07, 7
        "Function_8_2954",         # 08, 8
        "Function_9_29A7",         # 09, 9
        "Function_10_2A4C",        # 0A, 10
        "Function_11_2AAE",        # 0B, 11
        "Function_12_2B25",        # 0C, 12
        "Function_13_2EBB",        # 0D, 13
        "Function_14_2F10",        # 0E, 14
        "Function_15_2F65",        # 0F, 15
        "Function_16_2FBA",        # 10, 16
        "Function_17_2FD3",        # 11, 17
        "Function_18_30F2",        # 12, 18
        "Function_19_317A",        # 13, 19
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_B9")
    OP_A2(0x3)

    label("loc_B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_147")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Cleared QST034 in previous game\x01",            # 0
            "Did not clear QST034 in previous game\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_13B"),
        (1, "loc_141"),
        (SWITCH_DEFAULT, "loc_147"),
    )


    label("loc_13B")

    OP_A2(0x3)
    Jump("loc_147")

    label("loc_141")

    OP_A3(0x3)
    Jump("loc_147")

    label("loc_147")

    Call(1, 17)

    ChrTalk(    #0
        0x101,
        (
            "#1011FUmm, got a sec?\x02\x03",

            "We're from the guild.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_8C(0xFE, 90, 400)

    ChrTalk(    #1
        0xFE,
        "Oh, you came!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4CE")
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #2
        0xFE,
        "H-Huh...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1000FWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "No, you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Aren't you the person who delivered that\x01",
            "prototype from Ruan a while back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1004FD-Did I?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "Yeah, I'm pretty sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "You came to the weapon shop\x01",
            "with a black-haired boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1015FBlack-haired boy...\x01",
            "That's gotta be Joshua.\x02\x03",

            "Thinking about it, I guess\x01",
            "that might have happened.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3AD")

    ChrTalk(    #10
        0x106,
        (
            "#053FWell, if you're curious, have a look\x01",
            "at your Notebook.\x02\x03",

            "#050FMore importantly, right now we should\x01",
            "talk work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42D")

    label("loc_3AD")


    ChrTalk(    #11
        0x103,
        (
            "#026FWell, if you're curious, have a look\x01",
            "in your Notebook.\x02\x03",

            "#020FMore importantly, I think right now we\x01",
            "should talk work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42D")


    ChrTalk(    #12
        0x101,
        "#1011FAhh, right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "...So then, did you come because\x01",
            "you saw the board?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1006FOf course.\x02\x03",

            "Looks like you're recruiting testers\x01",
            "for an orbal gun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52B")

    label("loc_4CE")


    ChrTalk(    #15
        0x101,
        (
            "#1006FI saw the job board.\x02\x03",

            "Looks like you're recruiting testers\x01",
            "for an orbal gun, huh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52B")


    ChrTalk(    #16
        0xFE,
        "Yeah, actually, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "Actually I was just having problems since\x01",
            "I wasn't getting many respondents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "I know it's kinda sudden, but can I give\x01",
            "you the explanation of the job now?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_708")

    ChrTalk(    #19
        0x101,
        (
            "#1007FI'd love to say yes, but...\x02\x03",

            "Our gun user isn't with us right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Ohhh, then it'd be kinda hard to explain much,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "Please bring him here when you get a chance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1016FYeah, thought so.\x02\x03",

            "All right. We'll be back.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6E, 0x1, 0x8000)
    OP_28(0x6E, 0x1, 0x4000)
    OP_A2(0x4)
    EventEnd(0x0)
    OP_8C(0xFE, 270, 0)
    ClearChrFlags(0xFE, 0x10)
    Return()

    label("loc_708")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75F")
    OP_28(0x6E, 0x4, 0x4)
    Call(1, 3)
    Return()

    label("loc_75F")


    ChrTalk(    #23
        0x101,
        "#1007FSorry, now's not a good time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "Ohhh, too bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1006FYeah, we'll come back when we have\x01",
            "the time. See you then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "Okay. See you later..\x02",
    )

    CloseMessageWindow()
    OP_28(0x6E, 0x1, 0x8000)
    EventEnd(0x0)
    OP_8C(0xFE, 270, 0)
    ClearChrFlags(0xFE, 0x10)
    Return()

    # Function_0_AA end

    def Function_1_813(): pass

    label("Function_1_813")


    ChrTalk(    #27
        0xFE,
        "Anyway, please bring your gun user here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "Otherwise, I can't really explain.\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_1_813 end

    def Function_2_86A(): pass

    label("Function_2_86A")

    EventBegin(0x0)
    Call(1, 17)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_A1D")
    OP_8C(0xFE, 90, 400)

    ChrTalk(    #29
        0xFE,
        "Hey, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "Did you bring your gun user?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_94B")

    ChrTalk(    #31
        0x101,
        "#1006FYep, he's right here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x104,
        "#035FHeh, sorry to keep you waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "Great. Mind if I talk about the test, then?\x02",
    )

    CloseMessageWindow()
    OP_28(0x6E, 0x2, 0x4000)
    Jump("loc_A1A")

    label("loc_94B")


    ChrTalk(    #34
        0x101,
        "#1003FSorry. I don't have him with me right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "Please bring him here when you get a chance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "Otherwise, I can't really explain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1000FGot it. I'll be back later.\x02",
    )

    CloseMessageWindow()
    OP_28(0x6E, 0x1, 0x4000)
    OP_A2(0x4)
    EventEnd(0x0)
    OP_8C(0xFE, 270, 0)
    ClearChrFlags(0xFE, 0x10)
    Return()

    label("loc_A1A")

    Jump("loc_B7F")

    label("loc_A1D")

    OP_8C(0xFE, 90, 400)

    ChrTalk(    #38
        0xFE,
        "Hey, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Can you hear me out about the\x01",
            "orbal gun test now?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7F")

    ChrTalk(    #40
        0x101,
        (
            "#1007FI'd love to say yes, but...\x02\x03",

            "Our gun user isn't with us right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Ohhh, then it'd be kinda hard to explain much,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "Anyway, bring that person here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1016FYeah, thought so.\x02\x03",

            "All right. We'll be back.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6E, 0x1, 0x8000)
    OP_28(0x6E, 0x1, 0x4000)
    OP_A2(0x4)
    EventEnd(0x0)
    OP_8C(0xFE, 270, 0)
    ClearChrFlags(0xFE, 0x10)
    Return()

    label("loc_B7F")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BD6")
    OP_28(0x6E, 0x4, 0x4)
    Call(1, 3)
    Return()

    label("loc_BD6")


    ChrTalk(    #44
        0x101,
        "#1007FSorry. We still need a bit more time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "Aww, come on...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1016FI'm really sorry. We'll come back\x01",
            "when we have time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Yeah, please do. I'll be waiting here.\x01",
            "Forever waiting...\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6E, 0x1, 0x8000)
    EventEnd(0x0)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_2_86A end

    def Function_3_CAC(): pass

    label("Function_3_CAC")


    ChrTalk(    #48
        0x101,
        "#1000FYeah, go ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "Well, then, let me explain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "As you know my request is a test of an orbal gun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "I want you to check the reliability\x01",
            "of this gun through live battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1011FCheck the reliability?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "To put it very simply, I want you to test\x01",
            "its endurance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "All machines have failings you'd\x01",
            "never know unless you used them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "The causes of many problems are usually\x01",
            "things no one even imagined during the\x01",
            "development period.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "I want to pinpoint any hidden weaknesses,\x01",
            "and strengthen the reliability of my gun as\x01",
            "a weapon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "That's the goal of this test.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x104,
        (
            "#030FI believe I understand the intent.\x02\x03",

            "To use a bit more specialized term...\x01",
            "you want a combat demonstration.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(    #59
        0xFE,
        "Yes, exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "Incidentally, are you the shooter\x01",
            "who'll be doing the test?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x104,
        (
            "#031FHeh, it is a singular pleasure to meet you.\x02\x03",

            "I am the roaming poet and musician...\x01",
            "the indomitable hunter of love...\x01",
            "the one and only, Olivier Lenheim.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #62
        0xFE,
        "H-Hunter of...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#1001FJust ignore that.\x02\x03",

            "Sure, he might be a #5Stotal weirdo,#2S\x01",
            " but his skill with a gun is legit.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #64
        0x104,
        (
            "#033FOh, what's that?\x02\x03",

            "Did I detect a slight imbalance of emphasis\x01",
            "on the former part of your speech rather than\x01",
            "the latter...?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11F9")

    ChrTalk(    #65
        0x108,
        (
            "#071FHaha, well, what does it matter?\x02\x03",

            "Everyone acknowledges your skills.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_129B")

    label("loc_11F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_124C")

    ChrTalk(    #66
        0x106,
        (
            "#051FWell, what does it matter?\x02\x03",

            "Everyone acknowledges your skills.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_129B")

    label("loc_124C")


    ChrTalk(    #67
        0x103,
        (
            "#021FWell, now, what does it matter?\x02\x03",

            "Everyone acknowledges your ability.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_129B")


    ChrTalk(    #68
        0xFE,
        "I-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "Well, in that case I guess I'll trust you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0xFE, 400)

    ChrTalk(    #70
        0x104,
        (
            "#031FHahaha. Consider yourself without fear,\x01",
            "my good man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "(W-Will this really be okay...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "Uh, anyway... For now, here's the gun.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #73
        "\x07\x00Received #091i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x5B, 1)
    OP_59()
    OP_0D()
    Fade(500)
    SetChrChipByIndex(0x104, 3)
    SetChrSubChip(0x104, 0)
    OP_0D()
    Call(1, 18)

    ChrTalk(    #74
        0xFE,
        "That's the gun I'd like you to test.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "As thanks for coming, I'll\x01",
            "let you have that gratis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x104,
        (
            "#035FWell that is a most generous gift.\x02\x03",

            "#032FStill, this gun...\x01",
            "It's got a somewhat...unique structure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "Haha, of course it does. I'd be more\x01",
            "upset if you were familiar with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "After all, the drive portion of this\x01",
            "is a new model I developed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "How about it? Think you can handle it?\x02",
    )

    CloseMessageWindow()
    OP_43(0x104, 0x1, 0x1, 0x10)

    ChrTalk(    #80
        0x104,
        (
            "#035FHeh, but of course.\x02\x03",

            "I'm sure that this gun will play\x01",
            "a most beauteous harmony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "Gr-Great to hear...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #82
        0x101,
        (
            "#1007FIf you're done stroking that gun, Olivier,\x01",
            "we'd like to know more about the job.\x02\x03",

            "#1002FWe still haven't heard exactly\x01",
            "what we should be doing.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 0x1)
    Fade(500)
    SetChrChipByIndex(0x104, 65535)
    SetChrSubChip(0x104, 0)
    OP_0D()

    ChrTalk(    #83
        0x104,
        (
            "#033FOhh! Haha! True enough.\x02\x03",

            "Well, please go on.\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 19)

    ChrTalk(    #84
        0xFE,
        "It's more or less as you said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "Basically, I want you to wield this gun in\x01",
            "live combat then come back with the\x01",
            "results.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "I'd like you to test it over on\x01",
            "the Tratt Plains Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "That way, even if trouble comes up,\x01",
            "it shouldn't be too much of an issue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#1006FUnderstood. The Tratt Plains Roads.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "At a minimum I'd like you to fight ten battles.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "Of course, I want you to fight them\x01",
            "to the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "Fleeing over and over wouldn't be much\x01",
            "of a combat test.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x104,
        (
            "#030FLet me check, then...\x02\x03",

            "Go out onto the Tratt Plains Road\x01",
            "equipped with this gun...\x02\x03",

            "Then fight about ten battles to victory there.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1996")

    ChrTalk(    #93
        0x106,
        (
            "#050FThen, once that's settled, come back here\x01",
            "and report.\x02\x03",

            "...That it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19EA")

    label("loc_1996")


    ChrTalk(    #94
        0x103,
        (
            "#020FThen, once that's complete, return here\x01",
            "and report.\x02\x03",

            "...Is that about it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19EA")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #95
        0xFE,
        "Yeah, I think that should do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "If you don't have any more questions,\x01",
            "I'd like you to get to it. Everything clear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#1006FYup. I think we got it.\x02\x03",

            "We'll be back soon.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(    #98
        0xFE,
        "Olivier...I'm trusting you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x104,
        "#031FHeh, worry not. I never disappoint.\x02",
    )

    CloseMessageWindow()
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_28(0x6E, 0x4, 0x8)
    OP_28(0x6E, 0x1, 0x1)
    OP_28(0x6E, 0x1, 0x2)
    OP_A2(0x5)
    ClearChrFlags(0xFE, 0x10)
    EventEnd(0x0)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_3_CAC end

    def Function_4_1B29(): pass

    label("Function_4_1B29")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Report\x01",                      # 0
            "Check Job Requirements\x01",      # 1
            "Leave\x01",                       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B96")
    Call(1, 5)
    Return()

    label("loc_1B96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CFD")

    ChrTalk(    #100
        0xFE,
        (
            "What I want you to test is my new\x01",
            "0-Type Orbal Gun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "I want you to go fight at least ten\x01",
            "battles with that gun equipped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "I'd like you to do the testing over\x01",
            "on the Tratt Plains Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "It's fairly safe, after all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "Once you've completed the required number\x01",
            "of battles, come back here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "That's about it for my request.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D27")

    label("loc_1CFD")


    ChrTalk(    #106
        0xFE,
        "Well, then, good luck with the test.\x02",
    )

    CloseMessageWindow()

    label("loc_1D27")

    Return()

    # Function_4_1B29 end

    def Function_5_1D28(): pass

    label("Function_5_1D28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DAD")

    ChrTalk(    #107
        0xFE,
        "Huh, where's Olivier?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "Not much of a report without the gunner.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        "Sorry, but come back again later.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Return()

    label("loc_1DAD")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1E3B")

    ChrTalk(    #110
        0xFE,
        "Oh, did you come to report?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#1000FNo... We're just about to go and\x01",
            "do the testing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "Oh, I see. Well, good luck.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Return()

    label("loc_1E3B")

    EventBegin(0x0)
    Call(1, 17)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #113
        0xFE,
        "Hey, come to report?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        "#1000FYeah, we fought the battles.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x104,
        (
            "#030FWell, then, allow us to report\x01",
            "the results to date.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x5B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FAE")

    ChrTalk(    #116
        0xFE,
        "Sure, I don't mind, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "You don't seem to have the important part,\x01",
            "the 0-Type Orbal Gun α.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "Without that, I can't check the results\x01",
            "of the test.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "Sorry, but can you get it and come back.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)
    EventEnd(0x0)
    Return()

    label("loc_1FAE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #120
        "\x07\x05Olivier reported the current results of the test to Karl.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2018")
    Call(1, 6)
    Return()

    label("loc_2018")

    Call(1, 7)
    Return()

    # Function_5_1D28 end

    def Function_6_201E(): pass

    label("Function_6_201E")


    ChrTalk(    #121
        0xFE,
        (
            "Hmm, I see. Seems like you've done\x01",
            "a lot, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "Unfortunately it doesn't look like you've\x01",
            "fought enough battles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        "#1008FAh, I thought it might be. Not enough, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "Yeah, I'd appreciate it if you'd fight a bit more.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "Well, then, come back and report later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x104,
        "#030FHeh, we shall return, then.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    EventEnd(0x0)
    Return()

    # Function_6_201E end

    def Function_7_2162(): pass

    label("Function_7_2162")

    TurnDirection(0xFE, 0x104, 400)
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_21FD")

    ChrTalk(    #127
        0xFE,
        "Yeah, seems like you've fought enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "Man, it looks like you worked pretty hard,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        "#1001FAhaha, thanks.\x02",
    )

    CloseMessageWindow()
    OP_2B(0x6E, 0x1)
    OP_2C(0x6E, 0x3E8)
    Jump("loc_22C8")

    label("loc_21FD")


    ChrTalk(    #130
        0xFE,
        "Yeah, seems like you've fought enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "All right, we'll call that test complete.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1007FPhew! Finally over.\x02\x03",

            "That was rougher than I expected.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #133
        0xFE,
        "Haha, seems like you worked hard.\x02",
    )

    CloseMessageWindow()

    label("loc_22C8")


    ChrTalk(    #134
        0x104,
        (
            "#035FHeh, as but a humble assistant, it was\x01",
            "the least I could do.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(    #135
        0xFE,
        "So, Olivier. Were there any problems?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x104,
        (
            "#035FNo, absolutely no problems.\x02\x03",

            "Stable trajectory and a perfectly centered\x01",
            "balance...\x02\x03",

            "#030FI'm eager to see a fine piece of work\x01",
            "like this out on the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "*pheeew* Thank goodness. You have no\x01",
            "idea how relieved I am to hear that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "All right, seems like I can finally see the\x01",
            "production phase on the horizon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1000FOh? It's not gonna be mass produced yet?\x02\x03",

            "It looks like it's pretty done from\x01",
            "my point of view...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #140
        0xFE,
        "No, it still needs a bit more time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "Now I need to hone in on the fine\x01",
            "details for the manufacturing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "And I'm able to do that because of\x01",
            "the results you got me from this test.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "This new info should make further research\x01",
            "fly ahead.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2626")

    ChrTalk(    #144
        0x106,
        "#051FWell, keep up the good work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2647")

    label("loc_2626")


    ChrTalk(    #145
        0x103,
        "#020FKeep up the good work.\x02",
    )

    CloseMessageWindow()

    label("loc_2647")


    ChrTalk(    #146
        0x104,
        (
            "#031FA new model orbal gun...\x01",
            "I'll be expecting great things.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(    #147
        0xFE,
        "Yeah, look forward to it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "Oh, right... One sec before you go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        "#1011FHuh, was there something else?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #150
        0xFE,
        "Yeah, take this with you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #151
        "\x07\x00Got  #620i quartz.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x26C, 1)
    Sleep(500)

    ChrTalk(    #152
        0xFE,
        (
            "It was bothering me a bit that\x01",
            "the reward was kinda meager.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "Well, think of this as making up for that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "It's not a bad thing to have a bit of,\x01",
            "so please take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x101,
        "#1001FAh, yeah, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x104,
        "#031FHeh, we'll be glad to use it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "Well, then, if anything else comes up,\x01",
            "I'll call you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "You all take care.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        "#1018FSee you later!\x02",
    )

    CloseMessageWindow()
    OP_28(0x6E, 0x4, 0x10)
    OP_28(0x6E, 0x1, 0x80)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #160
        "Quest #2C[New Model Orbal Gun Test] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x8)
    EventEnd(0x0)
    Return()

    # Function_7_2162 end

    def Function_8_2954(): pass

    label("Function_8_2954")


    ChrTalk(    #161
        0xFE,
        "Well, then, I'm counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        "Especially you, Olivier! Do your best!\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_8_2954 end

    def Function_9_29A7(): pass

    label("Function_9_29A7")


    ChrTalk(    #163
        0xFE,
        "Everyone, thank you for today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "I'll do my best and make a great\x01",
            "orbal gun with this data.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "Well, then, if anything else comes up,\x01",
            "I'll call you guys.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_9_29A7 end

    def Function_10_2A4C(): pass

    label("Function_10_2A4C")


    ChrTalk(    #166
        0xFE,
        (
            "If the gunner isn't here, it won't\x01",
            "be much of a report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        "Sorry, but come back with him.\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_10_2A4C end

    def Function_11_2AAE(): pass

    label("Function_11_2AAE")


    ChrTalk(    #168
        0xFE,
        (
            "Unfortunately it doesn't look like you've\x01",
            "fought enough battles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        "Fight a bit more then come back to report.\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_11_2AAE end

    def Function_12_2B25(): pass

    label("Function_12_2B25")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x382), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B32")
    Return()

    label("loc_2B32")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0xE4E5A8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BC6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x154), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3BCE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BC6")
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C45")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10FE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x866), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C45")
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C45")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CC4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11F8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3C3C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CC4")
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CC4")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    LoadEffect(0x0, "map\\\\mp108_00.eff")
    PlayEffect(0x0, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xF4240), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DC4")
    EventBegin(0x1)
    OP_62(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_END)),
        (1, "loc_2DAA"),
        (2, "loc_2DB1"),
        (3, "loc_2DB8"),
        (SWITCH_DEFAULT, "loc_2DBF"),
    )


    label("loc_2DAA")

    OP_65(0x0, 0x1)
    Jump("loc_2DBF")

    label("loc_2DB1")

    OP_65(0x1, 0x1)
    Jump("loc_2DBF")

    label("loc_2DB8")

    OP_65(0x2, 0x1)
    Jump("loc_2DBF")

    label("loc_2DBF")

    EventEnd(0x1)
    Jump("loc_2EB4")

    label("loc_2DC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x4C4B40), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_2E1B")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #170
        "\x07\x05Response very nearby!\x02",
    )

    OP_22(0xAA, 0x0, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_2EB4")

    label("loc_2E1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x989680), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_2E76")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #171
        "\x07\x05Response in the vicinity.\x02",
    )

    OP_22(0xAA, 0x0, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_2EB4")

    label("loc_2E76")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #172
        "\x07\x05No response.\x02",
    )

    OP_22(0xAB, 0x0, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_2EB4")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_12_2B25 end

    def Function_13_2EBB(): pass

    label("Function_13_2EBB")

    EventBegin(0x1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #173
        "\x07\x00Received #563i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x233, 1)
    OP_28(0x6F, 0x1, 0x8)
    OP_64(0x0, 0x1)
    EventEnd(0x1)
    Return()

    # Function_13_2EBB end

    def Function_14_2F10(): pass

    label("Function_14_2F10")

    EventBegin(0x1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #174
        "\x07\x00Received #563i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x233, 1)
    OP_28(0x6F, 0x1, 0x10)
    OP_64(0x1, 0x1)
    EventEnd(0x1)
    Return()

    # Function_14_2F10 end

    def Function_15_2F65(): pass

    label("Function_15_2F65")

    EventBegin(0x1)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #175
        "\x07\x00Received #563i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x233, 1)
    OP_28(0x6F, 0x1, 0x20)
    OP_64(0x2, 0x1)
    EventEnd(0x1)
    Return()

    # Function_15_2F65 end

    def Function_16_2FBA(): pass

    label("Function_16_2FBA")

    SetChrChipByIndex(0x104, 3)
    OP_99(0x104, 0x0, 0xE, 0x7D0)
    WaitChrThread(0x104, 0x0)
    SetChrSubChip(0x104, 14)
    Return()

    # Function_16_2FBA end

    def Function_17_2FD3(): pass

    label("Function_17_2FD3")

    Fade(1000)
    SetChrPos(0x8, -2000, 0, 3410, 270)
    SetChrPos(0x101, -420, 0, 3410, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_303D")
    SetChrPos(0xF7, -490, 0, 5020, 245)
    SetChrPos(0xF8, 590, 0, 2940, 266)
    SetChrPos(0xF9, 950, 0, 4870, 240)
    Jump("loc_30B3")

    label("loc_303D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3080")
    SetChrPos(0xF8, -490, 0, 5020, 245)
    SetChrPos(0xF7, 590, 0, 2940, 266)
    SetChrPos(0xF9, 950, 0, 4870, 240)
    Jump("loc_30B3")

    label("loc_3080")

    SetChrPos(0xF9, -490, 0, 5020, 245)
    SetChrPos(0xF7, 590, 0, 2940, 266)
    SetChrPos(0xF8, 950, 0, 4870, 240)

    label("loc_30B3")

    OP_6D(-790, 0, 3710, 0)
    OP_67(0, 4800, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(57000, 0)
    OP_6E(280, 0)
    OP_0D()
    Return()

    # Function_17_2FD3 end

    def Function_18_30F2(): pass

    label("Function_18_30F2")


    def lambda_30F8():
        TurnDirection(0x101, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30F8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_312C")

    def lambda_3113():
        OP_8C(0xF8, 315, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3113)

    def lambda_3121():
        TurnDirection(0xF9, 0x104, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3121)
    Jump("loc_3174")

    label("loc_312C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3158")

    def lambda_313F():
        OP_8C(0xF7, 315, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_313F)

    def lambda_314D():
        TurnDirection(0xF9, 0x104, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_314D)
    Jump("loc_3174")

    label("loc_3158")


    def lambda_315E():
        OP_8C(0xF7, 315, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_315E)

    def lambda_316C():
        TurnDirection(0xF8, 0x104, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_316C)

    label("loc_3174")

    WaitChrThread(0x101, 0x1)
    Return()

    # Function_18_30F2 end

    def Function_19_317A(): pass

    label("Function_19_317A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31B4")

    def lambda_318D():
        OP_8C(0xF7, 245, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_318D)

    def lambda_319B():
        OP_8C(0xF8, 266, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_319B)

    def lambda_31A9():
        OP_8C(0xF9, 240, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_31A9)
    Jump("loc_3218")

    label("loc_31B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31EE")

    def lambda_31C7():
        OP_8C(0xF8, 245, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_31C7)

    def lambda_31D5():
        OP_8C(0xF7, 266, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_31D5)

    def lambda_31E3():
        OP_8C(0xF9, 240, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_31E3)
    Jump("loc_3218")

    label("loc_31EE")


    def lambda_31F4():
        OP_8C(0xF9, 245, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_31F4)

    def lambda_3202():
        OP_8C(0xF7, 266, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3202)

    def lambda_3210():
        OP_8C(0xF8, 240, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3210)

    label("loc_3218")

    Return()

    # Function_19_317A end

    SaveToFile()

Try(main)
