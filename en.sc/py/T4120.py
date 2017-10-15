from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4120   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Chaeli',                               # 9
        'Shepard',                              # 10
        'Zacharias',                            # 11
        'Tom',                                  # 12
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
        'ED6_DT07/CH01690 ._CH',             # 00
        'ED6_DT07/CH01140 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01043 ._CH',             # 03
        'ED6_DT07/CH01680 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01690P._CP',             # 00
        'ED6_DT07/CH01140P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01043P._CP',             # 03
        'ED6_DT07/CH01680P._CP',             # 04
    )

    DeclNpc(
        X                   = 1260,
        Z                   = 0,
        Y                   = -240,
        Direction           = 236,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 0,
        Y                   = 129840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 58580,
        Z                   = 0,
        Y                   = 360,
        Direction           = 102,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 120030,
        Z                   = 0,
        Y                   = -1260,
        Direction           = 10,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    DeclActor(
        TriggerX            = -10,
        TriggerZ            = 0,
        TriggerY            = -1600,
        TriggerRange        = 800,
        ActorX              = 1260,
        ActorZ              = 1500,
        ActorY              = -240,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60410,
        TriggerZ            = 0,
        TriggerY            = 390,
        TriggerRange        = 800,
        ActorX              = 58580,
        ActorZ              = 1500,
        ActorY              = 360,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 119960,
        TriggerZ            = 0,
        TriggerY            = 650,
        TriggerRange        = 800,
        ActorX              = 120030,
        ActorZ              = 1500,
        ActorY              = -1260,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1BE",          # 00, 0
        "Function_1_2FD",          # 01, 1
        "Function_2_36A",          # 02, 2
        "Function_3_38E",          # 03, 3
        "Function_4_393",          # 04, 4
        "Function_5_1D76",         # 05, 5
        "Function_6_1D7B",         # 06, 6
        "Function_7_271D",         # 07, 7
        "Function_8_2722",         # 08, 8
        "Function_9_2DBD",         # 09, 9
    )


    def Function_0_1BE(): pass

    label("Function_0_1BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_1DC")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    Jump("loc_2FC")

    label("loc_1DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1E6")
    Jump("loc_2FC")

    label("loc_1E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1F0")
    Jump("loc_2FC")

    label("loc_1F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_1FA")
    Jump("loc_2FC")

    label("loc_1FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_22D")
    OP_44(0xB, 0x0)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 3)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xB, 125240, 200, -1310, 90)
    Jump("loc_2FC")

    label("loc_22D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_237")
    Jump("loc_2FC")

    label("loc_237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_241")
    Jump("loc_2FC")

    label("loc_241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_24B")
    Jump("loc_2FC")

    label("loc_24B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_27E")
    OP_44(0xB, 0x0)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 3)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xB, 125240, 200, -1310, 90)
    Jump("loc_2FC")

    label("loc_27E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_2B1")
    OP_44(0xB, 0x0)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 3)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xB, 125240, 200, -1310, 90)
    Jump("loc_2FC")

    label("loc_2B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E8")
    OP_44(0xB, 0x0)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 3)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xB, 125240, 200, -1310, 90)
    Jump("loc_2FC")

    label("loc_2E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2F2")
    Jump("loc_2FC")

    label("loc_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2FC")
    Jump("loc_2FC")

    label("loc_2FC")

    Return()

    # Function_0_1BE end

    def Function_1_2FD(): pass

    label("Function_1_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_310")
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)

    label("loc_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_324")
    OP_64(0x2, 0x1)

    label("loc_324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_340")
    OP_B1("t4120_y")
    Jump("loc_349")

    label("loc_340")

    OP_B1("t4120_n")

    label("loc_349")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_369")
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)

    label("loc_369")

    Return()

    # Function_1_2FD end

    def Function_2_36A(): pass

    label("Function_2_36A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38D")
    OP_8D(0x9, 1470, 131290, -1690, 128210, 2000)
    Jump("Function_2_36A")

    label("loc_38D")

    Return()

    # Function_2_36A end

    def Function_3_38E(): pass

    label("Function_3_38E")

    Call(0, 4)
    Return()

    # Function_3_38E end

    def Function_4_393(): pass

    label("Function_4_393")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E5")
    Call(6, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3C8")
    OP_A9(0xDB)
    Jump("loc_3CA")

    label("loc_3C8")

    OP_A9(0xC8)

    label("loc_3CA")

    TalkEnd(0xA)
    Return()

    label("loc_3D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E2")
    TalkEnd(0xA)
    Return()

    label("loc_3E2")

    Jump("loc_12BC")

    label("loc_3E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12BC")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 60400, 0, -60, 270)
    SetChrPos(0x102, 60400, 0, 800, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44C")
    SetChrPos(0xF9, 61510, 0, -60, 270)
    SetChrPos(0xF8, 61510, 0, 800, 270)
    Jump("loc_46E")

    label("loc_44C")

    SetChrPos(0xF8, 61510, 0, -60, 270)
    SetChrPos(0xF9, 61510, 0, 800, 270)

    label("loc_46E")

    OP_8C(0xA, 90, 0)
    OP_6D(60390, 0, 280, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #0
        0xA,
        (
            "Ah, sorry, but the factory's closed for\x01",
            "business right now..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xA,
        (
            "A few days ago all orbal driven equipment\x01",
            "stopped working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xA,
        (
            "No clue why...\x01",
            "At this rate, though, I'm out of a job.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5EF")

    ChrTalk(    #3
        0x101,
        (
            "#1018F#6POh, right, of course.\x01",
            "Don't worry, though!\x02\x03",

            "I THINK we have a little something to\x01",
            "help with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        "A 'little something'?\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD7")

    label("loc_5EF")


    ChrTalk(    #5
        0x101,
        (
            "#1026F#6POhhh, right.\x02\x03",

            "#1015FWell, that's kind of a problem,\x01",
            "isn't it?\x02\x03",

            "If we can't manufacture quartz or\x01",
            "upgrade our slots, we're kinda\x01",
            "in trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_714")

    ChrTalk(    #6
        0x103,
        (
            "#025FEven if we can use arts, this\x01",
            "makes it a little inconvenient.\x02\x03",

            "At this rate, we're just\x01",
            "wasting our generators.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83D")

    label("loc_714")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79F")

    ChrTalk(    #7
        0x108,
        (
            "#072FEven if we can use arts, this\x01",
            "makes it a little inconvenient.\x02\x03",

            "At this rate, we're just\x01",
            "wasting our generators.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83D")

    label("loc_79F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_83D")

    ChrTalk(    #8
        0x106,
        (
            "#552FKeep in mind we ARE kind of lucky to\x01",
            "even have arts right now.\x02\x03",

            "Does feel like a waste to just be sittin'\x01",
            "on all this sepith, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B0")

    ChrTalk(    #9
        0x107,
        (
            "#064FAh, but, Estelle...\x02\x03",

            "If it's just for a little while,\x01",
            "we might be able to do something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91B")

    label("loc_8B0")


    ChrTalk(    #10
        0x102,
        (
            "#1043F#4PThat's true, but...\x02\x03",

            "#1040FHowever, we may be able to do\x01",
            "something for a short time, anyway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91B")

    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_998")

    def lambda_94B():
        TurnDirection(0x0, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_94B)
    Sleep(120)

    def lambda_95E():
        TurnDirection(0x1, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_95E)

    def lambda_96C():
        TurnDirection(0x2, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_96C)
    Sleep(120)

    def lambda_97F():
        TurnDirection(0x3, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_97F)

    def lambda_98D():
        TurnDirection(0xA, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_98D)
    Jump("loc_99F")

    label("loc_998")

    TurnDirection(0x101, 0x102, 400)

    label("loc_99F")

    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    ChrTalk(    #11
        0x101,
        "#1004F#6PHuh...?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A06")

    ChrTalk(    #12
        0x106,
        "#052FCan you get the factory working?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A7B")

    label("loc_A06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A42")

    ChrTalk(    #13
        0x103,
        "#023FCan you get the factory working?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A7B")

    label("loc_A42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A7B")

    ChrTalk(    #14
        0x108,
        "#073FCan you get the factory working?\x02",
    )

    CloseMessageWindow()

    label("loc_A7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC4")

    ChrTalk(    #15
        0x107,
        (
            "#060FY-Yeah, probably.\x02\x03",

            "If we use the generator...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B36")

    label("loc_AC4")


    ChrTalk(    #16
        0x102,
        (
            "#1040F#4PYes, most likely...\x02\x03",

            "If we use the generator, we can briefly\x01",
            "restore the equipment here, I suspect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B36")


    ChrTalk(    #17
        0x101,
        "#1018F#6PAh, I see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xA,
        (
            "Hey, you guys...\x01",
            "The heck you talkin' about?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B87():
        TurnDirection(0x0, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B87)
    Sleep(120)

    def lambda_B9A():
        TurnDirection(0x1, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_B9A)

    def lambda_BA8():
        TurnDirection(0x2, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_BA8)
    Sleep(120)

    def lambda_BBB():
        TurnDirection(0x3, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_BBB)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    label("loc_BD7")


    ChrTalk(    #19
        0x102,
        "#1040F#4PLet me explain.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "\x07\x05Joshua explained that by using the Zero Field Generator the\x01",
            "factory's functionality could be temporarily restored.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(    #21
        0xA,
        "Izzat true?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xA,
        (
            "Well, the equipment's right there.\x01",
            "Could ya give it a shot?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1006F#6PYeah, if you don't mind.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D3D")

    ChrTalk(    #24
        0x107,
        "#560FOkay! Just a sec...\x02",
    )

    CloseMessageWindow()
    Jump("loc_D8D")

    label("loc_D3D")


    ChrTalk(    #25
        0x102,
        (
            "#1040F#4PWell, then, if you'll let me borrow the\x01",
            "equipment for a moment...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #26
        (
            "\x07\x05On activation, the Zero Field Generator restored power\x01",
            "to the factory's tools.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #27
        0xA,
        "Ohhh... It really worked!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E8E")
    TurnDirection(0xA, 0x0, 400)

    ChrTalk(    #28
        0xA,
        (
            "All right, if you wanna tune your\x01",
            "orbments, now's the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_100E")

    label("loc_E8E")


    ChrTalk(    #29
        0x101,
        "#1000F#6PAwesome. It worked.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F1B")

    ChrTalk(    #30
        0x107,
        (
            "#063FYeah, but it'll only last for a little bit.\x02\x03",

            "#561FIt'll go back to normal soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F80")

    label("loc_F1B")


    ChrTalk(    #31
        0x102,
        (
            "#1040F#4PYeah, it went well...\x02\x03",

            "But it's not really fixed, so after\x01",
            "some time it'll stop again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F80")

    TurnDirection(0xA, 0x0, 400)

    ChrTalk(    #32
        0xA,
        (
            "I see... So it is ultimately just a temporary\x01",
            "patch, in other words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "Well, if you wanna tune your orbments,\x01",
            "now's the time.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    label("loc_100E")

    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x77)
    OP_56(0x0)
    OP_0D()
    Sleep(30)

    ChrTalk(    #34
        0xA,
        (
            "Still, those generators or whatever are\x01",
            "incredible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xA,
        (
            "Just to check...\x01",
            "Would you be willin' to sell one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1004F#6PUh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xA,
        (
            "Even if the cost's a bit high,\x01",
            "I'd be interested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xA,
        (
            "After all, if my equipment was the only\x01",
            "stuff that worked, I'd rake in the mira!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#1016F#6PI wish we could, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        (
            "#1040F#4PI'm sorry.\x01",
            "They're needed for an important mission.\x02\x03",

            "Besides, even if you were able to open your\x01",
            "factory, the citizens can't use their orbments.\x01",
            "So, there wouldn't be much point, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xA,
        "Mmm, there is that problem, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        "Well, bring that when you come by.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        (
            "If you do, you'll be able to use\x01",
            "the factory like normal.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20E5)
    EventEnd(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_12BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1489")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1411")

    ChrTalk(    #44
        0xA,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        (
            "When the orbments stopped, customers pushed\x01",
            "into the store wonderin' if theirs were damaged\x01",
            "or if they got sold bad parts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xA,
        (
            "They were real upset, but Tom explained, and\x01",
            "then they all just nodded their heads and left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        (
            "If it had been just me, I doubt I would've\x01",
            "been able to really persuade 'em.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1486")

    label("loc_1411")


    ChrTalk(    #48
        0xA,
        (
            "Still, though, in this situation,\x01",
            "I can't sell my stock...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        (
            "What the heck have I even been\x01",
            "doing until now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1486")

    Jump("loc_1D72")

    label("loc_1489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1609")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1592")

    ChrTalk(    #50
        0xA,
        (
            "Last night in the West Block, apparently\x01",
            "all orbments just cut out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        (
            "There was a case like that in Zeiss\x01",
            "a while back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xA,
        "If orbments stop workin', my store's dead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        (
            "And my life, that I've spent on this store\x01",
            "would also be over.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1606")

    label("loc_1592")


    ChrTalk(    #54
        0xA,
        "If orbments stop workin', my store's dead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        (
            "And my life, that I've spent on this store\x01",
            "would also be over.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1606")

    Jump("loc_1D72")

    label("loc_1609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_1613")
    Jump("loc_1D72")

    label("loc_1613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_161D")
    Jump("loc_1D72")

    label("loc_161D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_16EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 6)), scpexpr(EXPR_END)), "loc_16A0")

    ChrTalk(    #56
        0xA,
        "...A girl in a white dress?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xA,
        "You mean that kid you brought with you before?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xA,
        "Haven't seen her today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16EC")

    label("loc_16A0")


    ChrTalk(    #59
        0xA,
        "...A girl in a white dress?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xA,
        "Nope, no one like that in this store.\x02",
    )

    CloseMessageWindow()

    label("loc_16EC")

    Jump("loc_1D72")

    label("loc_16EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1768")

    ChrTalk(    #61
        0xA,
        (
            "Apparently Tom's been workin' on repairin'\x01",
            "some of our goods since late last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xA,
        "What an idiot...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D72")

    label("loc_1768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_180F")

    ChrTalk(    #63
        0xA,
        (
            "Tom, as you could probably guess, has\x01",
            "been stubborn since he was a kid...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xA,
        (
            "We may be old friends, but this is\x01",
            "somethin' I can't back down from.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D72")

    label("loc_180F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_19A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1929")

    ChrTalk(    #65
        0xA,
        "...I had a big fight with Tom.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "Lately he's been fixin' and fixin', and\x01",
            "hasn't helped around here at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xA,
        (
            "He keeps doin' that even though gettin' customers\x01",
            "to buy replacements would lift sales.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        "S'practically like payin' him to lose business.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_199E")

    label("loc_1929")


    ChrTalk(    #69
        0xA,
        "I'm not wrong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xA,
        (
            "...We may be called a factory,\x01",
            "but we're still a shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        "We gotta make money to survive.\x02",
    )

    CloseMessageWindow()

    label("loc_199E")

    Jump("loc_1D72")

    label("loc_19A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_1BF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B50")

    ChrTalk(    #72
        0xA,
        "Hey, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x12F,
        (
            "#264FIs this an orbment store?\x02\x03",

            "It's got more things than the\x01",
            "store near my house...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xA, 0x12F, 400)
    Sleep(1000)

    ChrTalk(    #74
        0xA,
        (
            "Oh, are you from outside the country,\x01",
            "little lady?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xA,
        (
            "In that case, why not buy a Liberl\x01",
            "orbment as a souvenir?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x12F,
        (
            "#260FMmmm... Maybe.\x01",
            "Don't have any mira right now.\x02\x03",

            "When Papa and Mama come get me,\x01",
            "I'll come again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xA,
        "Sure thing, kiddo. I'll be waitin'!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1646)
    Jump("loc_1BF2")

    label("loc_1B50")


    ChrTalk(    #78
        0xA,
        (
            "Apparently Tom was up late last night doin'\x01",
            "some repair work he got asked to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xA,
        (
            "He doesn't get paid any better even if does\x01",
            "this extra stuff, ya know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BF2")

    Jump("loc_1D72")

    label("loc_1BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1D72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE5")

    ChrTalk(    #80
        0xA,
        (
            "Doesn't matter how busy he is,\x01",
            "Tom will never refuse a request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xA,
        (
            "Even though we'd make a lot more sellin'\x01",
            "a new product than doin' some stupid repairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        (
            "I wish Tom would start thinking\x01",
            "about profits first.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1D72")

    label("loc_1CE5")


    ChrTalk(    #83
        0xA,
        (
            "...We'd make a lot more sellin' a new\x01",
            "product than doin' some stupid repairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xA,
        (
            "I wish Tom would start thinking\x01",
            "about profits first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D72")

    TalkEnd(0xA)
    Return()

    # Function_4_393 end

    def Function_5_1D76(): pass

    label("Function_5_1D76")

    Call(0, 6)
    Return()

    # Function_5_1D76 end

    def Function_6_1D7B(): pass

    label("Function_6_1D7B")

    TalkBegin(0x8)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DA9")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1DA0")
    OP_A9(0xDA)
    Jump("loc_1DA2")

    label("loc_1DA0")

    OP_A9(0xC9)

    label("loc_1DA2")

    TalkEnd(0x8)
    Return()

    label("loc_1DA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DBA")
    TalkEnd(0x8)
    Return()

    label("loc_1DBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1E3B")

    ChrTalk(    #85
        0x8,
        (
            "As long as I have that man,\x01",
            "I'm scared of nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "We didn't use to have orbments,\x01",
            "so we can live just fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2719")

    label("loc_1E3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1F82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F03")

    ChrTalk(    #87
        0x8,
        (
            "After we had a fight, I was going to leave\x01",
            "the house, but he stopped me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        "And then I finally realized how I felt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        (
            "He thinks more of me than I ever\x01",
            "thought he did...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1F7F")

    label("loc_1F03")


    ChrTalk(    #90
        0x8,
        (
            "That reminds me, when we were fighting,\x01",
            "the city around us was quite loud, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        "I wonder if something happened.\x02",
    )

    CloseMessageWindow()

    label("loc_1F7F")

    Jump("loc_2719")

    label("loc_1F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_1F8C")
    Jump("loc_2719")

    label("loc_1F8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_1F96")
    Jump("loc_2719")

    label("loc_1F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2079")

    ChrTalk(    #92
        0x8,
        (
            "Husband and wife, or strangers both, there are\x01",
            "things you have to say straight out, or else\x01",
            "they won't get across...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x8,
        (
            "Just staying quiet doesn't let\x01",
            "others know what you think...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        "Don't you think so too?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2719")

    label("loc_2079")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_2136")

    ChrTalk(    #95
        0x8,
        "It's been five years since we married...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        (
            "It doesn't matter if I'm angry, or crying...\x01",
            "My husband almost never says anything\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x8,
        "I wonder what on earth he's thinking...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2719")

    label("loc_2136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2301")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_223F")

    ChrTalk(    #98
        0x8,
        (
            "My husband, on top of not being very talkative,\x01",
            "isn't what you'd call very social, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        (
            "It seems like he spent all day\x01",
            "in the warehouse working too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "We're making a living on this business,\x01",
            "so I wish he'd try a bit harder.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_22FE")

    label("loc_223F")


    ChrTalk(    #101
        0x8,
        (
            "Even if there's nothing to be done about\x01",
            "his quiet nature, I wish he was a bit more\x01",
            "personable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        (
            "But I don't intend to force him to smile,\x01",
            "either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        "What should I do, I wonder?\x02",
    )

    CloseMessageWindow()

    label("loc_22FE")

    Jump("loc_2719")

    label("loc_2301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2374")

    ChrTalk(    #104
        0x8,
        "Maybe it's because the signing ceremony's near...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        "It seems as if the city's a lot more lively.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2719")

    label("loc_2374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2624")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2582")

    ChrTalk(    #106
        0x8,
        "Welcome to Weis Arms & Guards!\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)
    TurnDirection(0x8, 0x12F, 400)

    ChrTalk(    #107
        0x8,
        "My, my, what an adorable little girl.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0x8, 400)

    ChrTalk(    #108
        0x12F,
        "#264FWho, me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x8,
        "Yes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x8,
        "I wish I had a darling daughter like you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "How about it?\x01",
            "Want to become my child?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x12F,
        (
            "#267FI already have a papa and mama\x01",
            "I love very much...\x02\x03",

            "#260FSorry, lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x8,
        (
            "Ahaha, it was a joke. I wish I could\x01",
            "at least give you some candy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x8,
        "Sadly, all we have here are weapons.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x12F,
        "#261FHeehee, don't worry. It was a nice thought.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x164B)
    Jump("loc_2621")

    label("loc_2582")


    ChrTalk(    #116
        0x8,
        (
            "If I had a daughter, we could go shopping,\x01",
            "and we could talk and everything, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        (
            "...My husband is the silent type\x01",
            "so I wish I at least had a child.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2621")

    Jump("loc_2719")

    label("loc_2624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2719")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCF, 2)), scpexpr(EXPR_END)), "loc_26B4")

    ChrTalk(    #118
        0x8,
        "Oh, you're...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x8,
        (
            "You're the team of bracers that won\x01",
            "the Martial Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x8,
        "Haha, welcome. Welcome, indeed!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2719")

    label("loc_26B4")


    ChrTalk(    #121
        0x8,
        "Welcome. Welcome to Weis Arms & Guards!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x8,
        (
            "We have all kinds of weapons.\x01",
            "Please, take a look.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2719")

    TalkEnd(0x8)
    Return()

    # Function_6_1D7B end

    def Function_7_271D(): pass

    label("Function_7_271D")

    Call(0, 8)
    Return()

    # Function_7_271D end

    def Function_8_2722(): pass

    label("Function_8_2722")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2813")

    ChrTalk(    #123
        0xB,
        (
            "Seems like everyone finally understands that\x01",
            "all orbments EVERYWHERE aren't working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xB,
        (
            "Seems like the announcement from\x01",
            "Queen Alicia had some effect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xB,
        (
            "Anyway, all we can do is put up with\x01",
            "it while we do what we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB9")

    label("loc_2813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2887")

    ChrTalk(    #126
        0xB,
        (
            "Ever since we fought, Zacharias\x01",
            "and I haven't talked much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xB,
        "But, I don't think I'm wrong at all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DB9")

    label("loc_2887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_2891")
    Jump("loc_2DB9")

    label("loc_2891")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_289B")
    Jump("loc_2DB9")

    label("loc_289B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2983")

    ChrTalk(    #128
        0xB,
        (
            "Zacharias is an old friend, and\x01",
            "we've fought many times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xB,
        (
            "He's always about mira, mira, mira!\x01",
            "He focuses on it waaaay too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xB,
        (
            "I mean, mira's important and all, but I don't\x01",
            "think that's all a factory's for.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB9")

    label("loc_2983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_2A07")

    ChrTalk(    #131
        0xB,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xB,
        "Ah...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xB,
        "Looks like I fell asleep at some point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xB,
        "I got to bed pretty late last night, after all...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DB9")

    label("loc_2A07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A79")

    ChrTalk(    #135
        0xB,
        "Ah, I see... The septium joint's warped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xB,
        "If I swap out the socket, then I'm sure I can...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DB9")

    label("loc_2A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2AFC")

    ChrTalk(    #137
        0xB,
        (
            "I love seeing people smile when they\x01",
            "get back something important repaired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xB,
        "Why doesn't he understand that...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DB9")

    label("loc_2AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2D45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CD8")

    ChrTalk(    #139
        0xB,
        (
            "So this goes like this, and the wiring\x01",
            "goes here...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0xB, 400)

    ChrTalk(    #140
        0x12F,
        "#264FWhat are you doing here, mister?\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)
    TurnDirection(0xB, 0x12F, 400)

    ChrTalk(    #141
        0xB,
        "...I'm fixing Helmuth's orbment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xB,
        (
            "After all, it's important to him. He's had it\x01",
            "for years and it's full of memories...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xB,
        "I want to fix it no matter what.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x12F,
        "#260FHmm... You're great, mister.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xB,
        "...Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xB,
        "No, I mean, haha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xB,
        (
            "Thanks. It's...kind of embarrassing\x01",
            "to have that said. But nice.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_2D42")

    label("loc_2CD8")


    ChrTalk(    #148
        0xB,
        (
            "Just focusing on repairs gets Zacharias\x01",
            "angry at me, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xB,
        "I just can't ignore people in need.\x02",
    )

    CloseMessageWindow()

    label("loc_2D42")

    Jump("loc_2DB9")

    label("loc_2D45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2DB9")

    ChrTalk(    #150
        0xB,
        "Hey, welcome. This is the repairs desk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xB,
        (
            "If you've got a broken orbment,\x01",
            "I can fix it for you here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DB9")

    TalkEnd(0xB)
    Return()

    # Function_8_2722 end

    def Function_9_2DBD(): pass

    label("Function_9_2DBD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2DFE")

    ChrTalk(    #152
        0xFE,
        "No matter what, I have to keep my wife safe...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3297")

    label("loc_2DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2EF2")

    ChrTalk(    #153
        0xFE,
        (
            "Last night at dinner, I decided I'll make\x01",
            "a point of talking to my wife every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "I've always been bad at talking about\x01",
            "how I feel, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "If I don't even try to convey how I feel,\x01",
            "there's no way it'll reach her, huh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3297")

    label("loc_2EF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_2EFC")
    Jump("loc_3297")

    label("loc_2EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_2F06")
    Jump("loc_3297")

    label("loc_2F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2F91")

    ChrTalk(    #156
        0xFE,
        (
            "I want to tell my wife how thankful I am,\x01",
            "but I've always been bad at this kind of\x01",
            "thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "I wonder what I should do.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3297")

    label("loc_2F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_3017")

    ChrTalk(    #158
        0xFE,
        (
            "This store's something I inherited from\x01",
            "my dead father...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "I'm really thankful to my wife for running\x01",
            "it so well..\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3297")

    label("loc_3017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30F8")

    ChrTalk(    #160
        0xFE,
        "I thought I was hungry. It's evening, that's why.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "It's hard to tell how it is outside when you're in\x01",
            "here. Maybe that's why time seems to fly past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        "I think of it as easy and don't mind it at all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3297")

    label("loc_30F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_319A")

    ChrTalk(    #163
        0xFE,
        "The non-aggression pact...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "I don't know the details, but peace is\x01",
            "best, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "I hope our weapons are only used to\x01",
            "fight monsters...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3297")

    label("loc_319A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_3228")

    ChrTalk(    #166
        0xFE,
        "...Welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "If you want to buy weapons, climb the\x01",
            "stairs and go to the front desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        "My wife should be at the counter.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3297")

    label("loc_3228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3297")

    ChrTalk(    #169
        0xFE,
        (
            "The Birthday Celebration's over, and the\x01",
            "town's regained its calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        "This quiet sure is nice...\x02",
    )

    CloseMessageWindow()

    label("loc_3297")

    TalkEnd(0xFE)
    Return()

    # Function_9_2DBD end

    SaveToFile()

Try(main)
