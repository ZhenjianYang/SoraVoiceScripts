from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4406   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4406.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        ' ',                                    # 9
        ' ',                                    # 10
        ' ',                                    # 11
        ' ',                                    # 12
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 3500,
        Y                   = -1000,
        Z                   = -6930,
        Range               = 7780,
        Unknown_10          = 0x1388,
        Unknown_14          = 0x177A,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    DeclActor(
        TriggerX            = -19450,
        TriggerZ            = 0,
        TriggerY            = -15500,
        TriggerRange        = 1000,
        ActorX              = -20540,
        ActorZ              = -500,
        ActorY              = -17840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -20540,
        TriggerZ            = -700,
        TriggerY            = -17840,
        TriggerRange        = 1000,
        ActorX              = -19600,
        ActorZ              = 500,
        ActorY              = -14960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -23370,
        TriggerZ            = -560,
        TriggerY            = -22430,
        TriggerRange        = 1000,
        ActorX              = -23370,
        ActorZ              = 200,
        ActorY              = -22430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1B6",          # 00, 0
        "Function_1_1B7",          # 01, 1
        "Function_2_200",          # 02, 2
        "Function_3_8FF",          # 03, 3
        "Function_4_92C",          # 04, 4
        "Function_5_959",          # 05, 5
        "Function_6_986",          # 06, 6
        "Function_7_9B3",          # 07, 7
        "Function_8_A87",          # 08, 8
        "Function_9_FE3",          # 09, 9
        "Function_10_10C7",        # 0A, 10
        "Function_11_111F",        # 0B, 11
        "Function_12_1169",        # 0C, 12
        "Function_13_11A5",        # 0D, 13
        "Function_14_11D3",        # 0E, 14
        "Function_15_12B7",        # 0F, 15
        "Function_16_130F",        # 10, 16
        "Function_17_1359",        # 11, 17
        "Function_18_1395",        # 12, 18
    )


    def Function_0_1B6(): pass

    label("Function_0_1B6")

    Return()

    # Function_0_1B6 end

    def Function_1_1B7(): pass

    label("Function_1_1B7")

    OP_16(0x2, 0xFA0, 0xFFFE3AE0, 0xFFFE69C0, 0x23006D)
    OP_22(0x1C5, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 1)), scpexpr(EXPR_END)), "loc_1E1")
    OP_B1("U4406_y")
    Jump("loc_1EA")

    label("loc_1E1")

    OP_B1("U4406_n")

    label("loc_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB")
    OP_72(0x1002, 0x0)
    ExitThread()
    Jump("loc_1FF")

    label("loc_1FB")

    OP_64(0x2, 0x1)

    label("loc_1FF")

    Return()

    # Function_1_1B7 end

    def Function_2_200(): pass

    label("Function_2_200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 1)), scpexpr(EXPR_END)), "loc_208")
    Return()

    label("loc_208")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24F")
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x109, 225, 400)

    ChrTalk(    #0
        0x109,
        "#1079FWha...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_353")

    label("loc_24F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_292")
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10F, 225, 400)

    ChrTalk(    #1
        0x10F,
        "#1444FWhat?\x02",
    )

    CloseMessageWindow()
    Jump("loc_353")

    label("loc_292")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D3")
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x107, 225, 400)

    ChrTalk(    #2
        0x107,
        "#065FHuh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_353")

    label("loc_2D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_315")
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10E, 225, 400)

    ChrTalk(    #3
        0x10E,
        "#173FWhat?\x02",
    )

    CloseMessageWindow()
    Jump("loc_353")

    label("loc_315")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_353")
    OP_62(0x10D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x109, 225, 400)

    ChrTalk(    #4
        0x10D,
        "#273FHmm?\x02",
    )

    CloseMessageWindow()

    label("loc_353")

    Sleep(300)

    def lambda_35E():
        OP_6D(-22380, 290, -22070, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_35E)

    def lambda_376():
        OP_67(0, 7900, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_376)

    def lambda_38E():
        OP_6B(3070, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_38E)

    def lambda_39E():
        OP_6C(224000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_39E)

    def lambda_3AE():
        OP_6E(420, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_3AE)
    WaitChrThread(0x109, 0x1)
    SetChrPos(0x10F, 910, 0, -55320, 0)
    SetChrPos(0xF0, -910, 0, -55370, 0)
    SetChrPos(0xF1, -20, 0, -56270, 0)
    OP_43(0x109, 0x0, 0x0, 0x3)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    OP_43(0xF0, 0x0, 0x0, 0x5)
    OP_43(0xF1, 0x0, 0x0, 0x6)
    Sleep(1000)

    def lambda_417():
        OP_6D(-21370, 0, -16740, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_417)

    def lambda_42F():
        OP_67(0, 5800, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_42F)

    def lambda_447():
        OP_6B(3070, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_447)

    def lambda_457():
        OP_6C(224000, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_457)

    def lambda_467():
        OP_6E(355, 3000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_467)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C6")

    ChrTalk(    #5
        0x107,
        "#065F#6PWhat's the Bobcat doing here?\x02",
    )

    CloseMessageWindow()
    Jump("loc_510")

    label("loc_4C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_510")

    ChrTalk(    #6
        0x10D,
        "#270F#6PWhat is the Bobcat doing in a place like this?\x02",
    )

    CloseMessageWindow()

    label("loc_510")


    ChrTalk(    #7
        0x10F,
        "#1443F#6PYou recognize this ship?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x109,
        (
            "#1065F#5PIt's owned by the sky bandits who managed\x01",
            "to make their way onto that flying city just\x01",
            "like us.\x02\x03",

            "#1063FI hear they've put a stop to the whole bandit\x01",
            "business now, though.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D6")

    ChrTalk(    #9
        0x10E,
        (
            "#176F#6PAfter all the trouble on the Liber Ark, \x01",
            "Her Majesty extended all of them a royal\x01",
            "pardon for their actions.\x02\x03",

            "#175FI hear they are currently using their airship\x01",
            "to operate a courier business, in fact.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D0")

    label("loc_6D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7D0")

    ChrTalk(    #10
        0x10D,
        (
            "#272F#6PI believe they were granted a royal pardon by\x01",
            "Queen Alicia after the situation in Liberl calmed\x01",
            "down.\x02\x03",

            "Since then, I've heard they have been operating\x01",
            "a courier service using the Bobcat, but I can't be\x01",
            "sure if that's true.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D0")


    ChrTalk(    #11
        0x109,
        "#1840F#5PHuh. That's cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10F,
        (
            "#1446F#6PI see.\x02\x03",

            "#1802FStill, why would it be here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x109,
        (
            "#1067F#5PWell, it's not impossible that they came\x01",
            "to Grancel to deliver some sort of letter\x01",
            "or parcel...\x02\x03",

            "#1060F...but the best way to find that answer is\x01",
            "to look inside and see what we find.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2709)
    OP_28(0x2C, 0x1, 0x4)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_200 end

    def Function_3_8FF(): pass

    label("Function_3_8FF")

    SetChrPos(0xFE, -12370, 0, -6360, 219)
    OP_8E(0xFE, 0xFFFFB5C8, 0x0, 0xFFFFCB9E, 0x1388, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_3_8FF end

    def Function_4_92C(): pass

    label("Function_4_92C")

    SetChrPos(0xFE, -12390, 0, -4230, 215)
    OP_8E(0xFE, 0xFFFFB0C8, 0x0, 0xFFFFCCC0, 0x1388, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_4_92C end

    def Function_5_959(): pass

    label("Function_5_959")

    SetChrPos(0xFE, -10060, 0, -4480, 222)
    OP_8E(0xFE, 0xFFFFB866, 0x0, 0xFFFFD210, 0x1388, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_5_959 end

    def Function_6_986(): pass

    label("Function_6_986")

    SetChrPos(0xFE, -10090, 0, -2450, 227)
    OP_8E(0xFE, 0xFFFFB24E, 0x0, 0xFFFFD2CE, 0x1388, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_6_986 end

    def Function_7_9B3(): pass

    label("Function_7_9B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 4)), scpexpr(EXPR_END)), "loc_A24")
    TalkBegin(0xFF)
    Sleep(300)
    OP_22(0x73, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05The door was unlocked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x270D)
    OP_64(0x2, 0x1)
    OP_71(0x1002, 0x0)
    ExitThread()
    TalkEnd(0xFF)
    Jump("loc_A86")

    label("loc_A24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A33")
    Call(0, 8)
    Jump("loc_A86")

    label("loc_A33")

    TalkBegin(0xFF)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_A86")

    Return()

    # Function_7_9B3 end

    def Function_8_A87(): pass

    label("Function_8_A87")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x109, -23040, -610, -21760, 180)
    SetChrPos(0x10F, -21410, -170, -21530, 270)
    SetChrPos(0xF0, -20040, -240, -20880, 270)
    SetChrPos(0xF1, -20670, -450, -19630, 225)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(-23140, -610, -22300, 0)
    OP_67(0, 6680, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #17
        0x109,
        (
            "#1841F#6PAww. That sucks.\x02\x03",

            "#1063FThere might be someone in here, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10F,
        (
            "#1803F#6P...\x02\x03",

            "#1440FShould we try breaking it down?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #19
        0x109,
        (
            "#1061F#2PHack away!\x02\x01",

            "#1063F...Wait! No! I was joking!\x02\x03",

            "At least let us TRY to see if we can unlock it\x01",
            "by some other means before skipping to our\x01",
            "last resort!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D68")

    ChrTalk(    #20
        0x107,
        (
            "#560F#6PIt's an airship door we're talking about, so it's\x01",
            "going to be on the sturdy side, anyway.\x02\x03",

            "It'd probably take a lot to break through it...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1D")

    label("loc_D68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E1D")

    ChrTalk(    #21
        0x10D,
        (
            "#272F#6PGiven that this is an airship's door, I imagine\x01",
            "it must be fairly sturdy.\x02\x03",

            "#270FIt would probably take a significant amount\x01",
            "of force to break through it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E1D")

    OP_8C(0x10F, 45, 400)
    Sleep(300)

    ChrTalk(    #22
        0x10F,
        "#1447F#5PNaturally, I was also joking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x109,
        (
            "#1068F#2P(You little fibber...)\x02\x03",

            "#1060FOkay! Now that we've saved this poor door's\x01",
            "life, let's look around for a key to open it.\x02\x03",

            "Until then, we're just going to have to leave it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-20660, -170, -21090, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -20660, -170, -21090, 0)
    SetChrPos(0x1, -20660, -170, -21090, 0)
    SetChrPos(0x2, -20660, -170, -21090, 0)
    SetChrPos(0x3, -20660, -170, -21090, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x270A)
    OP_28(0x2C, 0x1, 0x8)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_8_A87 end

    def Function_9_FE3(): pass

    label("Function_9_FE3")

    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x0, 0x1, 0x0, 0xD)
    OP_43(0x1, 0x1, 0x0, 0xC)
    OP_43(0x2, 0x1, 0x0, 0xB)
    OP_43(0x3, 0x1, 0x0, 0xA)
    WaitChrThread(0x3, 0x1)
    OP_30(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_9_FE3 end

    def Function_10_10C7(): pass

    label("Function_10_10C7")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x12, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB0BE, 0xFFFFFD58, 0xFFFFBA5A, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_10_10C7 end

    def Function_11_111F(): pass

    label("Function_11_111F")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB0BE, 0xFFFFFD58, 0xFFFFBA5A, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_11_111F end

    def Function_12_1169(): pass

    label("Function_12_1169")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB0BE, 0xFFFFFD58, 0xFFFFBA5A, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_12_1169 end

    def Function_13_11A5(): pass

    label("Function_13_11A5")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 180, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB0BE, 0xFFFFFD58, 0xFFFFBA5A, 0x3E8, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_13_11A5 end

    def Function_14_11D3(): pass

    label("Function_14_11D3")

    OP_51(0x10, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x0, 0x1, 0x0, 0x12)
    OP_43(0x1, 0x1, 0x0, 0x11)
    OP_43(0x2, 0x1, 0x0, 0x10)
    OP_43(0x3, 0x1, 0x0, 0xF)
    WaitChrThread(0x3, 0x1)
    OP_30(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_14_11D3 end

    def Function_15_12B7(): pass

    label("Function_15_12B7")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x12, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB3A2, 0x0, 0xFFFFC63A, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_15_12B7 end

    def Function_16_130F(): pass

    label("Function_16_130F")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x11, 0x0, 0x1770, 0x0)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB3A2, 0x0, 0xFFFFC63A, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_16_130F end

    def Function_17_1359(): pass

    label("Function_17_1359")

    SetChrFlags(0xFE, 0x4)
    OP_92(0xFE, 0x10, 0x0, 0x1770, 0x0)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB3A2, 0x0, 0xFFFFC63A, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_17_1359 end

    def Function_18_1395(): pass

    label("Function_18_1395")

    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 0, 0)
    SetChrSubChip(0xFE, 0)
    OP_96(0xFE, 0xFFFFB3A2, 0x0, 0xFFFFC63A, 0x7D0, 0x1388)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_18_1395 end

    SaveToFile()

Try(main)
