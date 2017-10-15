from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3131   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
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
        'Ben',                                  # 9
        'Ursus',                                # 10
        'Randall',                              # 11
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


    AddCharChip(
        'ED6_DT07/CH01020 ._CH',             # 00
        'ED6_DT07/CH01270 ._CH',             # 01
        'ED6_DT07/CH01003 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01020P._CP',             # 00
        'ED6_DT07/CH01270P._CP',             # 01
        'ED6_DT07/CH01003P._CP',             # 02
    )

    DeclNpc(
        X                   = -2470,
        Z                   = -1000,
        Y                   = 4710,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 5480,
        Z                   = -1000,
        Y                   = 5320,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -450,
        Z                   = -650,
        Y                   = 2280,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x135,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    DeclActor(
        TriggerX            = -530,
        TriggerZ            = -1000,
        TriggerY            = 4660,
        TriggerRange        = 400,
        ActorX              = -2470,
        ActorZ              = 500,
        ActorY              = 4710,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_146",          # 00, 0
        "Function_1_174",          # 01, 1
        "Function_2_1A9",          # 02, 2
        "Function_3_1CD",          # 03, 3
        "Function_4_1D2",          # 04, 4
        "Function_5_FBC",          # 05, 5
        "Function_6_17F7",         # 06, 6
    )


    def Function_0_146(): pass

    label("Function_0_146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_150")
    Jump("loc_173")

    label("loc_150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_15A")
    Jump("loc_173")

    label("loc_15A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_164")
    Jump("loc_173")

    label("loc_164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_16E")
    Jump("loc_173")

    label("loc_16E")

    SetChrFlags(0xA, 0x80)

    label("loc_173")

    Return()

    # Function_0_146 end

    def Function_1_174(): pass

    label("Function_1_174")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A8")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)

    label("loc_1A8")

    Return()

    # Function_1_174 end

    def Function_2_1A9(): pass

    label("Function_2_1A9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CC")
    OP_8D(0xFE, 400, 5540, 5960, 4780, 2000)
    Jump("Function_2_1A9")

    label("loc_1CC")

    Return()

    # Function_2_1A9 end

    def Function_3_1CD(): pass

    label("Function_3_1CD")

    Call(0, 4)
    Return()

    # Function_3_1CD end

    def Function_4_1D2(): pass

    label("Function_4_1D2")

    TalkBegin(0x8)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EF")
    OP_A9(0x9B)
    TalkEnd(0x8)
    Return()

    label("loc_1EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_200")
    TalkEnd(0x8)
    Return()

    label("loc_200")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_20D")
    OP_A2(0x0)

    label("loc_20D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A2")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Cleared 'Order for New Ingredients'\x01",           # 0
            "Didn't clear 'Order for New Ingredients'\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_296"),
        (1, "loc_29C"),
        (SWITCH_DEFAULT, "loc_2A2"),
    )


    label("loc_296")

    OP_A2(0x0)
    Jump("loc_2A2")

    label("loc_29C")

    OP_A3(0x0)
    Jump("loc_2A2")

    label("loc_2A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_401")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37D")

    ChrTalk(    #0
        0x8,
        "Did you guys see that floating object too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "According to the rumors, there's something\x01",
            "like a city on top of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "Seriously, it's like something out of\x01",
            "a fairytale!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_3FE")

    label("loc_37D")


    ChrTalk(    #3
        0x8,
        (
            "Apparently there's something like a city\x01",
            "atop that floating object.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "Seriously, it's like something out of\x01",
            "a fairytale!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FE")

    Jump("loc_A2D")

    label("loc_401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_591")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FF")

    ChrTalk(    #5
        0x8,
        (
            "The air conditioning's stopped, but\x01",
            "for now it's not affecting business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "We've always cooked over an open flame,\x01",
            "after all, so we're used to the heat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "Even with orbments not working,\x01",
            "it's not really affecting us much.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_58E")

    label("loc_4FF")


    ChrTalk(    #8
        0x8,
        (
            "For now there's no effect on business\x01",
            "at all, in fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "We've always cooked over an open flame,\x01",
            "after all, so we're used to the heat!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58E")

    Jump("loc_A2D")

    label("loc_591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_6E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_62F")

    ChrTalk(    #10
        0x8,
        (
            "It's good news that there'll be no\x01",
            "more earthquakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "I never doubt good news. Better just to\x01",
            "accept it and be merry, I always say!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DE")

    label("loc_62F")

    TurnDirection(0x8, 0xA, 0)

    ChrTalk(    #12
        0x8,
        (
            "Well, one way or another, it's good news\x01",
            "that the earthquakes are finally over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "Think too much and all you're gonna\x01",
            "do is lose more hair! That's my motto.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_6DE")

    Jump("loc_A2D")

    label("loc_6E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_81E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_780")

    ChrTalk(    #14
        0x8,
        (
            "Apparently that non-aggression\x01",
            "pact will be signed soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "I'd love it if I had more Republican guests\x01",
            "as a result of that agreement.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81B")

    label("loc_780")


    ChrTalk(    #16
        0x8,
        (
            "Oh, yeah, apparently that non-aggression\x01",
            "pact will be signed soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "I'd love it if I had more Republican guests\x01",
            "as a result of that agreement.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_81B")

    Jump("loc_A2D")

    label("loc_81E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_948")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_89C")

    ChrTalk(    #18
        0x8,
        (
            "So old man Randall's granddaughter's\x01",
            "old enough to be off at work, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "Time just keeps on movin'.\x02",
    )

    CloseMessageWindow()
    Jump("loc_945")

    label("loc_89C")


    ChrTalk(    #20
        0x8,
        (
            "So old man Randall's granddaughter's\x01",
            "old enough to be off at work, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "Aww, who am I to talk.\x01",
            "Looks like I've gotten old too!\x01",
            "Wonder when that happened...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_945")

    Jump("loc_A2D")

    label("loc_948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_A2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9B3")

    ChrTalk(    #22
        0x8,
        "Gotta say, an earthquake's pretty rare.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        "Hopefully there wasn't too much damage.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A2D")

    label("loc_9B3")


    ChrTalk(    #24
        0x8,
        "Hey, good work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "We've got a great menu for dealing\x01",
            "with exhaustion, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        "You should give it a try!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_A2D")

    Jump("loc_AF2")

    label("loc_A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_AA8")

    ChrTalk(    #27
        0x8,
        (
            "Right now things are rough, but we've\x01",
            "gotta get through 'em.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        "Let's both work hard and stay healthy!\x02",
    )

    CloseMessageWindow()
    Jump("loc_AF2")

    label("loc_AA8")


    ChrTalk(    #29
        0x8,
        "If you get hungry, come by any time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        "And keep up the good work.\x02",
    )

    CloseMessageWindow()

    label("loc_AF2")

    Jump("loc_FB8")

    label("loc_AF5")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 0)
    OP_63(0x8)

    ChrTalk(    #31
        0x8,
        "Oh, hey, aren't you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "Yeah, you're the bracers who brought\x01",
            "me that Acerbic Tomato!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#1011FAh, you remember us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        "Heh, you bet I do. I owe you a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "My 'bitter tomato cooking' is pretty\x01",
            "popular now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1004F...Seriously?!\x02\x03",

            "#1016FY-You're kidding, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CDF")
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #37
        0x107,
        (
            "#064FNo, it's true!\x02\x03",

            "Apparently the people at the central factory\x01",
            "eat it a bunch.\x02\x03",

            "#561FEveryone picks nutrition over flavor around\x01",
            "these parts.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)
    Jump("loc_DB0")

    label("loc_CDF")


    ChrTalk(    #38
        0x8,
        (
            "Hahaha. No kidding, right?\x01",
            "Those researchers can't get enough of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "It's got a rep for being the best cure for a\x01",
            "little fatigue. You can imagine why scientists\x01",
            "would be all over that kind of thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DB0")

    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #40
        0x101,
        (
            "#1007FHmmm, I dunno. I still struggle to understand\x01",
            "how the benefits would outweigh a flavor like\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "Hey, since you're here, give my new recipe\x01",
            "a try! What do you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        "It's my treat, of course.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EBE")

    def lambda_EB6():
        TurnDirection(0x107, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_EB6)

    label("loc_EBE")

    TurnDirection(0x101, 0x8, 400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #43
        "\x07\x00Received #409i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_3E(0x199, 1)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #44
        0x8,
        (
            "Eat some of my super nutritious cookin'\x01",
            "and keep up the good work, and you'll\x01",
            "go far. I guarantee it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "Catch y'all later.\x01",
            "Looking forward to your business!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_A2(0x1426)

    label("loc_FB8")

    TalkEnd(0x8)
    Return()

    # Function_4_1D2 end

    def Function_5_FBC(): pass

    label("Function_5_FBC")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_11BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1104")

    ChrTalk(    #46
        0xFE,
        (
            "Seems like the central factory's got things\x01",
            "pretty rough in the research department right\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Louise's been heading out there\x01",
            "really early these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "I'm keeping an eye on her little\x01",
            "sister while she's away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "...Really, the Orbal Shutdown Phenomenon's\x01",
            "had a huge effect on everyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_11BA")

    label("loc_1104")


    ChrTalk(    #50
        0xFE,
        (
            "I'm taking care of her little sister\x01",
            "because of it, ultimately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Really is amazing how much one event\x01",
            "can impact your life...even in ways\x01",
            "you wouldn't normally think about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11BA")

    Jump("loc_17F3")

    label("loc_11BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_12E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1276")

    ChrTalk(    #52
        0xFE,
        (
            "You know, we don't even have any orbal\x01",
            "cooking equipment here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "That's why it's business as usual!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "I'll admit, I kinda hoped\x01",
            "I'd get some time off...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_12E2")

    label("loc_1276")


    ChrTalk(    #55
        0xFE,
        (
            "You know, we don't even have any orbal\x01",
            "cooking equipment here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "That's why it's business as usual!\x02",
    )

    CloseMessageWindow()

    label("loc_12E2")

    Jump("loc_17F3")

    label("loc_12E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_13E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_136A")

    ChrTalk(    #57
        0xFE,
        (
            "Yuriel's always watching over the house\x01",
            "by herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "I can see why she'd complain about it,\x01",
            "given her age.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E6")

    label("loc_136A")


    ChrTalk(    #59
        0xFE,
        (
            "Ohh, once it's break time, I need\x01",
            "to get over to Louise's house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "Poor Yuriel must be starving all alone there!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_13E6")

    Jump("loc_17F3")

    label("loc_13E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1595")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1469")

    ChrTalk(    #61
        0xFE,
        (
            "Who takes care of her little sister\x01",
            "Yuriel when she's away on business?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "That would be me, I suppose.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1592")

    label("loc_1469")


    ChrTalk(    #63
        0xFE,
        (
            "Oh, yeah, Louise said she had\x01",
            "to go away on a business trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Apparently they're gonna change out\x01",
            "an airship's engine at Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "But wait. Thinking about it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Who's going to take care of her little\x01",
            "sister Yuriel while she's away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "That would be me, I guess...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1592")

    Jump("loc_17F3")

    label("loc_1595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_16A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_162F")

    ChrTalk(    #68
        0xFE,
        "Our boss just piles up huge towers of plates.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "If he leaves them like that, they're gonna\x01",
            "be dust next time an earthquake hits.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A3")

    label("loc_162F")


    ChrTalk(    #70
        0xFE,
        (
            "Phew! Got to everything in time.\x01",
            "All the dishware is safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "And it's all thanks to keeping it in order!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_16A3")

    Jump("loc_17F3")

    label("loc_16A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_17F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_173A")

    ChrTalk(    #72
        0xFE,
        (
            "My girlfriend works as a researcher\x01",
            "at the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "I hope there wasn't any damage\x01",
            "there from that earthquake...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F3")

    label("loc_173A")


    ChrTalk(    #74
        0xFE,
        (
            "Yikes. That shook more than I expected.\x01",
            "Pretty scary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "Oh, yeah, Louise said she'd be\x01",
            "going into work today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "I hope there wasn't any damage\x01",
            "at the central factory...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_17F3")

    TalkEnd(0x9)
    Return()

    # Function_5_FBC end

    def Function_6_17F7(): pass

    label("Function_6_17F7")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1993")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F1")

    ChrTalk(    #77
        0xFE,
        (
            "Seems the factory folk are interested\x01",
            "in that floating object.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "Hoho. Investigating unknown phenomena\x01",
            "is a favorite activity of researchers,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "Though I shouldn't joke. Things are\x01",
            "very serious right now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1990")

    label("loc_18F1")


    ChrTalk(    #80
        0xFE,
        (
            "The factory folk are extremely interested\x01",
            "in that floating object.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "And to be honest, right now probably isn't\x01",
            "the time to be worried about research.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1990")

    Jump("loc_2181")

    label("loc_1993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1B48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA6")

    ChrTalk(    #82
        0xFE,
        (
            "I know that the owner here actually\x01",
            "did want an orbal oven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "When the shop first opened, though, he was\x01",
            "so poor he had to give up on that dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "But, thanks to that, he's open now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "Really, you never know what'll turn out\x01",
            "for the best!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1B45")

    label("loc_1AA6")


    ChrTalk(    #86
        0xFE,
        (
            "The owner here was very poor when he opened\x01",
            "the shop. He couldn't buy an orbal oven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "Still, thanks to that, he's able to stay\x01",
            "open for business now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B45")

    Jump("loc_2181")

    label("loc_1B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1D1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1C42")

    ChrTalk(    #88
        0xFE,
        (
            "I'm sure ol' Russell is involved in this somehow.\x01",
            "Heck, he probably even started it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "Then an earthquake happened, and\x01",
            "his research got interrupted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "Hmm... A very believable sequence of events,\x01",
            "come to think of it...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D18")

    label("loc_1C42")


    ChrTalk(    #91
        0xFE,
        (
            "Apparently a safety announcement went out,\x01",
            "but it all sounds fishy to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "How can they say so clearly that no more\x01",
            "earthquakes will happen, hmm? It's hogwash!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "Veeeery suspicious, if you ask me...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1D18")

    Jump("loc_2181")

    label("loc_1D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1F40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1DE8")

    ChrTalk(    #94
        0xFE,
        (
            "Our connection with foreign countries will\x01",
            "be extremely critical, moving forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "The queen has tremendous foresight, given\x01",
            "how much she's worked on reconciliatory\x01",
            "negotiations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F3D")

    label("loc_1DE8")


    ChrTalk(    #96
        0xFE,
        (
            "Still, as always, orbment sales are\x01",
            "doing very well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "Just as our national sales had started\x01",
            "dropping, foreign exports came to be\x01",
            "expanding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "Our connection with foreign countries will\x01",
            "be extremely critical, moving forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "The queen has tremendous foresight, given\x01",
            "how much she's worked on reconciliatory\x01",
            "negotiations.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1F3D")

    Jump("loc_2181")

    label("loc_1F40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2048")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1FC9")

    ChrTalk(    #100
        0xFE,
        (
            "Well, my granddaughter isn't the type\x01",
            "to worry about the little things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "She's tough. I'm sure she'll survive.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2045")

    label("loc_1FC9")


    ChrTalk(    #102
        0xFE,
        (
            "My granddaughter's off working at the\x01",
            "central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "I can't help but worry whether\x01",
            "she's doing okay or not.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2045")

    Jump("loc_2181")

    label("loc_2048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_2181")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_20C7")

    ChrTalk(    #104
        0xFE,
        (
            "Lately my granddaughter's been going\x01",
            "to the central factory a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "I admit, it's kind of worrisome.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2181")

    label("loc_20C7")


    ChrTalk(    #106
        0xFE,
        (
            "Well, I'm sure the central factory's\x01",
            "fine with a little shake like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "The only real damage I imagine is people\x01",
            "using the earthquake as an excuse to skip\x01",
            "out early. Hmph.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2181")

    TalkEnd(0xA)
    Return()

    # Function_6_17F7 end

    SaveToFile()

Try(main)
