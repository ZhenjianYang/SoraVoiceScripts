from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5507   ._SN',
        MapName             = 'Other',
        Location            = 'C5507.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60021",
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
        'Female Jaeger',                        # 9
        'Targeted Smoke Bomb',                  # 10
        'Target Camera',                        # 11
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
        'ED6_DT07/CH00261 ._CH',             # 00
        'ED6_DT27/CH04000 ._CH',             # 01
        'ED6_DT27/CH04001 ._CH',             # 02
        'ED6_DT07/CH00420 ._CH',             # 03
        'ED6_DT07/CH00421 ._CH',             # 04
        'ED6_DT07/CH00264 ._CH',             # 05
        'ED6_DT27/CH03005 ._CH',             # 06
        'ED6_DT27/CH03095 ._CH',             # 07
        'ED6_DT06/CH20020 ._CH',             # 08
        'ED6_DT27/CH04640 ._CH',             # 09
        'ED6_DT27/CH04641 ._CH',             # 0A
        'ED6_DT27/CH04642 ._CH',             # 0B
        'ED6_DT27/CH04644 ._CH',             # 0C
        'ED6_DT26/CH20265 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH00261P._CP',             # 00
        'ED6_DT27/CH04000P._CP',             # 01
        'ED6_DT27/CH04001P._CP',             # 02
        'ED6_DT07/CH00420P._CP',             # 03
        'ED6_DT07/CH00421P._CP',             # 04
        'ED6_DT07/CH00264P._CP',             # 05
        'ED6_DT27/CH03005P._CP',             # 06
        'ED6_DT27/CH03095P._CP',             # 07
        'ED6_DT06/CH20020P._CP',             # 08
        'ED6_DT27/CH04640P._CP',             # 09
        'ED6_DT27/CH04641P._CP',             # 0A
        'ED6_DT27/CH04642P._CP',             # 0B
        'ED6_DT27/CH04644P._CP',             # 0C
        'ED6_DT26/CH20265P._CP',             # 0D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
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
        Unknown3            = 1900552,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -2500,
        Y                   = -100,
        Z                   = 28500,
        Range               = 8500,
        Unknown_10          = 0x76C,
        Unknown_14          = 0x7724,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -3520,
        Y                   = 0,
        Z                   = -11140,
        Range               = 8109,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFE17E,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    DeclActor(
        TriggerX            = 5300,
        TriggerZ            = 0,
        TriggerY            = 9990,
        TriggerRange        = 800,
        ActorX              = 5300,
        ActorZ              = 1000,
        ActorY              = 9990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_201",          # 01, 1
        "Function_2_202",          # 02, 2
        "Function_3_212",          # 03, 3
        "Function_4_119B",         # 04, 4
        "Function_5_124D",         # 05, 5
        "Function_6_14EB",         # 06, 6
        "Function_7_1D92",         # 07, 7
        "Function_8_228A",         # 08, 8
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1EC")
    OP_A3(0x10F0)
    Event(0, 5)

    label("loc_1EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_200")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_200")

    label("loc_200")

    Return()

    # Function_0_1DE end

    def Function_1_201(): pass

    label("Function_1_201")

    Return()

    # Function_1_201 end

    def Function_2_202(): pass

    label("Function_2_202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_211")
    Call(0, 3)
    Jump("loc_211")

    label("loc_211")

    Return()

    # Function_2_202 end

    def Function_3_212(): pass

    label("Function_3_212")

    EventBegin(0x0)
    OP_A2(0x1011)
    Fade(1000)
    OP_6D(2510, 0, -9490, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4140, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2310, 0, -8920, 339)
    SetChrPos(0x10A, 3870, 0, -9500, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_354")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as Recovered 6 Pieces of Gear\x01",                  # 0
            "Set as Not Yet Recovered Even 1 Piece of Gear\x01",      # 1
            "No Change\x01",                                          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32C")
    OP_A2(0x1120)
    OP_A2(0x1121)
    OP_A2(0x1122)
    OP_A2(0x1130)
    OP_A2(0x1132)
    OP_A2(0x1133)
    Jump("loc_34B")

    label("loc_32C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B")
    OP_A3(0x1120)
    OP_A3(0x1121)
    OP_A3(0x1122)
    OP_A3(0x1130)
    OP_A3(0x1132)
    OP_A3(0x1133)

    label("loc_34B")

    FadeToBright(300, 0)

    label("loc_354")


    def lambda_35A():
        OP_8E(0x101, 0x514, 0x0, 0xB0E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_35A)
    Sleep(100)

    def lambda_37A():
        OP_8E(0x10A, 0x9C4, 0x0, 0xB0E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37A)

    def lambda_395():
        OP_6D(2090, 0, 22590, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_395)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)

    def lambda_3B7():
        OP_6D(2150, 0, 2820, 3000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_3B7)

    def lambda_3CF():
        OP_67(0, 9500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3CF)

    def lambda_3E7():
        OP_6B(3220, 3000)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_3E7)
    WaitChrThread(0x10A, 0x0)
    WaitChrThread(0x10A, 0x1)
    WaitChrThread(0x10A, 0x2)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x10A, 500)
    Sleep(100)
    TurnDirection(0x10A, 0x101, 500)

    ChrTalk(    #0
        0x101,
        "#1018F#6PAnelace! I think that's the exit!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10A,
        "#4P#819FWhew! Finally. I thought we'd never get out!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, 70, 0, 18120, 180)
    TurnDirection(0x8, 0x101, 1000)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 11)
    SetChrSubChip(0x8, 3)

    NpcTalk(    #2
        0x8,
        "Woman's Voice",
        "Oh, dear-rie me...\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    NpcTalk(    #3
        0x8,
        "Woman's Voice",
        (
            "I take my eyes off you for one second, and\x01",
            "you run away! Such naughty, naughty children.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(300)

    def lambda_57E():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57E)

    def lambda_58C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_58C)
    Sleep(300)
    LoadEffect(0x0, "map\\\\mp003_00.eff")
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 440, 1000, 10570, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1180, 1000, 8170, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 820, 1000, 5160, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_666():
        OP_96(0xFE, 0x0, 0x0, 0x5DC, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_666)
    Sleep(50)

    def lambda_689():
        OP_96(0xFE, 0xA8C, 0x0, 0x53C, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_689)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1740, 1000, 1930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 6)
    SetChrSubChip(0x10A, 0)
    SetChrChipByIndex(0x10A, 7)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1300, 1000, -600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1680, 1000, -2630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 2000, 1000, -4630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    ChrTalk(    #4
        0x101,
        "#1P#1021F#1KAgh!\x02",
    )


    ChrTalk(    #5
        0x10A,
        "#2P#1312F#1KHnk!\x02",
    )

    Sleep(1000)
    OP_56(0x1)
    OP_59()
    OP_1D(0x56)
    Sleep(500)
    OP_69(0x8, 0x7D0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x10A, 0)
    SetChrChipByIndex(0x10A, 65535)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 10)

    def lambda_815():
        OP_8E(0xFE, 0x82, 0x0, 0x2044, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_815)

    def lambda_830():
        OP_6D(900, 0, 4900, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_830)
    WaitChrThread(0x8, 0x1)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 9)
    WaitChrThread(0x8, 0x2)

    NpcTalk(    #6
        0x8,
        "Female Jaeger",
        (
            "#6PTeehee...\x01",
            "Welcome to my hunting grounds, kittens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1004F#2PA-A woman?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10A,
        (
            "#815F#2PEstelle, watch out!\x02\x03",

            "Whoever she is...she's good!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #9
        0x8,
        "Female Jaeger",
        (
            "#6POooh, sharp enough to pick\x01",
            "up on that, are we?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #10
        0x8,
        "Female Jaeger",
        (
            "#6PNot only that, but you're already back on\x01",
            "your feet after getting a face full of gas.\x01",
            "That's slightly impressive.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #11
        0x8,
        "Female Jaeger",
        (
            "#6PThat's a bracer for you, I suppose!\x01",
            "Pointlessly tough, if nothing else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1005F#2PH-Hey, whoever you are!\x01",
            "What's going on here?!\x02\x03",

            "Why are you attacking the training\x01",
            "grounds? What did we ever do to you?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #13
        0x8,
        "Female Jaeger",
        (
            "#6POh, kitten, you're assuming\x01",
            "I need to answer questions.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #14
        0x8,
        "Female Jaeger",
        "#6PNow, you have two choices:\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #15
        0x8,
        "Female Jaeger",
        (
            "#6PSurrender quietly...or we have\x01",
            "a little hunting party.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x224, 0)), scpexpr(EXPR_END)), "loc_B90")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x224, 1)), scpexpr(EXPR_END)), "loc_BA1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x224, 2)), scpexpr(EXPR_END)), "loc_BB2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 0)), scpexpr(EXPR_END)), "loc_BC3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 2)), scpexpr(EXPR_END)), "loc_BD4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 3)), scpexpr(EXPR_END)), "loc_BE5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_BE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C39")

    ChrTalk(    #16
        0x101,
        (
            "#1002F#2PDamn it...\x02\x03",

            "(Can we hope to fight her off as we are?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C83")

    label("loc_C39")


    ChrTalk(    #17
        0x101,
        (
            "#1003F#2PDammit...\x02\x03",

            "(We just don't have the equipment\x01",
            "to fight her!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C83")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Retreat For Now\x01",      # 0
            "Fight Now\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109C")

    ChrTalk(    #18
        0x101,
        "#1005F#5PAnelace! Come on!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10A,
        "#815F#2PNngh! Right...!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x10A, 0)
    SetChrChipByIndex(0x10A, 65535)

    def lambda_D37():
        OP_8C(0xFE, 180, 800)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D37)
    Sleep(200)

    def lambda_D4A():
        OP_8C(0xFE, 180, 800)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_D4A)
    WaitChrThread(0x101, 0x1)

    def lambda_D5D():
        OP_8E(0xFE, 0x7D0, 0x0, 0xFFFFC0CC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D5D)
    WaitChrThread(0x10A, 0x1)

    def lambda_D7D():
        OP_8E(0xFE, 0x7D0, 0x0, 0xFFFFC0CC, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_D7D)

    def lambda_D98():
        OP_6D(2970, 0, -7130, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D98)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    SetChrChipByIndex(0x8, 11)
    SetChrSubChip(0x8, 3)
    LoadEffect(0x0, "map\\\\mp003_00.eff")
    LoadEffect(0x1, "monster\\\\msc0310.eff")
    Sleep(200)
    OP_43(0x8, 0x3, 0x0, 0x4)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1300, 1000, -600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1280, 1000, -2630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 900, 1000, -3630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1300, 1000, -4630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1000, 1000, -5760, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1300, 1000, -6630, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xFF, 1960, 1000, -7810, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sleep(500)

    def lambda_FCB():
        OP_69(0x8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_FCB)
    WaitChrThread(0x10A, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 9)

    NpcTalk(    #20
        0x8,
        "Female Jaeger",
        (
            "#6PWell, run if you want, kittens.\x01",
            "There's no other way out, after all...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #21
        0x8,
        "Female Jaeger",
        "#6PWe'll just take this dance nice and slow, then.\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5512   ._SN", 102, 0, 0)
    IdleLoop()
    Jump("loc_1196")

    label("loc_109C")


    ChrTalk(    #22
        0x101,
        "#1005F#5PAnelace!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10A,
        "#815F#2PRight behind you!\x02",
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 1)
    Sleep(100)
    SetChrSubChip(0x10A, 0)
    SetChrChipByIndex(0x10A, 3)
    Sleep(500)

    NpcTalk(    #24
        0x8,
        "Female Jaeger",
        "#6POh, yes, kittens... That's right.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #25
        0x8,
        "Female Jaeger",
        (
            "#6PCome closer, now. Let's put\x01",
            "an end to our little hunt!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0x101, 0xFF)
    OP_44(0x10A, 0xFF)
    Battle(0x394, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)

    label("loc_1196")

    Call(0, 6)
    Return()

    # Function_3_212 end

    def Function_4_119B(): pass

    label("Function_4_119B")

    PlayEffect(0x1, 0x0, 0xFF, 210, 800, 7650, 148, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x1, 0x0, 0xFF, 210, 800, 7650, 148, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x1, 0x0, 0xFF, 210, 800, 7650, 148, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_82(0x0, 0x2)
    Return()

    # Function_4_119B end

    def Function_5_124D(): pass

    label("Function_5_124D")

    EventBegin(0x0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 0, 0, 10770, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x10A, 3)
    SetChrPos(0x101, 1370, 0, -36430, 0)
    SetChrPos(0x10A, 3490, 0, -37430, 0)
    FadeToBright(1000, 0)

    def lambda_12CC():
        OP_8E(0x101, 0xFFFFFA42, 0x0, 0x1D4C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12CC)

    def lambda_12E7():
        OP_8E(0x10A, 0x5BE, 0x0, 0x1D4C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_12E7)
    Sleep(1000)
    OP_0D()
    Fade(500)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    SetChrPos(0x101, -470, 0, -3500, 0)
    SetChrPos(0x10A, 1320, 0, -4500, 0)

    def lambda_1337():
        OP_8E(0x101, 0xFFFFFE2A, 0x0, 0x11EE, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1337)

    def lambda_1352():
        OP_8E(0x10A, 0x528, 0x0, 0x11A8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1352)
    OP_6D(390, 0, 7240, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3540, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #26
        0x101,
        "#1005F#2PSorry to make you wait, Miss Creepo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10A,
        (
            "#815F#2PThis time, we're leaving...\x01",
            "either past you, or OVER you!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #28
        0x8,
        "Female Jaeger",
        (
            "#6POooh, such fire this time!\x01",
            "Well, kittens, come closer...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #29
        0x8,
        "Female Jaeger",
        "#6PLet's put an end to our little hunt!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0x101, 0xFF)
    OP_44(0x10A, 0xFF)
    Battle(0x394, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    Call(0, 6)
    Return()

    # Function_5_124D end

    def Function_6_14EB(): pass

    label("Function_6_14EB")

    ClearMapFlags(0x1)
    OP_6D(730, 0, 7340, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3260, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x8, 0, 0, 10770, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 12)
    SetChrSubChip(0x8, 3)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x10A, 3)
    SetChrPos(0x101, -580, 0, 5380, 6)
    SetChrPos(0x10A, 2060, 0, 5380, 343)
    FadeToBright(1000, 0)
    OP_0D()

    NpcTalk(    #30
        0x8,
        "Female Jaeger",
        "#6PErgh. Seems I underestimated you...a little.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#1005F#2PThat'll teach you to look down on bracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10A,
        (
            "#812F#4PYour first mistake was assuming\x01",
            "we're just a pair of clueless little girls!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #33
        0x8,
        "Female Jaeger",
        (
            "#6PMy! So spirited and fiery now!\x01",
            "We'll have to do something about that...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrChipByIndex(0x8, 13)
    SetChrFlags(0x8, 0x2)
    LoadEffect(0x0, "map\\\\mp004_00.eff")
    SetChrPos(0x9, 70, 0, 6150, 28)

    def lambda_16F0():
        OP_99(0xFE, 0x0, 0x9, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_16F0)
    Sleep(800)
    PlayEffect(0x0, 0xFF, 0x8, 250, 900, -500, 0, 0, 0, 1000, 1000, 1000, 0x9, 0, 0, 0, 0)

    ChrTalk(    #34 op#A op#5
        0x101,
        "#2P#1020F#10AThis again?!\x05\x02",
    )

    Sleep(1200)
    OP_22(0x7F, 0x0, 0x64)

    ChrTalk(    #35 op#A op#5
        0x10A,
        "#815F#4P#16AEstelle! Hold your breath!\x05\x02",
    )

    Sleep(1700)
    OP_8C(0x101, 45, 0)
    OP_8C(0x101, 315, 0)

    def lambda_17A2():
        OP_96(0xFE, 0xFFFFF4D4, 0x0, 0x13A6, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17A2)

    def lambda_17C0():
        OP_96(0xFE, 0x8FC, 0x0, 0x1504, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_17C0)
    Sleep(100)
    TurnDirection(0x101, 0x8, 1000)
    TurnDirection(0x10A, 0x8, 1000)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x10A, 0x1)
    Sleep(300)
    FadeToDark(500, 16777215, -1)
    OP_0D()
    Sleep(2000)

    NpcTalk(    #36
        0x8,
        "Female Jaeger",
        (
            "Oh, kittens. You realize we've captured\x01",
            "the Tactician already, yes?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #37
        0x8,
        "Female Jaeger",
        "You're all alone here now.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #38
        0x8,
        "Female Jaeger",
        (
            "Just give up and surrender.\x01",
            "It'll be easier...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 10)

    def lambda_18E1():
        OP_8E(0xFE, 0xFFFFFFCE, 0x0, 0x556E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_18E1)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_44(0x8, 0x1)
    OP_20(0x7D0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    SetChrFlags(0x8, 0x80)
    OP_8C(0x101, 0, 0)
    OP_8C(0x101, 0, 0)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(500)

    ChrTalk(    #39
        0x101,
        "#1007F#5PShe got away...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    Sleep(100)
    SetChrSubChip(0x10A, 0)
    SetChrChipByIndex(0x10A, 65535)
    Sleep(200)
    TurnDirection(0x101, 0x10A, 500)

    def lambda_1980():
        OP_8E(0xFE, 0xFFFFFD44, 0x0, 0x145A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1980)

    def lambda_199B():
        OP_6D(-100, 0, 5180, 1200)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_199B)

    def lambda_19B3():
        TurnDirection(0x10A, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_19B3)
    WaitChrThread(0x10A, 0x1)

    def lambda_19C6():
        OP_8E(0xFE, 0x258, 0x0, 0x140A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_19C6)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x10A, 0x1)
    WaitChrThread(0x10A, 0x3)
    Sleep(150)

    ChrTalk(    #40
        0x101,
        (
            "#1002F#6PWe probably shouldn't chase her,\x01",
            "right, Anelace?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10A,
        (
            "#812FYeah, bad idea. Way too obvious a trap.\x02\x03",

            "#813F...H-Hey, Estelle.\x02\x03",

            "She said, 'We've captured the Tactician,'\x01",
            "didn't she...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1026F#6POh...\x02\x03",

            "#1003FYeah, she was...probably talking about Kurt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10A,
        (
            "#813FYeah...she had to be.\x02\x03",

            "...Please, no...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#1018F#6PHey, don't worry!\x02\x03",

            "Even if he was caught, this is Kurt\x01",
            "we're talking about--he'll be fine!\x02\x03",

            "#1006FBesides...this is the sort of\x01",
            "thing we've been training for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10A,
        (
            "#814FYou really think so?\x02\x03",

            "Hmm... Emergency decision making, survival\x01",
            "techniques, counter-terrorism skills...\x02\x03",

            "#816FYeah... You're right!\x02\x03",

            "We'll put what we've learned\x01",
            "to use and save Kurt!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1001F#6PThat's the Anelace I know!\x02\x03",

            "#1006FHey, how about we return to the lodge real quick?\x02\x03",

            "We should check to see if the\x01",
            "enemy's occupied it, for starters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10A,
        (
            "#810FYeah, good point.\x02\x03",

            "Off we go, then!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1012)
    OP_28(0x7F, 0x1, 0x2000)
    OP_28(0x7F, 0x1, 0x4000)
    OP_28(0x7F, 0x1, 0x8000)
    OP_28(0x80, 0x4, 0x2)
    OP_28(0x80, 0x4, 0x8)
    OP_1D(0x15)
    EventEnd(0x0)
    Return()

    # Function_6_14EB end

    def Function_7_1D92(): pass

    label("Function_7_1D92")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 2)), scpexpr(EXPR_END)), "loc_1DB0")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DC1")

    label("loc_1DB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 2)), scpexpr(EXPR_END)), "loc_1DC1")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DC1")

    SetMapFlags(0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS137._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1E32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_213F")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_1E5D"),
        (1, "loc_1E89"),
        (2, "loc_1ECA"),
        (SWITCH_DEFAULT, "loc_1F1E"),
    )


    label("loc_1E5D")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",          # 0
            "[Balstar Channel]\x01",      # 1
        )
    )

    Jump("loc_1F1E")

    label("loc_1E89")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",             # 0
            "[Balstar Channel]\x01",         # 1
            "[Saint-Croix Forest]\x01",      # 2
        )
    )

    Jump("loc_1F1E")

    label("loc_1ECA")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",             # 0
            "[Balstar Channel]\x01",         # 1
            "[Saint-Croix Forest]\x01",      # 2
            "[Grimsel Fortress]\x01",        # 3
        )
    )

    Jump("loc_1F1E")

    label("loc_1F1E")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F48"),
        (1, "loc_1FC1"),
        (2, "loc_203E"),
        (3, "loc_20BE"),
        (SWITCH_DEFAULT, "loc_213C"),
    )


    label("loc_1F48")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #48
        "\x07\x05Move to [Guild Lodge]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1FAE"),
        (1, "loc_1FBB"),
        (SWITCH_DEFAULT, "loc_1FBE"),
    )


    label("loc_1FAE")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FBE")

    label("loc_1FBB")

    Jump("loc_1FBE")

    label("loc_1FBE")

    Jump("loc_213C")

    label("loc_1FC1")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #49
        "\x07\x05Move to [Balstar Channel]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_202B"),
        (1, "loc_2038"),
        (SWITCH_DEFAULT, "loc_203B"),
    )


    label("loc_202B")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_203B")

    label("loc_2038")

    Jump("loc_203B")

    label("loc_203B")

    Jump("loc_213C")

    label("loc_203E")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #50
        "\x07\x05Move to [Saint-Croix Forest]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_20AB"),
        (1, "loc_20B8"),
        (SWITCH_DEFAULT, "loc_20BB"),
    )


    label("loc_20AB")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20BB")

    label("loc_20B8")

    Jump("loc_20BB")

    label("loc_20BB")

    Jump("loc_213C")

    label("loc_20BE")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #51
        "\x07\x05Move to [Grimsel Fortress]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2129"),
        (1, "loc_2136"),
        (SWITCH_DEFAULT, "loc_2139"),
    )


    label("loc_2129")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2139")

    label("loc_2136")

    Jump("loc_2139")

    label("loc_2139")

    Jump("loc_213C")

    label("loc_213C")

    Jump("loc_1E32")

    label("loc_213F")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2158"),
        (1, "loc_218C"),
        (2, "loc_21C0"),
        (3, "loc_21F4"),
        (SWITCH_DEFAULT, "loc_2228"),
    )


    label("loc_2158")

    OP_C6(0x0, 0x0, -640000, 0, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_2228")

    label("loc_218C")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_2228")

    label("loc_21C0")

    OP_C6(0x0, 0x0, -362000, -266000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_2228")

    label("loc_21F4")

    OP_C6(0x0, 0x0, -64000, -340000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_2228")

    label("loc_2228")

    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2259"),
        (1, "loc_2265"),
        (2, "loc_2271"),
        (3, "loc_227D"),
        (SWITCH_DEFAULT, "loc_2289"),
    )


    label("loc_2259")

    NewScene("ED6_DT21/T5100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2289")

    label("loc_2265")

    NewScene("ED6_DT21/C5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_2289")

    label("loc_2271")

    NewScene("ED6_DT21/C5507   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_2289")

    label("loc_227D")

    NewScene("ED6_DT21/C5508   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_2289")

    label("loc_2289")

    Return()

    # Function_7_1D92 end

    def Function_8_228A(): pass

    label("Function_8_228A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #52
        "\x07\x05Saint-Croix Forest\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #53
        "\x07\x05Recommended for ranger training and other survival lessons.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_228A end

    SaveToFile()

Try(main)
