from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2120   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T2120   ._SN',
            'ED6_DT21/T2120_1 ._SN',
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
        'Jean',                                 # 9
        'Tobias',                               # 10
        'Eva',                                  # 11
        "O'Neil",                               # 12
        'Nial',                                 # 13
        'Dorothy',                              # 14
        'Primo',                                # 15
        'Melvin',                               # 16
        'Target Camera',                        # 17
        'Scherazard',                           # 18
        'Agate',                                # 19
        'Tita',                                 # 20
        'Zin',                                  # 21
        'Santos',                               # 22
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
        'ED6_DT07/CH02400 ._CH',             # 00
        'ED6_DT07/CH01020 ._CH',             # 01
        'ED6_DT07/CH01210 ._CH',             # 02
        'ED6_DT07/CH01100 ._CH',             # 03
        'ED6_DT07/CH02060 ._CH',             # 04
        'ED6_DT07/CH02070 ._CH',             # 05
        'ED6_DT07/CH01270 ._CH',             # 06
        'ED6_DT07/CH01760 ._CH',             # 07
        'ED6_DT07/CH00023 ._CH',             # 08
        'ED6_DT07/CH00053 ._CH',             # 09
        'ED6_DT07/CH00063 ._CH',             # 0A
        'ED6_DT07/CH00073 ._CH',             # 0B
        'ED6_DT07/CH01660 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH02400P._CP',             # 00
        'ED6_DT07/CH01020P._CP',             # 01
        'ED6_DT07/CH01210P._CP',             # 02
        'ED6_DT07/CH01100P._CP',             # 03
        'ED6_DT07/CH02060P._CP',             # 04
        'ED6_DT07/CH02070P._CP',             # 05
        'ED6_DT07/CH01270P._CP',             # 06
        'ED6_DT07/CH01760P._CP',             # 07
        'ED6_DT07/CH00023P._CP',             # 08
        'ED6_DT07/CH00053P._CP',             # 09
        'ED6_DT07/CH00063P._CP',             # 0A
        'ED6_DT07/CH00073P._CP',             # 0B
        'ED6_DT07/CH01660P._CP',             # 0C
    )

    DeclNpc(
        X                   = -5700,
        Z                   = 0,
        Y                   = 45100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -30000,
        Z                   = 0,
        Y                   = 4910,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 1,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 0,
        Y                   = 5000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 29900,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -36400,
        Z                   = 0,
        Y                   = 41430,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -1310,
        Y                   = 0,
        Z                   = 38500,
        Range               = 1450,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x9B46,
        Unknown_18          = 0x0,
        Unknown_1C          = 24,
    )


    DeclActor(
        TriggerX            = 1070,
        TriggerZ            = 0,
        TriggerY            = 43260,
        TriggerRange        = 1400,
        ActorX              = 1070,
        ActorZ              = 2000,
        ActorY              = 43260,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -30020,
        TriggerZ            = 0,
        TriggerY            = 3590,
        TriggerRange        = 400,
        ActorX              = -30000,
        ActorZ              = 1500,
        ActorY              = 4910,
        Flags               = 0x7E,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1020,
        TriggerZ            = 0,
        TriggerY            = 3000,
        TriggerRange        = 400,
        ActorX              = 1200,
        ActorZ              = 1500,
        ActorY              = 5000,
        Flags               = 0x7E,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 29980,
        TriggerZ            = 0,
        TriggerY            = 3310,
        TriggerRange        = 400,
        ActorX              = 29900,
        ActorZ              = 1500,
        ActorY              = 4500,
        Flags               = 0x7E,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4420,
        TriggerZ            = 0,
        TriggerY            = 45090,
        TriggerRange        = 600,
        ActorX              = -5700,
        ActorZ              = 1500,
        ActorY              = 45100,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3A6",          # 00, 0
        "Function_1_54C",          # 01, 1
        "Function_2_57C",          # 02, 2
        "Function_3_581",          # 03, 3
        "Function_4_1A24",         # 04, 4
        "Function_5_1AD0",         # 05, 5
        "Function_6_2082",         # 06, 6
        "Function_7_22C5",         # 07, 7
        "Function_8_24AB",         # 08, 8
        "Function_9_2821",         # 09, 9
        "Function_10_2A25",        # 0A, 10
        "Function_11_2C91",        # 0B, 11
        "Function_12_65EA",        # 0C, 12
        "Function_13_7900",        # 0D, 13
        "Function_14_791C",        # 0E, 14
        "Function_15_793D",        # 0F, 15
        "Function_16_797D",        # 10, 16
        "Function_17_79DD",        # 11, 17
        "Function_18_A609",        # 12, 18
        "Function_19_C4EF",        # 13, 19
        "Function_20_E3EF",        # 14, 20
        "Function_21_E40B",        # 15, 21
        "Function_22_E427",        # 16, 22
        "Function_23_E443",        # 17, 23
        "Function_24_E473",        # 18, 24
        "Function_25_EEC1",        # 19, 25
        "Function_26_EEE7",        # 1A, 26
        "Function_27_EF0D",        # 1B, 27
        "Function_28_EF33",        # 1C, 28
        "Function_29_EF81",        # 1D, 29
        "Function_30_F019",        # 1E, 30
    )


    def Function_0_3A6(): pass

    label("Function_0_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3B0")
    Jump("loc_3CA")

    label("loc_3B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3CA")
    ClearChrFlags(0xF, 0x80)

    label("loc_3CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EC")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -2790, 0, 41750, 0)

    label("loc_3EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_42E")
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x11, 8)
    SetChrPos(0x11, -33790, 250, 46120, 180)

    label("loc_42E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_45B")
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 9)
    SetChrPos(0x12, -31990, 250, 46120, 180)

    label("loc_45B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_488")
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x13, 10)
    SetChrPos(0x13, -33850, 250, 43760, 0)

    label("loc_488")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B5")
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x4)
    SetChrChipByIndex(0x14, 11)
    SetChrPos(0x14, -31980, 250, 43650, 0)

    label("loc_4B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_4CB")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 17)
    Jump("loc_54B")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_4E1")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 18)
    Jump("loc_54B")

    label("loc_4E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_4F7")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(1, 7)
    Jump("loc_54B")

    label("loc_4F7")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_503"),
        (SWITCH_DEFAULT, "loc_54B"),
    )


    label("loc_503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51B")
    SetMapFlags(0x10000000)
    Event(0, 19)
    Jump("loc_548")

    label("loc_51B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_537")
    SetMapFlags(0x10000000)
    Event(0, 12)
    Jump("loc_548")

    label("loc_537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_548")
    SetMapFlags(0x10000000)
    Event(0, 11)

    label("loc_548")

    Jump("loc_54B")

    label("loc_54B")

    Return()

    # Function_0_3A6 end

    def Function_1_54C(): pass

    label("Function_1_54C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x248, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_565")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_565")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57B")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)

    label("loc_57B")

    Return()

    # Function_1_54C end

    def Function_2_57C(): pass

    label("Function_2_57C")

    Call(0, 3)
    Return()

    # Function_2_57C end

    def Function_3_581(): pass

    label("Function_3_581")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_BB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x416, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB3")

    ChrTalk(    #0
        0x8,
        (
            "#650FHey, good work. Sounds like things\x01",
            "were pretty tough over at the school.\x02\x03",

            "Guess I should have expected it, but\x01",
            "you took care of it all no problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1001FAhaha, you're welcome.\x02\x03",

            "We couldn't have done it without\x01",
            "your quick response, though, Jean!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        (
            "#1040FShe's right. It was thanks to Carna and\x01",
            "the others that we were able to break in,\x01",
            "essentially.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#650FHaha. That's my job, after all.\x02\x03",

            "Anyway, I'm just relieved things\x01",
            "turned out all right.\x02\x03",

            "#655FOf course, with the orbal blackout\x01",
            "still a thing, we can hardly relax.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81F")

    ChrTalk(    #4
        0x108,
        (
            "#072FThe society might also still do something.\x02\x03",

            "We need to stay vigilant as we proceed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_922")

    label("loc_81F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A2")

    ChrTalk(    #5
        0x103,
        (
            "#022FYeah, the society might still\x01",
            "be planning something.\x02\x03",

            "We need to be careful as\x01",
            "we go forward from here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_922")

    label("loc_8A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_922")

    ChrTalk(    #6
        0x106,
        (
            "#050FThere's no tellin' what the society\x01",
            "might be up to, either.\x02\x03",

            "So we gotta move with caution\x01",
            "from now on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_922")


    ChrTalk(    #7
        0x101,
        "#1002FDefinitely...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_94B")
    OP_A2(0x8)
    Jump("loc_94E")

    label("loc_94B")

    OP_A3(0x8)

    label("loc_94E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F4")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as regional quest unreported\x01",      # 0
            "Set as reported at other branch\x01",       # 1
            "No change\x01",                             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9E8"),
        (1, "loc_9EE"),
        (SWITCH_DEFAULT, "loc_9F4"),
    )


    label("loc_9E8")

    OP_A3(0x8)
    Jump("loc_9F4")

    label("loc_9EE")

    OP_A2(0x8)
    Jump("loc_9F4")

    label("loc_9F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B38")

    ChrTalk(    #8
        0x8,
        (
            "#652FWell, take care of yourselves, okay?\x02\x03",

            "#650FOh, and right, right...\x02\x03",

            "About the case at the academy, I went ahead\x01",
            "and put together the paperwork for it.\x02\x03",

            "If you want to collect your reward,\x01",
            "you'll need to formally report in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1000FAh, yeah. Thanks, Jean!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        "#1040FWell then, if you'll pardon us...\x02",
    )

    CloseMessageWindow()
    Jump("loc_BAC")

    label("loc_B38")


    ChrTalk(    #11
        0x8,
        "#652FTake care of yourselves.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1000FAh, yeah. Thanks, Jean.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x102,
        "#1040FWell, then, if you'll pardon us...\x02",
    )

    CloseMessageWindow()

    label("loc_BAC")

    OP_A2(0x20B5)
    TalkEnd(0x8)
    Return()

    label("loc_BB3")

    Jump("loc_C56")

    label("loc_BB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_C56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x416, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C56")

    ChrTalk(    #14
        0x8,
        (
            "#650FOh, that reminds me...\x02\x03",

            "Tell me if you want to call in anyone\x01",
            "from the other branches.\x02\x03",

            "I'll contact 'em and have them report here.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20B4)

    label("loc_C56")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CC0")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",             # 0
            "Report\x01",           # 1
            "Call Allies\x01",      # 2
            "Leave\x01",            # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jump("loc_CC4")

    label("loc_CC0")

    Call(6, 5)

    label("loc_CC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E7E")
    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D6A")
    OP_28(0xC3, 0x4, 0x20)
    OP_A9(0x67)

    ChrTalk(    #15
        0x8,
        (
            "#650FGood work. Seems you safely\x01",
            "achieved your goal.\x02\x03",

            "If you have any jobs completed,\x01",
            "come on by and report them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E75")

    label("loc_D6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x67)"), scpexpr(EXPR_END)), "loc_DEB")

    ChrTalk(    #16
        0x8,
        (
            "#650FGood work. Seems you safely\x01",
            "achieved your goal.\x02\x03",

            "If you have any jobs completed,\x01",
            "come on by and report them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E75")

    label("loc_DEB")


    ChrTalk(    #17
        0x8,
        (
            "#650FIt doesn't look like you have any\x01",
            "work to report on at the moment.\x02\x03",

            "If you have any jobs completed,\x01",
            "come on by and report them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E75")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_E7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F78")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F71")

    ChrTalk(    #18
        0x8,
        (
            "#650FYou wanna call in some allies?\x02\x03",

            "Got it. I'll contact them immediately.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "\x07\x05Jean contacted the other branches and had members\x01",
            "on standby assemble.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_F71")

    TalkEnd(0x8)
    Return()

    label("loc_F78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F89")
    TalkEnd(0x8)
    Return()

    label("loc_F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1035")

    ChrTalk(    #20
        0x8,
        (
            "#650FSeems like things were pretty\x01",
            "crazy at the academy.\x02\x03",

            "There's a possibility those society guys\x01",
            "are planning more attacks like this.\x02\x03",

            "Do be very careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A20")

    label("loc_1035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_134C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 2)), scpexpr(EXPR_END)), "loc_11BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1126")

    ChrTalk(    #21
        0x8,
        (
            "#650FAbout the contact from the capital branch,\x01",
            "apparently it's not urgent.\x02\x03",

            "They just want you to drop in if you\x01",
            "happen to stop by the capital.\x02\x03",

            "Basically, go see Elnan at some\x01",
            "point when you have the time.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_11BC")

    label("loc_1126")


    ChrTalk(    #22
        0x8,
        (
            "#650FAbout the contact from the capital branch,\x01",
            "apparently it's not urgent.\x02\x03",

            "They just want you to drop in if you\x01",
            "happen to stop by the capital.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11BC")

    Jump("loc_1349")

    label("loc_11BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129D")

    ChrTalk(    #23
        0x8,
        (
            "#650FCould you have a look at the requests\x01",
            "on the job board? Just in case there's\x01",
            "something urgent there.\x02\x03",

            "Also, it'd be great if you could check\x01",
            "on the residents in the outskirts.\x02\x03",

            "I'm counting on you!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1349")

    label("loc_129D")


    ChrTalk(    #24
        0x8,
        (
            "#650FI guess I'd ask you to check the\x01",
            "bulletin board and patrol the outskirts\x01",
            "just in case, if you don't mind.\x02\x03",

            "That's about what I have on your\x01",
            "plate for the moment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1349")

    Jump("loc_1A20")

    label("loc_134C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1507")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_140C")

    ChrTalk(    #25
        0x8,
        (
            "#650FOnce you get to Zeiss, you should\x01",
            "stop in at Professor Russell's.\x02\x03",

            "We should probably pick his brain\x01",
            "about this new Gospel situation.\x02\x03",

            "Anyway, be careful out there!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1504")

    label("loc_140C")

    OP_A2(0x2)

    ChrTalk(    #26
        0x8,
        (
            "#650FOnce you get to Zeiss, you should\x01",
            "stop in at Professor Russell's.\x02\x03",

            "We should probably pick his brain\x01",
            "about this new Gospel situation.\x02\x03",

            "I should be able to keep things under\x01",
            "control here with just Melvin.\x02\x03",

            "Anyway, be careful out there!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1504")

    Jump("loc_1A20")

    label("loc_1507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_15D9")

    ChrTalk(    #27
        0x8,
        (
            "#650FThe royal academy is out the north exit\x01",
            "of the city, then east along the\x01",
            "Gull Seaside Way.\x02\x03",

            "Remember when you helped out\x01",
            "at the school festival?\x02\x03",

            "I'm counting on you for this investigation!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A20")

    label("loc_15D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_1697")

    ChrTalk(    #28
        0x8,
        (
            "#652FSorry, but I need you to handle the\x01",
            "trouble at the bridge.\x02\x03",

            "If the supporters of the two candidates get\x01",
            "into a fist fight, we're gonna have serious\x01",
            "trouble on our hands.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A20")

    label("loc_1697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1878")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1743")

    ChrTalk(    #29
        0x8,
        (
            "#650FOnce you've checked up on all three subjects,\x01",
            "come here and let me know what you found.\x02\x03",

            "We'll go over the information\x01",
            "you've gathered then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1875")

    label("loc_1743")

    OP_A2(0x2)

    ChrTalk(    #30
        0x8,
        (
            "#650FSeems you're working hard.\x02\x03",

            "Are you done poring over the\x01",
            "eyewitness information?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#1000FNo, we're still on that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "#650FOnce you've checked up on all three subjects,\x01",
            "come here and let me know what you found.\x02\x03",

            "We'll go over the information\x01",
            "you've gathered then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#1006FOkay, got it.\x02",
    )

    CloseMessageWindow()

    label("loc_1875")

    Jump("loc_1A20")

    label("loc_1878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1A20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_194D")

    ChrTalk(    #34
        0x8,
        (
            "#650FFirst, I'd like you to check up on the three\x01",
            "eyewitness reports, compile your findings,\x01",
            "then come report to me.\x02\x03",

            "It's not an urgent job, so you can\x01",
            "put it off till later if you need to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A20")

    label("loc_194D")

    OP_A2(0x2)

    ChrTalk(    #35
        0x8,
        (
            "#650FFirst, I'd like you to check up on the three\x01",
            "eyewitness reports, compile your findings,\x01",
            "then come report to me.\x02\x03",

            "It's not an urgent job, so you can\x01",
            "put it off till later if you need to.\x02\x03",

            "Good luck!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A20")

    TalkEnd(0x8)
    Return()

    # Function_3_581 end

    def Function_4_1A24(): pass

    label("Function_4_1A24")

    TalkBegin(0xE)

    ChrTalk(    #36
        0xE,
        (
            "Norman's supporters are arguing with\x01",
            "Portos' supporters on the bridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xE,
        (
            "At this rate it's gonna turn into an outright\x01",
            "brawl. Please, you need to intervene!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_4_1A24 end

    def Function_5_1AD0(): pass

    label("Function_5_1AD0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1EB3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1CA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1BA8")

    ChrTalk(    #38
        0xFE,
        (
            "A bit ago, when I was in the warehouse district,\x01",
            "I got asked a bunch of weird questions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Like, what one needed to be an apprentice\x01",
            "bracer, or how to apply for the job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C9D")

    label("loc_1BA8")

    OP_A2(0x3)

    ChrTalk(    #40
        0xFE,
        (
            "A bit ago, when I was in the warehouse district,\x01",
            "I got asked a bunch of weird questions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Like, what one needed to be an apprentice\x01",
            "bracer, or how to apply for the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Honestly, I wish they'd ask Jean\x01",
            "those sorts of questions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C9D")

    Jump("loc_1EB0")

    label("loc_1CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1DAA")

    ChrTalk(    #43
        0xFE,
        (
            "I've gotten through everything that's happened\x01",
            "up till this point through sheer willpower, but\x01",
            "that can only take a man so far...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "Bracers need knowledge and education,\x01",
            "too, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "I really got hit over the head with\x01",
            "that fact the other day...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB0")

    label("loc_1DAA")

    OP_A2(0x3)

    ChrTalk(    #46
        0xFE,
        (
            "A bit ago, I ended up filling in for Carna\x01",
            "as a Sunday School guest teacher...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "...and oh, man, was I ever hopeless! I gotta\x01",
            "study from the bottom up, starting with the\x01",
            "guild code!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "The sister was super disappointed, too.\x01",
            "It was so embarrassing!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EB0")

    Jump("loc_207E")

    label("loc_1EB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_207E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1F26")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #49
        0xFE,
        "Estelle! Congratulations on your promotion!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "I'll do my best to keep up with you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_207E")

    label("loc_1F26")

    OP_A2(0x3)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #51
        0xFE,
        "Ah, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "It's been a while! Remember me? I'm Melvin,\x01",
            "the junior bracer here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Congratulations on your promotion!\x01",
            "I'll do my best to keep up with you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Honestly, I'm absolutely drowning in work\x01",
            "without Carna around.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2050")
    TurnDirection(0xFE, 0x106, 0)

    ChrTalk(    #55
        0xFE,
        "Agate, good luck to you too!\x02",
    )

    CloseMessageWindow()
    Jump("loc_207E")

    label("loc_2050")

    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(    #56
        0xFE,
        "Scherazard, good luck to you too!\x02",
    )

    CloseMessageWindow()

    label("loc_207E")

    TalkEnd(0xFE)
    Return()

    # Function_5_1AD0 end

    def Function_6_2082(): pass

    label("Function_6_2082")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x11)
    ClearChrFlags(0x11, 0x10)
    TurnDirection(0x11, 0x0, 0)
    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2112")
    Jump("loc_2154")

    label("loc_2112")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_212E")
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2154")

    label("loc_212E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_214A")
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2154")

    label("loc_214A")

    OP_51(0x11, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2154")

    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)

    ChrTalk(    #57
        0x11,
        "#020FOh, do you need something?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Change Party\x01",      # 0
            "Never mind\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_21F9"),
        (SWITCH_DEFAULT, "loc_223F"),
    )


    label("loc_21F9")


    ChrTalk(    #58
        0x11,
        (
            "#020FOh, I see. You want to swap out\x01",
            "your teammates, hmm?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 10)
    Jump("loc_22BC")

    label("loc_223F")


    ChrTalk(    #59
        0x11,
        (
            "#026FWe're in Ruan, of all places. I don't\x01",
            "want to be locked up in here...\x02\x03",

            "#027FMaybe I'll sneak out to the casino.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22BC")

    label("loc_22BC")

    SetChrSubChip(0x11, 0)
    TalkEnd(0x11)
    Return()

    # Function_6_2082 end

    def Function_7_22C5(): pass

    label("Function_7_22C5")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x12)
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x0, 0)
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2355")
    Jump("loc_2397")

    label("loc_2355")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2371")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2397")

    label("loc_2371")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_238D")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2397")

    label("loc_238D")

    OP_51(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2397")

    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)

    ChrTalk(    #60
        0x12,
        "#050FHey, what's up?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Change Party\x01",      # 0
            "Never mind\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2431"),
        (SWITCH_DEFAULT, "loc_2458"),
    )


    label("loc_2431")


    ChrTalk(    #61
        0x12,
        "#052FChangin' your lineup?\x02",
    )

    CloseMessageWindow()
    Call(0, 10)
    Jump("loc_24A2")

    label("loc_2458")


    ChrTalk(    #62
        0x12,
        (
            "#050FI see... Well, do what you want.\x02\x03",

            "I'm just gonna chill here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A2")

    label("loc_24A2")

    SetChrSubChip(0x12, 0)
    TalkEnd(0x12)
    Return()

    # Function_7_22C5 end

    def Function_8_24AB(): pass

    label("Function_8_24AB")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x13)
    ClearChrFlags(0x13, 0x10)
    TurnDirection(0x13, 0x0, 0)
    OP_51(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_253B")
    Jump("loc_257D")

    label("loc_253B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2557")
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_257D")

    label("loc_2557")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2573")
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_257D")

    label("loc_2573")

    OP_51(0x13, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_257D")

    OP_51(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x13, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25E4")

    ChrTalk(    #63
        0x13,
        (
            "#560FAh, Agate.\x02\x03",

            "Umm, did you need something?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2649")

    label("loc_25E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2616")

    ChrTalk(    #64
        0x13,
        "#060FAh, what is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2649")

    label("loc_2616")


    ChrTalk(    #65
        0x13,
        (
            "#060FAh, hello!\x02\x03",

            "Umm, did you need something?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2649")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Change Party\x01",      # 0
            "Never mind\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_26A4"),
        (SWITCH_DEFAULT, "loc_2729"),
    )


    label("loc_26A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2700")

    ChrTalk(    #66
        0x13,
        (
            "#060FAh, yeah, got it. You wanna\x01",
            "swap out your teammates, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2722")

    label("loc_2700")


    ChrTalk(    #67
        0x13,
        "#560FOkay. New lineup it is!\x02",
    )

    CloseMessageWindow()

    label("loc_2722")

    Call(0, 10)
    Jump("loc_2818")

    label("loc_2729")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_27AD")

    ChrTalk(    #68
        0x13,
        (
            "#064FHuh, you don't need me...?\x02\x03",

            "#060FI'll be waiting here, so if anything\x01",
            "happens, just say the word.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2815")

    label("loc_27AD")


    ChrTalk(    #69
        0x13,
        (
            "#064FHuh, you don't need me...?\x02\x03",

            "#060FI'll be waiting here, so just\x01",
            "call me if anything happens...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2815")

    Jump("loc_2818")

    label("loc_2818")

    SetChrSubChip(0x13, 0)
    TalkEnd(0x13)
    Return()

    # Function_8_24AB end

    def Function_9_2821(): pass

    label("Function_9_2821")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x14)
    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x0, 0)
    OP_51(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_28B1")
    Jump("loc_28F3")

    label("loc_28B1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_28CD")
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_28F3")

    label("loc_28CD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_28E9")
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_28F3")

    label("loc_28E9")

    OP_51(0x14, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28F3")

    OP_51(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x14, 0x10)

    ChrTalk(    #70
        0x14,
        "#070FOh, need something?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Change Party\x01",      # 0
            "Never mind\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2991"),
        (SWITCH_DEFAULT, "loc_29B5"),
    )


    label("loc_2991")


    ChrTalk(    #71
        0x14,
        "#070FSwapping out, huh?\x02",
    )

    CloseMessageWindow()
    Call(0, 10)
    Jump("loc_2A1C")

    label("loc_29B5")


    ChrTalk(    #72
        0x14,
        (
            "#070F...You really don't need me?\x02\x03",

            "I thought I'd get to sightsee\x01",
            "around Ruan a bit. Too bad...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A1C")

    label("loc_2A1C")

    SetChrSubChip(0x14, 0)
    TalkEnd(0x14)
    Return()

    # Function_9_2821 end

    def Function_10_2A25(): pass

    label("Function_10_2A25")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_A3(0x7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2AC2")
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x11, 8)
    SetChrPos(0x11, -33790, 250, 46120, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AA7")
    OP_41(0x2, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x7)

    label("loc_2AA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AC2")
    OP_41(0x2, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x7)

    label("loc_2AC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B25")
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 9)
    SetChrPos(0x12, -31990, 250, 46120, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B0A")
    OP_41(0x5, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x7)

    label("loc_2B0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B25")
    OP_41(0x5, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x7)

    label("loc_2B25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B88")
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x13, 10)
    SetChrPos(0x13, -33850, 250, 43760, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B6D")
    OP_41(0x6, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x7)

    label("loc_2B6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B88")
    OP_41(0x6, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x7)

    label("loc_2B88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BEB")
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x4)
    SetChrChipByIndex(0x14, 11)
    SetChrPos(0x14, -31980, 250, 43650, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BD0")
    OP_41(0x7, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x7)

    label("loc_2BD0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BEB")
    OP_41(0x7, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x7)

    label("loc_2BEB")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2C90")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #73
        (
            "\x07\x05A standby member was equipped with a Zero Field Generator.\x01",
            "It has been recovered and added to party inventory.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_2C90")

    Return()

    # Function_10_2A25 end

    def Function_11_2C91(): pass

    label("Function_11_2C91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CA2")
    Call(0, 29)

    label("loc_2CA2")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrPos(0x101, -3540, 0, 45230, 0)
    SetChrPos(0xF7, -3540, 0, 43990, 0)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0xF7, 0x8, 400)
    OP_4A(0x8, 255)
    OP_6D(-650, 0, 40270, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    def lambda_2D25():
        OP_6D(-4590, 0, 45190, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D25)

    def lambda_2D3D():
        OP_67(0, 7240, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D3D)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4978")

    ChrTalk(    #74
        0x8,
        (
            "#650F#3POh! Hey! Welcome back!\x01",
            "Boy, but I'm glad you guys are here.\x02\x03",

            "Carna's been away, so the board's\x01",
            "covered with jobs.\x02\x03",

            "#651FYou guys have your work cut out for you.\x01",
            "Geared up and ready to go, I hope?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1016F#4PAh...haha...\x01",
            "Sending us out already...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x106,
        (
            "#053F#6PWe were expecting a LITTLE board\x01",
            "work, but...\x02\x03",

            "#050FAnything urgent come up lately?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "#650F#3PWell, no. We're snowed under with\x01",
            "work in general, but none of it is\x01",
            "particularly urgent.\x02\x03",

            "I mean, the election's being held under\x01",
            "the eyes of the military anyway...\x02\x03",

            "The town's so busy boiling over\x01",
            "from the election that the tourists\x01",
            "have stayed away a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1015F#4PWhoa, the election's gotten that hot?\x02\x03",

            "Who's running? We haven't heard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#650F#3PMr. Norman, who is a proponent of the tourism\x01",
            "industry, and Mr. Portos, who wants to try and\x01",
            "revive the harbors and shipping business.\x02\x03",

            "Remember, this is a big deal--the mayor of\x01",
            "Ruan is also the governor of the entire region!\x02\x03",

            "People in Manoria and elsewhere are\x01",
            "voting, too. It's been a real media circus.\x02\x03",

            "#651FThis election is basically going to decide\x01",
            "the future of Ruan. It's exciting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#1006F#4PI get it now. That IS big!\x02\x03",

            "Well, given that I'm underage and not a\x01",
            "citizen of Ruan, I guess I can't vote...\x02\x03",

            "Gotta admit, though, since I, uh, basically\x01",
            "helped CAUSE this, I'm sorta curious to\x01",
            "see where it goes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        (
            "#651F#3POh, then read the coverage from the Liberl News.\x01",
            "Their investigative articles are excellent.\x02\x03",

            "#653FInvestigation... Wait, that reminds me...\x02\x03",

            "#652FThere is actually a job I'd like for you to focus\x01",
            "on. It isn't 'urgent,' but...it's something that\x01",
            "needs looking into.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        "#1004F#4POh? What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        (
            "#654F#3PUh, well, how do I put this...?\x02\x03",

            "It's hard to explain.\x01",
            "Maybe I shouldn't have...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x106,
        (
            "#555F#6PThe heck? Ain't like you to beat\x01",
            "around the bush, Jean.\x02\x03",

            "Since when do you hesitate to pile\x01",
            "the work on? Come on, spit it out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        (
            "#651F#3PHaha! Well, ah, thanks for the honesty...\x01",
            "I think...\x02\x03",

            "#652FWell, all right. Here it is:\x02\x03",

            "I want you to investigate ghost sightings.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)
    OP_63(0x106)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #86
        0x8,
        (
            "#654F#3PSee, I KNEW you were gonna\x01",
            "look at me like that...\x02\x03",

            "This is why I didn't want\x01",
            "to bring it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#1016F#4PN-No, sorry, it's just a bit of,\x01",
            "um, a surprise, is all.\x02\x03",

            "#1011FSo...uh, what exactly do you\x01",
            "mean by 'ghost sightings'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        (
            "#652F#3POkay, so.\x01",
            "It began about two weeks ago.\x02\x03",

            "We've been receiving reports that people\x01",
            "have been seeing a 'white shadow' at night.\x02\x03",

            "And not just in the City of Ruan, mind you.\x01",
            "Reports have come in from all across\x01",
            "the province.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#1015F#4PThey saw a 'white shadow' at night...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #90
        0x101,
        "#1020F#3S#4PW-W-Wait, you mean...?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #91
        0x106,
        (
            "#053F#6PAh, so that's why you said a 'ghost.'\x02\x03",

            "#050FAnd it probably isn't a prank or\x01",
            "a trick of the eyes, if people are\x01",
            "seeing this thing all over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "#652F#3PExactly. I'd have dismissed one sighting,\x01",
            "but with all the reports we've gotten...\x02\x03",

            "While you're traveling around working on\x01",
            "the other jobs, do you think you could\x01",
            "follow up on a few of the reports?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #93
        0x101,
        (
            "#1008F#4PEr, um, well, you see...\x02\x03",

            "#1013FUh, it'd be...irresponsible of us to take\x01",
            "such a job with so much else going on!\x01",
            "Yeah... That's it...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 0)
    TurnDirection(0x8, 0x101, 0)
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    OP_63(0x8)

    ChrTalk(    #94
        0x8,
        "#653F#3PEstelle...are you...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 600)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x8, 600)
    Sleep(400)
    TurnDirection(0x101, 0x106, 600)

    ChrTalk(    #95
        0x101,
        (
            "#1008F#4PWha, noooo, nonono! Not at all!\x02\x03",

            "You think Estelle the Coup-Breaker,\x01",
            "Hero of Liberl, would be afraid of ghosts?\x01",
            "No way! No how! No...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 500)

    ChrTalk(    #96
        0x101,
        (
            "#1007F#4P...Sorry, I AM afraid of ghosts.\x01",
            "A little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x8,
        (
            "#651F#3PHaha! More than a little,\x01",
            "from the looks of it.\x02\x03",

            "#650FWell, don't worry. Nobody's been hurt\x01",
            "or anything, and it isn't urgent. We'll \x01",
            "just pretend this conversation didn't--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x106,
        "#053F#6PNo. We'll take it.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #99
        0x106,
        (
            "#057F#6PDon't forget. A big part of our mission\x01",
            "is investigating the society.\x02\x03",

            "We're to keep an eye out for even the\x01",
            "slightest hints of activity from them.\x02\x03",

            "That's the plan, remember?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#1026F#4POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x106,
        (
            "#053F#6PEveryone has things they have\x01",
            "trouble handling. Everyone.\x02\x03",

            "So don't be afraid to admit\x01",
            "you're scared of something...\x02\x03",

            "#057F...but admit it, and do something about\x01",
            "it, instead of just running away from it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#1003F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        "#654F#3POuch. Little harsh, don't you think, Agate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1010F#4P...No. Agate's totally right.\x02\x03",

            "#1002FI'm afraid of ghosts, but...\x02\x03",

            "No ghost...could match the terror\x01",
            "I felt the day Joshua disappeared.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #105
        0x8,
        "#653F#3PEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x106,
        "#051F#6PHeh, now you get it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(    #107
        0x101,
        (
            "#1006F#4PJean. We'll investigate those sightings\x01",
            "and get to the bottom of them. I promise!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x8,
        (
            "#651F#3PGlad to hear it.\x02\x03",

            "#652FAnyway, I've got three sightings in\x01",
            "particular that I think bear looking\x01",
            "into.\x02\x03",

            "The first one is a report from\x01",
            "a guard at Air-Letten.\x02\x03",

            "Apparently, he saw something during\x01",
            "a night patrol that spooked the heck\x01",
            "out of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#1007F#4POookay...\x01",
            "Not scared, not scared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x8,
        (
            "#655F#3PThe second one I know of was a sighting\x01",
            "by a member of the Ravens.\x02\x03",

            "#650FFigure that one should be easy\x01",
            "since Agate is with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x106,
        (
            "#051F#6PHeh. If he doesn't talk, I'll remind\x01",
            "the guy who his REAL boss is.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #112
        0x101,
        (
            "#1007F#4POh, cut it out with the macho stuff...\x02\x03",

            "#1025FThey seemed...kind of different during\x01",
            "the tournament in Grancel, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x106,
        "#552F#6PYeah, I kind of doubt it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x8,
        (
            "#654F#3PWell, ah, do try to be...\x01",
            "SUBTLE about it, yes?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #115
        0x8,
        (
            "#650F#3PThe last report is from one of the\x01",
            "children at the Mercia Orphanage.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #116
        0x101,
        "#1004F#4PWait, one of the orphanage kids?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x8,
        (
            "#650F#3PYes, Matron Theresa contacted us on her behalf.\x02\x03",

            "Oh, right, guess you wouldn't know. Reconstruction\x01",
            "of the orphanage finished not too long ago.\x02\x03",

            "According to Matron Theresa, it's more\x01",
            "or less exactly as it once was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1017F#4PIt is? That's a relief.\x02\x03",

            "I wanted to go say hi to Matron Theresa\x01",
            "and the kids anyway.\x02\x03",

            "I'll ask about the...thingy sighting\x01",
            "when I go congratulate them over\x01",
            "the new orphanage building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x8,
        (
            "#651F#3PAnd that's it!\x02\x03",

            "#650FRemember, though, this really isn't urgent,\x01",
            "so you can put it off for a bit if something\x01",
            "else comes up.\x02\x03",

            "The rest of the jobs are on the board,\x01",
            "so make sure to check it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4618():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4618)

    def lambda_4626():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_4626)
    OP_6D(-720, 0, 45530, 1500)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #120
        (
            "\x07\x05Bracer quests, which you may choose to accept or ignore,\x01",
            "are posted to the board in each guildhouse. If you\x01",
            "approach the board and press the confirm prompt when\x01",
            "the ! mark appears, you can see the full list.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #121
        (
            "\x07\x05Select a job to see the details on it such as the objective\x01",
            "and potential rewards. These details will automatically be\x01",
            "recorded in your notebook.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    def lambda_47C8():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47C8)

    def lambda_47D6():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_47D6)
    OP_6D(-4590, 0, 45190, 1500)

    ChrTalk(    #122
        0x8,
        (
            "#650F#3POnce you've heard what all three witnesses\x01",
            "have to say, come back here.\x02\x03",

            "We can go over all the testimonies and\x01",
            "take a stab at figuring this mess out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        (
            "#1006F#4PUnderstood!\x02\x03",

            "The Ravens hang out right here in\x01",
            "the city, in the Warehouse District.\x01",
            "We might check with them first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x106,
        (
            "#051F#6PRight. The Warehouse District is across\x01",
            "the bridge, by the harbor. Let's move out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65AE")

    label("loc_4978")


    ChrTalk(    #125
        0x8,
        (
            "#650F#3POh! Hey! Welcome back!\x01",
            "Boy, but I'm glad you guys are here.\x02\x03",

            "Carna's been away, so the board's\x01",
            "covered with jobs.\x02\x03",

            "#651FYou guys have your work cut out for you.\x01",
            "Geared up and ready to go, I hope?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        "#1016F#4PAh...haha... Sending us out already...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x103,
        (
            "#021F#6POh, I think I can guess the\x01",
            "reason for his eagerness.\x02\x03",

            "#020FSo, O taskmaster, I take it you\x01",
            "have some urgent jobs for us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x8,
        (
            "#650F#3PSurprisingly, not actually. We're snowed\x01",
            "under with work in general, but none of\x01",
            "it is particularly urgent.\x02\x03",

            "I mean, the election's being held under\x01",
            "the eyes of the military anyway...\x02\x03",

            "The town's so busy boiling over\x01",
            "from the election that the tourists\x01",
            "have stayed away a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1015F#4PWhoa, the election's gotten that hot?\x02\x03",

            "Who's running? We haven't heard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x8,
        (
            "#650F#3PMr. Norman, who is a proponent of the tourism\x01",
            "industry, and Mr. Portos, who wants to try and\x01",
            "revive the harbors and shipping business.\x02\x03",

            "Remember, this is a big deal--the mayor of\x01",
            "Ruan is also the governor of the entire region!\x02\x03",

            "People in Manoria and elsewhere are voting,\x01",
            "too. It's been a real media circus.\x02\x03",

            "#651FThis election is basically going to decide\x01",
            "the future of Ruan. It's exciting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        (
            "#1006F#4PI get it now. That IS big!\x02\x03",

            "Well, given that I'm underage and not a\x01",
            "citizen of Ruan, I guess I can't vote...\x02\x03",

            "Gotta admit, though, since I, uh,\x01",
            "basically helped CAUSE this, I'm\x01",
            "sorta curious to see where it goes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x8,
        (
            "#651F#3POh, then read the coverage from the Liberl News.\x01",
            "Their investigative articles are excellent.\x02\x03",

            "#653FInvestigation... Wait, that reminds me...\x02\x03",

            "#652FThere is actually a job I'd like for you to focus\x01",
            "on. It isn't 'urgent,' but...it's something that\x01",
            "needs looking into.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        "#1004F#4POh? What's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x8,
        (
            "#655F#3PUh, well, how do I put this...\x02\x03",

            "It's hard to explain.\x01",
            "Maybe I shouldn't have...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x103,
        (
            "#027F#6PJean? Unsure? Hold the presses,\x01",
            "I think we're witnessing a miracle.\x02\x03",

            "Usually you'll happily pile the work\x01",
            "on a bracer till they sink into the\x01",
            "ground from the weight of it all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        (
            "#654F#3PAww, Schera, I'm not THAT bad, come on...\x02\x03",

            "#652FWell, all right. Here it is:\x02\x03",

            "I want you to investigate ghost sightings.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)
    OP_63(0x103)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #137
        0x8,
        (
            "#654F#3PSee, I KNEW you were gonna\x01",
            "look at me like that...\x02\x03",

            "This is why I didn't want to bring it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        (
            "#1016F#4PN-No, sorry, it's just a bit of,\x01",
            "um, a surprise, is all.\x02\x03",

            "#1011FSo...uh, what exactly do you\x01",
            "mean by 'ghost sightings'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x8,
        (
            "#652F#3POkay, so.\x01",
            "It began about two weeks ago.\x02\x03",

            "We've been receiving reports that people\x01",
            "have been seeing a 'white shadow' at night.\x02\x03",

            "And not just in the City of Ruan, mind you.\x01",
            "Reports have come in from all across\x01",
            "the province.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        "#1015F#4PThey saw a 'white shadow' at night...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #141
        0x101,
        "#1020F#3S#4PW-W-Wait, you mean...?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #142
        0x103,
        (
            "#026F#6PAh, so that's why you called\x01",
            "it a 'ghost,' then.\x02\x03",

            "#020FIf it was just a prank or something,\x01",
            "you wouldn't be hearing about it\x01",
            "province-wide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x8,
        (
            "#652F#3PExactly. I'd have dismissed one sighting,\x01",
            "but with all the reports we've gotten...\x02\x03",

            "While you're traveling around working on\x01",
            "the other jobs, do you think you could\x01",
            "follow up on a few of the reports?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #144
        0x101,
        (
            "#1008F#4PEr, um, well, you see...\x02\x03",

            "#1013FUh, it'd be...irresponsible of us to take\x01",
            "such a job with so much else going on!\x01",
            "Yeah... That's it...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    TurnDirection(0x8, 0x101, 400)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x103)
    OP_63(0x8)

    ChrTalk(    #145
        0x8,
        "#653F#3PEstelle...are you...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 600)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x8, 600)
    Sleep(400)
    TurnDirection(0x101, 0x103, 600)

    ChrTalk(    #146
        0x101,
        (
            "#1008F#4PWha, noooo, nonono! Not at all!\x02\x03",

            "You think Estelle the Coup-Breaker,\x01",
            "Hero Of Liberl, would be afraid of ghosts?\x01",
            "No way! No how! No...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #147
        0x101,
        (
            "#1007F#4P...Sorry, I AM afraid of ghosts.\x01",
            "A little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        (
            "#651F#3PHaha! More than a little,\x01",
            "from the looks of it.\x02\x03",

            "#650FWell, don't worry. Nobody's been hurt\x01",
            "or anything, and it isn't urgent. We'll \x01",
            "just pretend this conversation didn't--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x103,
        (
            "#026F#6PJean, wait.\x02\x03",

            "#020FEstelle...don't you think we\x01",
            "should take this job?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #150
        0x103,
        (
            "#021F#6PDon't you worry, your big sister\x01",
            "will make it aaaall better. ㈱\x02\x03",

            "#020FBesides, investigating this could\x01",
            "prove useful to our, ah, actual\x01",
            "mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x101,
        "#1026F#4PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x103,
        (
            "#026F#6PRemember, Estelle. Our true purpose is\x01",
            "investigating the movements of the\x01",
            "society throughout Liberl.\x02\x03",

            "And that involves keeping an eye out for\x01",
            "anything even remotely suspicious.\x02\x03",

            "#027FSounds a little bit like a 'ghost hunt'\x01",
            "to me...wouldn't you agree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        (
            "#1004F#4PAh...\x02\x03",

            "#1011FYeah...when you put it like that,\x01",
            "it makes sense...\x02\x03",

            "#1007FSorry, Schera. I was being childish.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x103, 0x8, 400)

    ChrTalk(    #154
        0x101,
        (
            "#1006F#4PJean. We'll investigate those sightings\x01",
            "and get to the bottom of them.\x01",
            "I promise!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x8,
        (
            "#651F#3PGlad to hear it!\x02\x03",

            "#652FAnyway, I've got three sightings in\x01",
            "particular that I think bear looking\x01",
            "into.\x02\x03",

            "The first one is a report from\x01",
            "a guard at Air-Letten.\x02\x03",

            "Apparently, he saw something during\x01",
            "a night patrol that spooked the heck\x01",
            "out of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        (
            "#1007F#4POookay...\x01",
            "Not scared, not scared...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x8,
        (
            "#655F#3PThe second one I know of was a sighting\x01",
            "by a member of the Ravens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x103,
        (
            "#022F#6PThe Ravens... That's the local\x01",
            "docks gang, right?\x02\x03",

            "#522FHmm... Hopefully we can get\x01",
            "them to cooperate.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #159
        0x101,
        (
            "#1025F#4PI don't think that'll actually be\x01",
            "as big a problem as you think...\x02\x03",

            "They seemed...kind of different during\x01",
            "the tournament in Grancel, y'know?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #160
        0x103,
        (
            "#023F#6PReally? You'll have to fill\x01",
            "me in on the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x8,
        (
            "#651F#3PWell, sounds like you'll make\x01",
            "it work. Anyway...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x103, 0x8, 400)

    ChrTalk(    #162
        0x8,
        (
            "#650F#3PThe last report is from one of the\x01",
            "children at the Mercia Orphanage.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #163
        0x101,
        "#1004F#4PWait, one of the orphanage kids?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x8,
        (
            "#650F#3PYes, Matron Theresa contacted us on her behalf.\x02\x03",

            "Oh, right, guess you wouldn't know. Reconstruction\x01",
            "of the orphanage finished not too long ago.\x02\x03",

            "According to Matron Theresa, it's more or\x01",
            "less exactly as it once was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        (
            "#1017F#4PIt is? That's a relief.\x02\x03",

            "I wanted to go say hi to Matron Theresa\x01",
            "and the kids anyway.\x02\x03",

            "I'll ask about the...thingy sighting when\x01",
            "I go congratulate them over the new\x01",
            "orphanage building!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x8,
        (
            "#651F#3PAnd that's it!\x02\x03",

            "#650FRemember, though, this really isn't\x01",
            "urgent, so you can put it off for a\x01",
            "bit if something else comes up.\x02\x03",

            "The rest of the jobs are on the board,\x01",
            "so make sure to check it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6238():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6238)

    def lambda_6246():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_6246)
    OP_6D(-720, 0, 45530, 1500)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #167
        (
            "\x07\x05Bracer quests, which you may choose to accept or ignore,\x01",
            "are posted to the board in each guildhouse. If you\x01",
            "approach the board and press the confirm prompt when\x01",
            "the ! mark appears, you can see the full list.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #168
        (
            "\x07\x05Select a job to see the details on it such as the objective\x01",
            "and potential rewards. These details will automatically be\x01",
            "recorded in your notebook.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    def lambda_63E8():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_63E8)

    def lambda_63F6():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_63F6)
    OP_6D(-4590, 0, 45190, 1500)

    ChrTalk(    #169
        0x8,
        (
            "#650F#3POnce you've heard what all three witnesses\x01",
            "have to say, come back here.\x02\x03",

            "We can go over all the testimonies and\x01",
            "take a stab at figuring this mess out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        (
            "#1006F#4PUnderstood!\x02\x03",

            "The Ravens hang out right here in\x01",
            "the city, in the Warehouse District.\x01",
            "We might check with them first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x103,
        (
            "#020F#6PWell, then, let's stop by the Warehouse\x01",
            "District before we leave town. That's\x01",
            "across the bridge, I believe?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65AE")

    OP_A2(0x1206)
    OP_28(0x81, 0x1, 0x80)
    OP_28(0x81, 0x4, 0x10)
    OP_28(0x81, 0x4, 0x20)
    OP_28(0x82, 0x4, 0x2)
    OP_28(0x82, 0x4, 0x8)
    OP_28(0x82, 0x1, 0x1)
    OP_28(0x82, 0x1, 0x2)
    OP_28(0x82, 0x1, 0x10)
    OP_28(0x82, 0x1, 0x80)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_11_2C91 end

    def Function_12_65EA(): pass

    label("Function_12_65EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65FB")
    Call(0, 29)

    label("loc_65FB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x101, 180, -500, 37430, 45)
    SetChrPos(0xF7, 180, -500, 37430, 45)
    SetChrPos(0xC, -3540, 0, 45230, 275)
    SetChrPos(0xD, -2540, 0, 46000, 275)
    SetChrPos(0xE, 530, 0, 38440, 0)
    OP_4A(0xE, 255)
    OP_4A(0x8, 255)
    OP_6D(-520, 0, 40270, 0)
    OP_67(0, 6260, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF7, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_66D1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_66D1)

    def lambda_66E3():
        OP_8E(0xFE, 0xFFFFFD94, 0x0, 0x9B1E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_66E3)
    Sleep(500)

    def lambda_6703():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_6703)

    def lambda_6715():
        OP_8E(0xFE, 0x226, 0x0, 0x9934, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_6715)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0xF7, 0x0)
    TurnDirection(0x101, 0xC, 400)
    TurnDirection(0xF7, 0xC, 400)

    ChrTalk(    #172
        0x101,
        "#1004F#6PHey...!\x02",
    )

    CloseMessageWindow()

    def lambda_6783():

        label("loc_6783")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_6783")

    QueueWorkItem2(0xC, 1, lambda_6783)
    Sleep(200)

    def lambda_6799():

        label("loc_6799")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_6799")

    QueueWorkItem2(0xD, 1, lambda_6799)
    Sleep(100)

    def lambda_67AF():

        label("loc_67AF")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_67AF")

    QueueWorkItem2(0x8, 1, lambda_67AF)

    ChrTalk(    #173
        0xC,
        "#141F#6PHey, you're back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xD,
        "#151F#4PEstelle! Helloooooo!\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0xD)

    def lambda_6808():
        OP_6D(-3940, 0, 45120, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6808)

    def lambda_6820():
        OP_67(0, 6260, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6820)
    OP_43(0xF7, 0x1, 0x0, 0xE)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF7, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0x8, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #175
        0x101,
        "#1008F#3PNial! Dorothy! What are you two doing in Ruan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xC,
        (
            "#141F#6PObviously, getting some pictures taken\x01",
            "and articles made for this friggin' wildfire\x01",
            "of an election!\x02\x03",

            "And THEN I heard something weird beyond\x01",
            "that happening, so I stopped by to check\x01",
            "out what's up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#1017F#3PSomething weird...? You mean this white\x01",
            "shadow thing people have been reporting?\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)

    ChrTalk(    #178
        0x8,
        (
            "#654FActually, while you were out, we had another\x01",
            "report of the thing appearing in the city limits.\x02\x03",

            "The citizenry is starting to get\x01",
            "frightened and demand answers\x01",
            "that I can't give them...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6AD4")

    ChrTalk(    #179
        0x106,
        (
            "#050F#2PAh, hell...\x01",
            "This is really becoming a problem.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6AFC")

    label("loc_6AD4")


    ChrTalk(    #180
        0x103,
        "#022F#2PThis is getting serious...\x02",
    )

    CloseMessageWindow()

    label("loc_6AFC")


    ChrTalk(    #181
        0x8,
        (
            "#652FAnd the capstone to it all...would be\x01",
            "the picture this young lady took.\x02\x03",

            "This one pretty much puts the\x01",
            "nail in the coffin as to what's\x01",
            "going on, so to speak...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        "#1015F#3PA picture...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #183
        0x101,
        "#1020F#3PY-Y-You mean...?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6C54")

    ChrTalk(    #184
        0x106,
        "#052F#2PWhat, so you're into ghost hunting now?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C99")

    label("loc_6C54")


    ChrTalk(    #185
        0x103,
        (
            "#023F#2PReally? I had no idea you liked\x01",
            "ghost hunting, Dorothy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C99")


    ChrTalk(    #186
        0xD,
        (
            "#150FMmm, it's nothing like that, really.\x02\x03",

            "I was just taking pictures of the hotel\x01",
            "at night, and skaboosh! Ghost picture!\x02\x03",

            "Here, take a look!\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x240090, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #187
        "#1020FWh... Wh...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6DB6")
    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #188
        "#552F...Huh. Yeah, I'd, uh, call this decisive.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_6E01")

    label("loc_6DB6")

    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #189
        "#025F...Well. That's pretty decisive, all right.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_6E01")

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #190
        (
            "#1016FAhaha! Ha ha! Ha! Come on, guys, don't\x01",
            "you think this is just a bit too hasty?!\x02\x03",

            "It might just be, um, a malfunction\x01",
            "of the camera! Yeah!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 200, -1, -1)
    SetChrName("Dorothy")

    AnonymousTalk(    #191
        (
            "#150FNnnoooooo, I don't think it's the camera's fault.\x02\x03",

            "#151FIt's a shiny, brand new model from\x01",
            "the central factory, and I've been\x01",
            "taking reeeeeeally good care of it!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #192
        (
            "#1019FIt's a MALFUNCTION, okay?!\x01",
            "MAL. FUNC. TION.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 200, -1, -1)
    SetChrName("Dorothy")

    AnonymousTalk(    #193
        "#154FWaaah, Estelle, you're scary all of a sudden...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #194
        0x8,
        (
            "#654FAnyway. I'm willing to put a lot more\x01",
            "faith in these sightings now.\x01",
            "It seems something really IS out there.\x02\x03",

            "#652FMore to the point, I think working\x01",
            "with the media on this wouldn't be\x01",
            "a bad idea at this juncture.\x02\x03",

            "So let's all share information.\x01",
            "To start with, did you guys get\x01",
            "statements from the witnesses?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        "#1015F#3PUh, yeah... We checked with all thr--\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xE, 200, -500, 37500, 0)

    NpcTalk(    #196
        0xE,
        "Man's Voice",
        (
            "#2POh, crap, oh, crap!\x01",
            "This is an emergency! Help!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_7254():

        label("loc_7254")

        TurnDirection(0x101, 0xE, 400)
        OP_48()
        Jump("loc_7254")

    QueueWorkItem2(0x101, 1, lambda_7254)

    def lambda_7265():

        label("loc_7265")

        TurnDirection(0xF7, 0xE, 400)
        OP_48()
        Jump("loc_7265")

    QueueWorkItem2(0xF7, 1, lambda_7265)

    def lambda_7276():

        label("loc_7276")

        TurnDirection(0xC, 0xE, 400)
        OP_48()
        Jump("loc_7276")

    QueueWorkItem2(0xC, 1, lambda_7276)

    def lambda_7287():

        label("loc_7287")

        TurnDirection(0xD, 0xE, 400)
        OP_48()
        Jump("loc_7287")

    QueueWorkItem2(0xD, 1, lambda_7287)

    def lambda_7298():

        label("loc_7298")

        TurnDirection(0x8, 0xE, 400)
        OP_48()
        Jump("loc_7298")

    QueueWorkItem2(0x8, 1, lambda_7298)

    def lambda_72A9():
        OP_6D(-3020, 0, 43600, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_72A9)

    def lambda_72C1():
        OP_67(0, 6260, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_72C1)
    Sleep(500)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xE, 0x80)

    def lambda_72EE():
        OP_8E(0xFE, 0x0, 0x0, 0x9916, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_72EE)

    def lambda_7309():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7309)
    WaitChrThread(0xE, 0x0)

    def lambda_7320():
        OP_8E(0xFE, 0xFFFFF51A, 0x0, 0xA316, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_7320)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xE, 0x1)
    TurnDirection(0xE, 0x101, 400)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0x8, 0x1)

    ChrTalk(    #197
        0x101,
        (
            "#1004F#6PH-Hey, what's wrong?\x01",
            "Why are you so worked up?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_73CA")

    ChrTalk(    #198
        0x106,
        "#054F#4PIs it a robbery?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_73FA")

    label("loc_73CA")


    ChrTalk(    #199
        0x103,
        "#024F#4PWas someone attacked by monsters?!\x02",
    )

    CloseMessageWindow()

    label("loc_73FA")


    ChrTalk(    #200
        0xE,
        "#6PNo, no!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xE,
        (
            "#6PThe supporters of Norman and\x01",
            "Portos are arguing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xE,
        (
            "#6PThey're facing one another down\x01",
            "on the Langland Bridge!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #203
        0x101,
        "#1005F#6PAll that fuss over an argument?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7525")

    ChrTalk(    #204
        0x106,
        (
            "#057F#4PHold up. Those are the mayoral\x01",
            "candidates, right? Friggin'...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_758F")

    label("loc_7525")


    ChrTalk(    #205
        0x103,
        (
            "#022F#4PWait. Those are the two mayoral candidates,\x01",
            "aren't they? An 'argument' could be...bad, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_758F")


    ChrTalk(    #206
        0xC,
        (
            "#141F#6POh ho! This sounds like an\x01",
            "article...and maybe a riot!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 90, 400)

    ChrTalk(    #207
        0xC,
        "#144F#6PDorothy, we're on!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xD,
        "#151F#4PAye, aye, sir!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 600)
    TurnDirection(0x101, 0xC, 600)
    TurnDirection(0xF7, 0xC, 600)

    ChrTalk(    #209
        0xD,
        "#150F#4PSee you later, Estelle!\x02",
    )

    CloseMessageWindow()

    def lambda_7656():
        OP_6D(-1770, 0, 42260, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7656)

    def lambda_766E():
        OP_67(0, 6260, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_766E)
    TurnDirection(0xC, 0x101, 600)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0xC, 0x1, 0x0, 0xF)

    def lambda_76A6():
        OP_91(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76A6)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_76D8():
        OP_91(0xFE, 0x12C, 0x0, 0x12C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_76D8)

    def lambda_76F3():

        label("loc_76F3")

        TurnDirection(0x101, 0xC, 0)
        OP_48()
        Jump("loc_76F3")

    QueueWorkItem2(0x101, 2, lambda_76F3)

    def lambda_7704():

        label("loc_7704")

        TurnDirection(0xF7, 0xC, 0)
        OP_48()
        Jump("loc_7704")

    QueueWorkItem2(0xF7, 2, lambda_7704)
    OP_43(0xD, 0x1, 0x0, 0x10)
    WaitChrThread(0xD, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0xF7, 0x2)

    def lambda_7729():
        OP_6D(-3750, 0, 44170, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7729)

    def lambda_7741():
        OP_67(0, 6260, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7741)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #210
        0x101,
        "#1019F#6PM-Man, they're fast...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)

    def lambda_778F():
        OP_8F(0xFE, 0xFFFFF6DC, 0x0, 0xAAF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_778F)
    WaitChrThread(0xF7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7818")

    ChrTalk(    #211
        0x106,
        (
            "#057F#4PWe should get moving too.\x02\x03",

            "If that thing turns into a damn\x01",
            "riot, we need to be on hand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7897")

    label("loc_7818")


    ChrTalk(    #212
        0x103,
        (
            "#022F#4PWe should be quick, too, to be honest.\x02\x03",

            "We need to be on hand in case things\x01",
            "escalate...beyond words, as it were.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7897")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #213
        0x101,
        "#1002F#6PR-Right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x8,
        "#652F#6PThanks, you two. Good luck!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 105, 400)
    OP_4B(0x8, 255)
    OP_4B(0xE, 255)
    OP_43(0xE, 0x0, 0x6, 0x2)
    OP_A2(0x121C)
    OP_28(0x82, 0x1, 0x800)
    EventEnd(0x0)
    Return()

    # Function_12_65EA end

    def Function_13_7900(): pass

    label("Function_13_7900")

    OP_8E(0xFE, 0xFFFFF434, 0x0, 0xAA50, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xD, 400)
    Return()

    # Function_13_7900 end

    def Function_14_791C(): pass

    label("Function_14_791C")

    Sleep(500)
    OP_8E(0xFE, 0xFFFFF8D0, 0x0, 0xAA50, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xC, 400)
    Return()

    # Function_14_791C end

    def Function_15_793D(): pass

    label("Function_15_793D")

    OP_8F(0xFE, 0xFFFFFFEC, 0xFFFFFE0C, 0x95CE, 0x1388, 0x0)

    def lambda_7957():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7957)
    OP_8F(0xFE, 0x5A, 0xFFFFFE0C, 0x927C, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_15_793D end

    def Function_16_797D(): pass

    label("Function_16_797D")

    Sleep(500)
    OP_8C(0xFE, 180, 0)
    OP_8F(0xFE, 0xFFFFF63C, 0x0, 0xAD34, 0x1388, 0x0)
    OP_8F(0xFE, 0xFFFFFFEC, 0xFFFFFE0C, 0x95CE, 0x1388, 0x0)

    def lambda_79B7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_79B7)
    OP_8F(0xFE, 0x5A, 0xFFFFFE0C, 0x927C, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_16_797D end

    def Function_17_79DD(): pass

    label("Function_17_79DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_79EE")
    Call(0, 29)

    label("loc_79EE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_4A(0x8, 255)
    SetChrPos(0x101, -3540, 0, 45030, 90)
    SetChrPos(0xF7, -3550, 0, 46010, 125)
    SetChrPos(0x104, -2090, 0, 45270, 268)
    SetChrPos(0xC, -3440, 0, 43970, 44)
    SetChrPos(0xD, -2380, 0, 44040, 10)
    OP_6D(460, 0, 37310, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(2000)

    def lambda_7AAA():
        OP_6D(-3150, 0, 45370, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7AAA)

    def lambda_7AC2():
        OP_67(0, 8000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7AC2)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #215
        0x104,
        (
            "#034FHow fickle you can be, my rose!\x02\x03",

            "To meet your fated partner again after\x01",
            "such a long absence, and then to\x01",
            "abandon him! What cruel barbs you cast!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7C50")

    ChrTalk(    #216
        0x101,
        (
            "#1007F#6PHa! 'Fated partner,' my left Strega!\x02\x03",

            "#1019FWhat in the Goddess' name are you\x01",
            "DOING in Ruan, anyway, Olivier?\x02\x03",

            "Aren't you supposed to be turning into\x01",
            "a prune in Elmo's hot springs?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D18")

    label("loc_7C50")


    ChrTalk(    #217
        0x101,
        (
            "#1007F#6PHa! 'Fated partner,' my left Strega!\x02\x03",

            "#1019FWhat in the Goddess' name are you\x01",
            "DOING in Ruan, anyway, Olivier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x103,
        (
            "#020F#6PI thought you were wiling the days\x01",
            "away in Elmo's hot springs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D18")


    ChrTalk(    #219
        0x104,
        (
            "#030FMueller contacted me at the Maple Leaf Inn,\x01",
            "you see.\x02\x03",

            "He was kind enough to tell me that you'd returned\x01",
            "from your travails, Estelle.\x02\x03",

            "#031FAnd I thought to myself, 'She has been deprived of\x01",
            "my person for so long. Her happiness is imperiled!\x01",
            "I must welcome her back!' and flew here posthaste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        (
            "#1007F#6PIt certainly feels 'imperiled' now...\x02\x03",

            "#1017FStill...I haven't seen you since the\x01",
            "queen's birthday celebrations.\x02\x03",

            "Thanks for your help back there,\x01",
            "Olivier. It IS nice to see you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x104,
        (
            "#033FTruly...?\x02\x03",

            "#032FAh, but your honesty makes it\x01",
            "difficult for me to stay focused.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #222
        0x104,
        (
            "#037FWhen you don't take the opening to\x01",
            "make a joke at my expense, it leaves\x01",
            "me...wanting something more.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #223
        0x101,
        (
            "#1014F#6P#3SLet's see you deliver another line\x01",
            "like that through broken teeth!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #224
        0x101,
        "#1019F#6P...Whatever.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #225
        0x101,
        (
            "#1007F#6PJean, this THING is Olivier, one of the\x01",
            "people who helped us during the coup.\x02\x03",

            "He's a musician from Erebonia. We think.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #226
        0x8,
        (
            "#650FAh, nice to meet you!\x01",
            "You seem like an...interesting person!\x02\x03",

            "So I'm guessing you don't mind\x01",
            "if we let him in on this, then?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_832F")
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(    #227
        0x106,
        (
            "#552F#4PNormally I'd want to kick him out\x01",
            "on his butt for being an outsider...\x02\x03",

            "I doubt he'd even listen, though.\x01",
            "Just try not to make eye contact.\x01",
            "Maybe he'll go away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x104,
        (
            "#031FHa ha! Oh, Agate!\x02\x03",

            "Truly, you are intimately acquainted\x01",
            "with my ways!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x104, 400)

    ChrTalk(    #229
        0x106,
        (
            "#055F#6PHey, stop trying to imply things!\x02\x03",

            "We've never even talked much!\x01",
            "We just fought on the same side\x01",
            "for a little while!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8435")

    label("loc_832F")

    TurnDirection(0x103, 0x8, 400)

    ChrTalk(    #230
        0x103,
        (
            "#020F#4PYes, I don't mind.\x02\x03",

            "I doubt he'll listen if we tell\x01",
            "him to leave, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x104,
        (
            "#031FHa ha! Oh, Schera!\x02\x03",

            "Truly, you know all there\x01",
            "is to know about me.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 400)

    ChrTalk(    #232
        0x103,
        (
            "#027F#6PYour personal history, not quite,\x01",
            "but your personality? Oh, yes, I do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8435")


    ChrTalk(    #233
        0x101,
        "#1019F#6PANYWAY. Going beyond that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x8,
        "#651FYes, that sounds like a very good idea.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 0, 300)

    ChrTalk(    #235
        0xC,
        (
            "#142FSeriously, we have a story to\x01",
            "talk about, here.\x02\x03",

            "We don't have all day, either.\x01",
            "Dorothy and I need to get the\x01",
            "scoop on the election.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)

    def lambda_8533():
        TurnDirection(0xF7, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_8533)

    def lambda_8541():
        TurnDirection(0x8, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8541)

    def lambda_854F():
        TurnDirection(0x104, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_854F)

    def lambda_855D():
        TurnDirection(0xD, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_855D)

    ChrTalk(    #236
        0x101,
        (
            "#1007F#4PRight, right, I get it.\x02\x03",

            "#1002FSo. This is what the witnesses had to say...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #237
        (
            "\x07\x05Estelle relayed the witnesses' testimonies\x01",
            "and Kevin's analysis of the situation.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #238
        0x8,
        (
            "#650FI see... You managed to gather a\x01",
            "lot of detailed information.\x02\x03",

            "It's enough to see that something\x01",
            "is definitely up, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        "#1015F#6PReally? I thought a lot of it was kind of vague...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xC,
        (
            "#141FWell, the possibility of it being a prank\x01",
            "from the mayoral candidates to cause\x01",
            "problems for the other is out, for one.\x02\x03",

            "Scaring Norman's kid is one thing,\x01",
            "but I kind of doubt they'd waste\x01",
            "time scaring guards or orphans.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_888D")

    ChrTalk(    #241
        0x106,
        (
            "#050F#4PAlso, whatever this 'ghost' is, it can fly.\x01",
            "That was consistent across every report.\x02\x03",

            "That's not something Joe Average\x01",
            "could pull off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_893D")

    label("loc_888D")


    ChrTalk(    #242
        0x103,
        (
            "#022F#4PAlso, the reports were consistent.\x01",
            "The ghost was seen flying in every case.\x02\x03",

            "That's the kind of trick I doubt the\x01",
            "average man on the street could\x01",
            "pull off easily.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_893D")

    OP_62(0xD, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #243
        0xD,
        (
            "#151F#6PWell, then, it must be a real ghost!\x02\x03",

            "Maybe some ancient noble went crazy\x01",
            "and was locked up in a lonely cell,\x01",
            "and forced to wear a mask...FOOOREVER!\x02\x03",

            "And then, after hundreds of years,\x01",
            "he revived as a spooooooky ghooooul! ♪\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(    #244
        0x101,
        (
            "#1019F#6PP-Please stop talking about such scary\x01",
            "ideas with a happy face, thanks!\x02\x03",

            "#1015FBesides...ghosts are supposed to\x01",
            "be bound to people or places.\x02\x03",

            "So it really CAN'T be a ghost, can it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #245
        0x104,
        "#035F...Hmm. Not necessarily.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)

    def lambda_8B81():
        TurnDirection(0xF7, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_8B81)

    def lambda_8B8F():
        TurnDirection(0x8, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8B8F)

    def lambda_8B9D():
        TurnDirection(0xC, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8B9D)

    def lambda_8BAB():
        TurnDirection(0xD, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8BAB)

    ChrTalk(    #246
        0x101,
        "#1004F#6PWh-What do you mean, Olivier?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8C0C")

    ChrTalk(    #247
        0x106,
        "#052F#6PYou notice something?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C37")

    label("loc_8C0C")


    ChrTalk(    #248
        0x103,
        "#023F#6POh, did you notice something?\x02",
    )

    CloseMessageWindow()

    label("loc_8C37")


    ChrTalk(    #249
        0x104,
        (
            "#030FWell, I cannot weigh in on the matter of\x01",
            "our fugitive's ghostliness. However...\x02\x03",

            "Estelle's reports featured several\x01",
            "common points.\x02\x03",

            "From what she said, I think it's actually\x01",
            "quite possible our specter IS bound\x01",
            "to a place or person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x8,
        (
            "#650FOh, you're sharper than I thought.\x02\x03",

            "#651FI was about to say the same thing, actually!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x104,
        (
            "#031FHeh, indeed.\x02\x03",

            "#030FAs a wandering hunter of love, I must keep\x01",
            "a map of Liberl handy at all times.\x02\x03",

            "Let us use my map to look at Estelle's\x01",
            "sightings from a geographical perspective.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS133._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS200._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS201._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS202._CH")
    OP_C5(0x4, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS203._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #252
        (
            "#032FNow, then. Estelle, you investigated\x01",
            "three areas, I believe.\x02\x03",

            "Here, here, and...here, yes?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #253
        (
            "#1015FThat's right...\x02\x03",

            "The Ruan Warehouse District, the Air-Letten\x01",
            "Checkpoint, and the Mercia Orphanage.\x02\x03",

            "What about them?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #254
        (
            "#035FIf we look over the testimonies for differences,\x01",
            "one particular point stands out.\x02\x03",

            "#030FEstelle. I don't suppose you see it\x01",
            "yourself, now, looking at the map?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #255
        (
            "#1002FThe point that was obviously different\x01",
            "with all three testimonies...\x02\x03",

            "#1004FWait, that'd be...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #256
        (
            "\x18\x07\x05What is the point that is obviously different\x01",
            "between all three testimonies?\x02",
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "When The White Shadow Appeared\x01",      # 0
            "Where The White Shadow Went\x01",         # 1
            "What The White Shadow Did\x01",           # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_92B2"),
        (1, "loc_9480"),
        (2, "loc_94DC"),
        (SWITCH_DEFAULT, "loc_9654"),
    )


    label("loc_92B2")

    OP_2B(0x82, 0x1)
    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #257
        (
            "\x07\x00#030FWell, it's true that the child at the\x01",
            "orphanage saw it after dinner, while\x01",
            "the other two saw it at midnight...\x02\x03",

            "All of those effectively fall under the banner\x01",
            "of 'night,' however, so I think we can call it\x01",
            "close enough to not be a difference.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #258
        "\x07\x00#1007FOh, true...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 50, -1, -1)
    SetChrName("Jean")

    AnonymousTalk(    #259
        (
            "\x07\x00#651FThen allow me.\x02\x03",

            "#650FThe difference lies in where the\x01",
            "ghost went, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #260
        "\x07\x00#1004FAh...!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_9654")

    label("loc_9480")

    OP_2B(0x82, 0x3)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #261
        (
            "\x07\x00#1018FI've got it! It's where the ghost\x01",
            "went that matters!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_9654")

    label("loc_94DC")

    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #262
        (
            "\x07\x00#030FNo, many of the testimonies overlap\x01",
            "on what it did.\x02\x03",

            "The only exception is bowing to the orphan...\x02\x03",

            "Aside from that, the ghost always\x01",
            "dances about in the air.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #263
        "\x07\x00#1007FThat's true...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 50, -1, -1)
    SetChrName("Jean")

    AnonymousTalk(    #264
        (
            "\x07\x00#651FThen allow me.\x02\x03",

            "#650FThe difference lies in where the\x01",
            "ghost went, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #265
        "\x07\x00#1004FAh...!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_9654")

    label("loc_9654")

    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #266
        (
            "\x07\x00#031FPrecisely.\x02\x03",

            "#030FOur Raven-feathered tough man in the city's\x01",
            "southern block said it went northeast...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #267
        "\x07\x00#030FOur Air-Letten guardsman said it went north...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #268
        (
            "\x07\x00#035FAnd our young orphan said the white\x01",
            "shadow went east.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x4, 0x4, 0, 0, 0)
    OP_C6(0x4, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #269
        "\x07\x00#1004F#4SWHA?!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9859")
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #270
        (
            "#051FHeh, now I get it.\x01",
            "Never woulda figured...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_98A0")

    label("loc_9859")

    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #271
        (
            "#020FNow I see.\x01",
            "I never would've imagined...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_98A0")

    SetMessageWindowPos(200, 320, -1, -1)
    SetChrName("Nial")

    AnonymousTalk(    #272
        (
            "#141FThat's pretty conclusive, yeah.\x02\x03",

            "When you look at it like that, not many\x01",
            "other places it can come from, really.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #273
        (
            "#031FExactly my point.\x02\x03",

            "#030FJenis Royal Academy... It MUST be around there.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x3, 0x3, 16777215, 0, 0)
    OP_C6(0x4, 0x3, 16777215, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    OP_C6(0x2, 0x6, 0, 0, 0)
    OP_C6(0x3, 0x6, 0, 0, 0)
    OP_C6(0x4, 0x6, 0, 0, 0)

    ChrTalk(    #274
        0x101,
        (
            "#1001F#6POlivier...you're pretty clever!\x02\x03",

            "#1006FOkay, I don't care if it's a\x01",
            "ghost or a whatever.\x02\x03",

            "We're gonna go to the academy\x01",
            "and find out just what it is!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9B1A")
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(    #275
        0x106,
        "#051F#4PHm... Jean, it's cool, yeah?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9B66")

    label("loc_9B1A")

    TurnDirection(0x103, 0x8, 400)

    ChrTalk(    #276
        0x103,
        (
            "#020F#4PJean, I assume we have permission\x01",
            "to enter the academy?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B66")


    ChrTalk(    #277
        0x8,
        (
            "#650FAbsolutely. I'll phone ahead.\x01",
            "Go on over and investigate. See if\x01",
            "you can get to the bottom of all this.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xC, 400)
    Sleep(500)

    ChrTalk(    #278
        0x8,
        (
            "#650FI do have to wonder if our reporter\x01",
            "friends have any plans, however.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9C39():
        TurnDirection(0x101, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C39)

    def lambda_9C47():
        TurnDirection(0xF7, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_9C47)

    def lambda_9C55():
        TurnDirection(0x104, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9C55)

    def lambda_9C63():
        TurnDirection(0xD, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_9C63)

    ChrTalk(    #279
        0xC,
        (
            "#145FHrrrmmm... Really can't afford to\x01",
            "cut out on the election...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 400)
    Sleep(500)

    ChrTalk(    #280
        0xC,
        (
            "#141F#6POkay. Dorothy?\x01",
            "I'll leave this in your hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xD,
        (
            "#151F#2PYes, SIR!\x02\x03",

            "I'll do some REAL ghost hunting!\x01",
            "I'll get tons of pictures!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xC,
        (
            "#144F#6PNO! Help solve the damn mystery!\x02\x03",

            "You follow Estelle and take pictures\x01",
            "relating to this ghost mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xD,
        (
            "#153F#2POh, okaaay.\x02\x03",

            "#151FI don't really get it, but I'll do my best!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x101,
        "#1019F#4PEr, hey, we didn't actually agree to this part...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #285
        0x8,
        (
            "#651FNow, now.\x02\x03",

            "They did get us that photograph,\x01",
            "so let's help them out in return,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9EF0")

    ChrTalk(    #286
        0x106,
        (
            "#552F#4PRight, fine.\x01",
            "The camera girl can come too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F1F")

    label("loc_9EF0")


    ChrTalk(    #287
        0x103,
        "#021F#4PI think it'll be okay, don't you?\x02",
    )

    CloseMessageWindow()

    label("loc_9F1F")


    ChrTalk(    #288
        0x101,
        (
            "#1007F#4P*sigh* Kinda feels like this'll eat away at any\x01",
            "seriousness the situation might've had...\x02\x03",

            "#1017FStill, Dorothy probably can help us out, so...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #289
        0xC,
        (
            "#141FThat's settled, then.\x01",
            "I'm counting on you guys!\x02\x03",

            "If you'll excuse me, I have a couple\x01",
            "of mayoral candidates to interview.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 135, 400)

    def lambda_A055():

        label("loc_A055")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_A055")

    QueueWorkItem2(0x101, 1, lambda_A055)

    def lambda_A066():

        label("loc_A066")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_A066")

    QueueWorkItem2(0xF7, 1, lambda_A066)

    def lambda_A077():

        label("loc_A077")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_A077")

    QueueWorkItem2(0x104, 1, lambda_A077)

    def lambda_A088():

        label("loc_A088")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_A088")

    QueueWorkItem2(0xD, 1, lambda_A088)

    def lambda_A099():

        label("loc_A099")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_A099")

    QueueWorkItem2(0x8, 1, lambda_A099)

    def lambda_A0AA():
        OP_8E(0xFE, 0xFFFFFB1E, 0x0, 0xA0FA, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A0AA)
    Sleep(700)

    def lambda_A0CA():
        OP_8E(0xFE, 0xFFFFFB1E, 0x0, 0xA0FA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A0CA)

    def lambda_A0E5():
        OP_6D(-2280, 0, 44400, 1000)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_A0E5)
    WaitChrThread(0xC, 0x1)

    ChrTalk(    #290
        0xC,
        "#143FOh...before that, though. Estelle.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)
    Sleep(500)

    ChrTalk(    #291
        0xC,
        (
            "#140FYour dad...told me a little bit about\x01",
            "the Joshua thing. Not a lot...but\x01",
            "enough for me to get the picture.\x02\x03",

            "I know you're worried about...\x01",
            "uh, 'those people'...\x02\x03",

            "If I hear anything that might be related,\x01",
            "I'll forward it to the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x101,
        "#1004F#4PWha... Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xC,
        (
            "#144FSo, uh, yeah, keep a stiff upper lip!\x01",
            "Or, uh, something...\x02\x03",

            "Anyway, gotta go!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 135, 600)

    def lambda_A2A9():
        OP_6D(-1770, 0, 42260, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A2A9)

    def lambda_A2C1():
        OP_8E(0xFE, 0x96, 0x0, 0x9A1A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A2C1)
    WaitChrThread(0xC, 0x1)

    def lambda_A2E1():
        OP_8E(0xFE, 0x19A, 0xFFFFFE0C, 0x9114, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A2E1)
    Sleep(200)

    def lambda_A301():
        OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_A301)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xC, 0x1)
    Sleep(500)
    OP_6D(-3790, 0, 46180, 1500)
    SetChrFlags(0xC, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0xF7, 0xFF)
    OP_44(0x104, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0x8, 0xFF)

    ChrTalk(    #294
        0x101,
        "#1025F#6PNial...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xD,
        "#151F#5PAwwwwww, Nial's embarrassed!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #296
        0xD,
        (
            "#150F#5PIt was a really big shock when he heard\x01",
            "about it all from Cassius, I think.\x02\x03",

            "I think he's really been looking\x01",
            "for a way to help you, Estelle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x101,
        (
            "#1008F#6PR-Really...?\x02\x03",

            "#1016FOh, if only he could be a little\x01",
            "more honest, it'd be sweet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xD,
        (
            "#150F#5PI'll make sure to contact the guild, too,\x01",
            "if I take any more neato photographs\x01",
            "of weird people!\x02\x03",

            "#151FSo, Estelle, fight on! Yeah!\x01",
            "Or...something!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        (
            "#1012F#6PThanks, Dorothy.\x02\x03",

            "#1018FAnyway, off to the royal academy!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 400)

    ChrTalk(    #300
        0x8,
        (
            "#650FLike I said, I'll call ahead and\x01",
            "let them know to let you in.\x02\x03",

            "Good luck, guys!\x01",
            "We're counting on you!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    OP_A2(0x121D)
    NewScene("ED6_DT21/T2100   ._SN", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_17_79DD end

    def Function_18_A609(): pass

    label("Function_18_A609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A61A")
    Call(0, 29)

    label("loc_A61A")

    EventBegin(0x0)
    OP_1D(0xC)
    SetChrPos(0x101, -3540, 0, 46000, 270)
    SetChrPos(0xF7, -2470, 0, 45400, 270)
    SetChrPos(0x104, -2720, 0, 44400, 270)
    SetChrPos(0x105, -3540, 0, 43930, 315)
    OP_6D(-4410, 0, 45930, 0)
    OP_67(0, 6720, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_4A(0x8, 255)
    FadeToBright(2000, 0)
    OP_0D()
    OP_28(0x84, 0x1, 0x40)
    OP_28(0x84, 0x1, 0x80)
    OP_28(0x84, 0x1, 0x100)
    OP_28(0x84, 0x1, 0x200)

    ChrTalk(    #301
        0x8,
        (
            "#652F#6PI see... Good work, all of you.\x02\x03",

            "#655FThe 'Society of Ouroboros'...\x02\x03",

            "To be honest, I only half-believed Cassius\x01",
            "when he told me about a secret society\x01",
            "up to no good. But...\x02\x03",

            "#652FWell. Here's the reward for completing\x01",
            "the investigation.\x02\x03",

            "Sure didn't expect it to turn\x01",
            "out like this, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x82, 0x4, 0x10)
    OP_AF(0x67, 0x82)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x83, 0x4, 0x10)
    OP_28(0x83, 0x4, 0x20)
    OP_28(0x84, 0x4, 0x10)
    OP_28(0x84, 0x4, 0x20)

    ChrTalk(    #302
        0x8,
        (
            "#652FI'll have the results forwarded to\x01",
            "Cass--er, Brigadier General Bright and the\x01",
            "rest of the army immediately.\x02\x03",

            "I get the impression they're desperate\x01",
            "for information, too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A9D0")

    ChrTalk(    #303
        0x106,
        (
            "#050FYeah, please do.\x02\x03",

            "If those chucklenuts can make something like\x01",
            "that holo...whatever thing, Ouroboros is\x01",
            "capable of more than we ever dreamed of.\x02\x03",

            "Not to mention whippin' out another 'Gospel'\x01",
            "like it's a friggin' toy or something...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAD1")

    label("loc_A9D0")


    ChrTalk(    #304
        0x103,
        (
            "#022FYes, please do so.\x02\x03",

            "If Ouroboros can produce something like that...\x01",
            "holographic projector, was it? They're far\x01",
            "more capable than we even thought possible.\x02\x03",

            "Never mind producing another 'Gospel'\x01",
            "as casually as most people obtain a\x01",
            "pair of shoes...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AAD1")


    ChrTalk(    #305
        0x104,
        (
            "#030FThe real objective seems to have\x01",
            "been performing experiments with\x01",
            "that new Gospel.\x02\x03",

            "The fuss about the 'ghost' was little more\x01",
            "than the whim of the man in charge, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x101,
        (
            "#1002F#4PBleublanc the Phantom Thief...\x02\x03",

            "He called himself 'Enforcer No. X.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x8,
        (
            "#652F#6PIf I had to hazard a guess, 'Enforcer'\x01",
            "is probably a title for ranking agents\x01",
            "in the society.\x02\x03",

            "I'd put money on the man we know as\x01",
            "'Lieutenant Lorence' being another one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x101,
        "#1003F#4P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #309
        0x105,
        "#043F#5PUm, Estelle...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)
    Sleep(400)

    ChrTalk(    #310
        0x101,
        (
            "#1007F#6PYeah... I know.\x02\x03",

            "#1003FThe 'Black Fang'...\x02\x03",

            "That's what Joshua called himself,\x01",
            "that night he...disappeared.\x02\x03",

            "#1025FJoshua was also an 'Enforcer,' I bet...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_AE77")

    ChrTalk(    #311
        0x106,
        (
            "#053FI thought so...\x02\x03",

            "If he's just like that Phantom Fool,\x01",
            "all those weirdly specialized skills he\x01",
            "seemed to have make a lot more sense.\x02\x03",

            "#552FI'm guessing he was hiding what he\x01",
            "was truly capable of the whole time\x01",
            "he was with us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF6E")

    label("loc_AE77")


    ChrTalk(    #312
        0x103,
        (
            "#025FI always suspected there was...more\x01",
            "to him, from the moment we first met.\x02\x03",

            "But given his age, I never thought\x01",
            "he'd be able to match someone\x01",
            "like that Phantom Thief.\x02\x03",

            "#522FSomehow, I doubt he ever showed\x01",
            "us what he was really capable of.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF6E")


    ChrTalk(    #313
        0x101,
        "#1003F#6PYeah... Maybe...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #314
        0x101,
        "#1002F#4P...Hey, Jean.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x8,
        "#653F#6PWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x101,
        (
            "#1002F#4PThat Phantom Thief guy said the\x01",
            "society's plans had only just begun.\x02\x03",

            "I think they've got plots and\x01",
            "stuff in motion all over Liberl...\x02\x03",

            "Have you heard anything from the\x01",
            "other branches? Anything weird?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x8,
        (
            "#654F#6PHmmmmm... Nothing that stands out.\x02\x03",

            "#652FI bet you're right, though.\x01",
            "They're starting to act in\x01",
            "the shadows all over Liberl.\x02\x03",

            "Given that our little ghost fuss\x01",
            "is over, it might be wise for\x01",
            "you to head somewhere else.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_B1E7")

    ChrTalk(    #318
        0x106,
        (
            "#051FYeah, good thinking.\x02\x03",

            "Don't suppose any other branches\x01",
            "need help in general?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B272")

    label("loc_B1E7")


    ChrTalk(    #319
        0x103,
        (
            "#020FYes, I was just thinking that myself.\x02\x03",

            "Are any of the other branches looking\x01",
            "a little strained, potential society\x01",
            "trouble aside?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B272")


    ChrTalk(    #320
        0x8,
        (
            "#650F#6PI guess the Zeiss branch, sort of.\x02\x03",

            "Their standby, Gundolf, had to\x01",
            "head to Grancel.\x02\x03",

            "It sounds like they're fairly\x01",
            "undermanned at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x101,
        (
            "#1006F#4POkay, then! We should head\x01",
            "out there and help them.\x02\x03",

            "Will Ruan be all right, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x8,
        (
            "#651F#6PThe Bose branch is dispatching Sting\x01",
            "to help us out in a few days.\x02\x03",

            "Melvin and I will be able to hold the fort\x01",
            "until Sting gets here, I think.\x02\x03",

            "#650FOh, and once you get to Zeiss, you may\x01",
            "want to check in with Professor Russell.\x02\x03",

            "He might have an insight on the\x01",
            "new Gospel you guys observed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x101,
        (
            "#1006F#4PYeah, that's a good idea.\x02\x03",

            "I totally wanna see Tita again, anyway,\x01",
            "so I'll head over to his place right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x104,
        (
            "#031FWell, then. We should head for the airship port\x01",
            "as soon as our preparations are complete.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x8, 400)
    Sleep(500)

    ChrTalk(    #325
        0x104,
        (
            "#030FJean. If you would be so kind as to prepare\x01",
            "four tickets for the Zeiss-bound flight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x8,
        "#653F#6PPardon...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #327
        0x101,
        "#1019F#6PWhere do you get off taking the lead and...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #328
        0x101,
        "#1004F#6PHold on, FOUR?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_B769")

    ChrTalk(    #329
        0x104,
        (
            "#035FWell, naturally. You and Agate...\x02\x03",

            "#030F...and then myself and Miss\x01",
            "Kloe, here, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x101,
        "#1005F#6PWH-WH-WHAAAAT?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x104, 400)
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #331
        0x106,
        (
            "#552F#2PI thought this might come up,\x01",
            "but...you gonna come with us?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B84F")

    label("loc_B769")


    ChrTalk(    #332
        0x104,
        (
            "#035FWell, naturally. You and Schera...\x02\x03",

            "#030F...and then myself and Miss\x01",
            "Kloe, here, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x101,
        "#1005F#6PWH-WH-WHAAAAT?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 400)
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #334
        0x103,
        (
            "#020F#2PI thought this might come up.\x01",
            "You're certain you wish to\x01",
            "come with us?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B84F")

    TurnDirection(0x104, 0xF7, 400)

    ChrTalk(    #335
        0x104,
        (
            "#031FThe search for Joshua is my mission\x01",
            "as a hunter of love.\x02\x03",

            "Not to mention the matter of my\x01",
            "new rival! That should be reason\x01",
            "enough, I would think.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #336
        0x101,
        (
            "#1019F#6POkay, wait, leaving your total friggin'\x01",
            "insanity aside for a second...\x02\x03",

            "Don't drag Kloe into this too,\x01",
            "you jerk! She doesn't even wa--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x105,
        (
            "#542F#5PNo...\x02\x03",

            "Actually, I was...going to\x01",
            "ask for the same thing.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #338
        0x101,
        "#1004F#6PSay what?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x8, 400)

    ChrTalk(    #339
        0x105,
        (
            "#047F#5PThis malicious, mysterious 'society' is\x01",
            "operating within the borders of Liberl,\x01",
            "plotting who knows what.\x02\x03",

            "As...what I am, I cannot simply ignore\x01",
            "what they are doing. I must act.\x02\x03",

            "#043FBesides...\x02\x03",

            "I want to help Joshua...and you, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x101,
        (
            "#1008F#6PAw, Kloe...\x02\x03",

            "But your classes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x105,
        (
            "#542F#5PThis morning I sent a letter to Dean\x01",
            "Collins, stating that I will be needing\x01",
            "a break from lessons.\x02\x03",

            "My exam scores are excellent, anyway,\x01",
            "and I have all the credits I need to move\x01",
            "on at the end of the year already.\x02\x03",

            "#041FI talked to Jill and Hans about it,\x01",
            "and they insisted I should go...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x101,
        "#1016F#6PWh-What the...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_BEE9")

    ChrTalk(    #343
        0x106,
        (
            "#051F#2PHaha, dang. You don't do things\x01",
            "halfway once you've made up\x01",
            "your mind, huh, Pr--er, Kloe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x105,
        (
            "#540F#5PI-I'm sorry... I suppose I am shoving\x01",
            "myself onto you, in a way.\x02\x03",

            "#043FI...can remain behind, if you'd prefer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x101,
        (
            "#1008F#6PHaha, Oh, no, you don't!\x02\x03",

            "#1018FIf you really want to come,\x01",
            "I'd love to have your help!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #346
        0x101,
        "#1006F#6PAgate, you don't mind, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x106,
        (
            "#051F#2PAh, why the hell not.\x02\x03",

            "Having her skills in orbal arts and\x01",
            "that bird of hers around will help\x01",
            "a lot, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x105,
        (
            "#045F#5PTh-Thank you...\x02\x03",

            "#048FAgate, Estelle...thank you.\x01",
            "I'll give it my all. I swear.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C13D")

    label("loc_BEE9")


    ChrTalk(    #349
        0x103,
        (
            "#027F#2PMy, but you certainly go all in once\x01",
            "your mind is made up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x105,
        (
            "#540F#5PI-I'm sorry... I suppose I am shoving\x01",
            "myself onto you, in a way.\x02\x03",

            "#043FI...can remain behind,\x01",
            "if you'd prefer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x101,
        (
            "#1016F#6PHaha, Oh, no, you don't!\x02\x03",

            "#1018FIf you really want to come,\x01",
            "I'd love to have your help!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #352
        0x101,
        (
            "#1006F#6PYou don't have a problem with it,\x01",
            "right, Schera?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x103,
        (
            "#021F#2PJust the opposite!\x01",
            "I think it's a wonderful idea.\x02\x03",

            "Kloe's skills in orbal arts will\x01",
            "be a great help, as will Sieg.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x105,
        (
            "#045F#5PTh-Thank you...\x02\x03",

            "#048FScherazard, Estelle...thank you.\x01",
            "I'll give it my all. I swear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C13D")

    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #355
        0x101,
        (
            "#1017F#6PWell, we're old friends, after all!\x01",
            "We're the Red and Blue Knights,\x01",
            "remember.\x02\x03",

            "Now let's combine our forces\x01",
            "and find our lost princess!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x105,
        (
            "#542F#5PHaha... That's right...\x02\x03",

            "#041FYes! Lead on, Red Knight!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x104,
        (
            "#035FAh, then this would make me the lone, wandering\x01",
            "prince from a nearby country, here to take back\x01",
            "the dark-haired princess, even if by force...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #358
        0x101,
        "#1005F#6PYou don't get to add roles!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x8,
        (
            "#651F#6PHaha! Well, good to see that's sorted out.\x02\x03",

            "#650FIn that case, though, we should classify\x01",
            "you two as 'temporary assistants.'\x02\x03",

            "That way the guild can pay\x01",
            "expenses for you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 400)

    def lambda_C3AD():
        TurnDirection(0xF7, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_C3AD)

    def lambda_C3BB():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C3BB)

    ChrTalk(    #360
        0x105,
        "#040F#5PYes, please do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x104,
        (
            "#031FWell! I shall assist you with\x01",
            "all my heart. Let us be off!\x02",
        )
    )

    CloseMessageWindow()
    OP_3F(0x3F3, 1)
    OP_3F(0x3F4, 1)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_AD(0x2400AE, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x1241)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x123), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(100000, -100000, 100000, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_EA(0xE, 0x0, 0x0, 0x0)

    Menu(
        0,
        240,
        180,
        0,
        (
            "Save\x01",              # 0
            "Next Chapter\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4B6")
    ShowSaveMenu()

    label("loc_C4B6")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_20(0xBB8)
    OP_AE(0xC8)
    Sleep(2000)
    OP_21()
    OP_A3(0x1241)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("ED6_DT21/T2105   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_A609 end

    def Function_19_C4EF(): pass

    label("Function_19_C4EF")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C506")
    Call(0, 29)
    Call(0, 30)

    label("loc_C506")

    OP_4A(0x8, 255)
    OP_6D(-5760, 0, 45080, 0)
    OP_67(0, 7150, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(315000, 0)
    OP_6E(327, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_8C(0x8, 135, 400)

    ChrTalk(    #362
        0x8,
        "#650F#6PYes, what can I do for--\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #363
        0x8,
        "#653F#6PAh...!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, -550, 0, 39990, 315)
    SetChrPos(0x102, 80, 0, 40550, 315)
    SetChrPos(0xF8, 180, 0, 39140, 315)
    SetChrPos(0xF9, 840, 0, 39800, 315)

    def lambda_C602():
        OP_6D(-5300, 0, 46380, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C602)

    def lambda_C61A():
        OP_67(0, 5620, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C61A)

    def lambda_C632():
        OP_6E(310, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_C632)

    def lambda_C642():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_C642)

    def lambda_C652():

        label("loc_C652")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_C652")

    QueueWorkItem2(0x8, 2, lambda_C652)
    OP_43(0x102, 0x1, 0x0, 0x15)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0x14)
    Sleep(200)
    OP_43(0xF9, 0x1, 0x0, 0x17)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x16)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    OP_44(0x8, 0x2)

    ChrTalk(    #364
        0x101,
        "#1006F#2PHeya, Jean!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x102,
        "#1035FI'm glad to see you're well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x8,
        (
            "#653F#6PEstelle...and...and Joshua!\x02\x03",

            "#656FI see... You're both safe.\x01",
            "Thank Aidios...\x02\x03",

            "All this madness started while you\x01",
            "were at the towers, so I was worried\x01",
            "that something had happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x101,
        "#1016F#2PHaha... Thanks for worrying, Jean.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C880")

    ChrTalk(    #368
        0x103,
        (
            "#021FLast I checked, we managed to\x01",
            "come out of it with most of our \x01",
            "limbs intact. Somehow!\x02\x03",

            "#524FOn a serious note, though...it\x01",
            "looks like Ruan's been hit hard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C8E7")

    label("loc_C880")


    ChrTalk(    #369
        0x102,
        (
            "#1040FWe're all fine, for now, anyway.\x02\x03",

            "#1043FIt seems the same can't be\x01",
            "said for Ruan, though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C8E7")


    ChrTalk(    #370
        0x8,
        (
            "#654F#6PYou've got that right. We're in\x01",
            "a ridiculous mess right now.\x02\x03",

            "The second we saw that massive...\x01",
            "whatever it is above the lake, all\x01",
            "our orbments stopped working.\x02\x03",

            "#652FThe new Mayor, Mr. Norman, is\x01",
            "struggling to keep up with it all.\x02\x03",

            "Honestly, if it weren't for the clergy from\x01",
            "the church and the members of the Ravens\x01",
            "helping, the town'd be a wreck.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB08")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as knew about the Ravens' reform\x01",             # 0
            "Set as didn't know about the Ravens' reform\x01",      # 1
            "No change\x01",                                        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CAFC"),
        (1, "loc_CB02"),
        (SWITCH_DEFAULT, "loc_CB08"),
    )


    label("loc_CAFC")

    OP_A2(0x2080)
    Jump("loc_CB08")

    label("loc_CB02")

    OP_A3(0x2080)
    Jump("loc_CB08")

    label("loc_CB08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 0)), scpexpr(EXPR_END)), "loc_CC25")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CBCA")

    ChrTalk(    #371
        0x101,
        (
            "#1008F#2PI see...\x02\x03",

            "I guess the Ravens really are serious\x01",
            "about turning a new leaf.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x106,
        (
            "#051FThose good for nothin' punks...\x01",
            "Looks like I underestimated all of 'em.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC22")

    label("loc_CBCA")


    ChrTalk(    #373
        0x101,
        (
            "#1008F#2PI see...\x02\x03",

            "I guess the Ravens really are serious\x01",
            "about turning a new leaf.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC22")

    Jump("loc_CE4F")

    label("loc_CC25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC6A")

    ChrTalk(    #374
        0x101,
        "#1019F#2PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x106,
        "#055FThe Ravens are WHAT?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_CCB2")

    label("loc_CC6A")


    ChrTalk(    #376
        0x101,
        (
            "#1004F#2PEr.\x02\x03",

            "#1015FI'm sorry, did you say\x01",
            "the RAVENS are helping?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCB2")


    ChrTalk(    #377
        0x8,
        (
            "#650F#6POh, yes! Right after the orbments stopped working,\x01",
            "when everything really started going to hell,\x01",
            "they stepped in to help keep order.\x02\x03",

            "#651FRight now, we've got them working\x01",
            "as volunteer bracers, temporarily.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2080)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CE07")

    ChrTalk(    #378
        0x106,
        "#555FOh, good grief...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x101,
        (
            "#1006F#2PI get it... So they finally found\x01",
            "the will to do it, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE4F")

    label("loc_CE07")


    ChrTalk(    #380
        0x101,
        (
            "#1006F#2PI get it... So they finally found\x01",
            "the will to do it, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE4F")


    ChrTalk(    #381
        0x8,
        (
            "#654F#6POf course, it's just been one\x01",
            "catastrophe after another.\x02\x03",

            "#652FFor starters, this whole thing just HAD\x01",
            "to happen while Langland Bridge was up.\x01",
            "Naturally.\x02\x03",

            "Thanks to that you can only cross the\x01",
            "river via paddle-boat ferry right now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D03F")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as came from south side\x01",                                    # 0
            "Set as came from north side and saw the boat\x01",                   # 1
            "Set as came from north side and haven't seen the boat yet\x01",      # 2
            "No change\x01",                                                      # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D024"),
        (1, "loc_D02D"),
        (2, "loc_D036"),
        (SWITCH_DEFAULT, "loc_D03F"),
    )


    label("loc_D024")

    OP_A2(0x2035)
    OP_A2(0x2036)
    Jump("loc_D03F")

    label("loc_D02D")

    OP_A2(0x2035)
    OP_A3(0x2036)
    Jump("loc_D03F")

    label("loc_D036")

    OP_A3(0x2035)
    OP_A3(0x2036)
    Jump("loc_D03F")

    label("loc_D03F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_END)), "loc_D0A6")

    ChrTalk(    #382
        0x101,
        (
            "#1015F#2PYeah, we used it to get over here.\x02\x03",

            "#1007FThe wait time was absolutely brutal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D159")

    label("loc_D0A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 5)), scpexpr(EXPR_END)), "loc_D10D")

    ChrTalk(    #383
        0x101,
        (
            "#1015F#2PYeah, we saw the boat dock on our way over.\x02\x03",

            "The wait looks pretty nasty, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D159")

    label("loc_D10D")


    ChrTalk(    #384
        0x101,
        (
            "#1015F#2POh, man... Guess there's no other\x01",
            "way if the bridge is stuck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D159")


    ChrTalk(    #385
        0x8,
        (
            "#652F#6PUltimately, I don't think the city\x01",
            "can keep this up for very long.\x02\x03",

            "I'd like to put some kind of relief plan\x01",
            "together with the other branches and the\x01",
            "army...\x02\x03",

            "#654FBut with the phones not working,\x01",
            "at best we have written mail,\x01",
            "and the roads are a mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x101,
        (
            "#1006F#2PI think we can help on\x01",
            "that front, Jean.\x02\x03",

            "We have just the thing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x8,
        "#653F#6PYou can what? You have what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x102,
        "#1040FLet's get you up to speed.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #389
        (
            "\x07\x05Estelle explained recent events and about\x01",
            "the Zero Field Generator.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #390
        0x8,
        (
            "#652F#6PI get it... Figures that thing has\x01",
            "something to do with the society.\x02\x03",

            "#650FBeing able to use the phone would\x01",
            "be a HUGE help, though!\x02\x03",

            "#651FCould you set that up right now?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D54A")

    ChrTalk(    #391
        0x107,
        "#560FUh-huh!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(1, 9)
    SetChrPos(0x107, -6250, 0, 46860, 270)
    TurnDirection(0x8, 0x107, 0)
    TurnDirection(0x101, 0x107, 0)
    TurnDirection(0x102, 0x107, 0)
    TurnDirection(0xF8, 0x107, 0)
    TurnDirection(0xF9, 0x107, 0)
    OP_6D(-6670, 0, 46850, 0)
    OP_67(0, 5620, -10000, 0)
    OP_6B(2430, 0)
    OP_6C(315000, 0)
    OP_6E(321, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #392
        0x107,
        "#061FOkay, all done!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #393
        "\x07\x05Tita flipped the switch on the phone.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_D67D")

    label("loc_D54A")


    ChrTalk(    #394
        0x102,
        "#1040FYes, give me just a moment.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(1, 9)
    SetChrPos(0x102, -6250, 0, 46860, 270)
    TurnDirection(0x8, 0x102, 0)
    TurnDirection(0x101, 0x102, 0)
    TurnDirection(0xF8, 0x102, 0)
    TurnDirection(0xF9, 0x102, 0)
    OP_6D(-6670, 0, 46850, 0)
    OP_67(0, 5620, -10000, 0)
    OP_6B(2430, 0)
    OP_6C(315000, 0)
    OP_6E(321, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #395
        0x102,
        "#1035FThat should do it, hopefully.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #396
        "\x07\x05Joshua flipped the switch on the phone.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_D67D")

    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x83, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -6670, 1900, 46840, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #397
        0x8,
        "#653F#1PIt works!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D79A")
    OP_8C(0x107, 180, 400)

    ChrTalk(    #398
        0x107,
        (
            "#560F#4PThis phone should work fine now!\x02\x03",

            "You, um, won't be able to call anyone\x01",
            "until their phones work too, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D81B")

    label("loc_D79A")

    OP_8C(0x102, 180, 400)

    ChrTalk(    #399
        0x102,
        (
            "#1040F#4PIt should work now.\x02\x03",

            "You won't be able to make calls\x01",
            "until the receiver's phone is\x01",
            "also functional, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D81B")


    ChrTalk(    #400
        0x8,
        (
            "#656F#1POh, man, this is just what we needed.\x02\x03",

            "Having a working phone is like manna\x01",
            "from Aidios at a time like this!\x02\x03",

            "#651FI could kiss you all AND\x01",
            "Professor Russell right now!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D953")
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #401
        0x107,
        "#067F#4PAwww...!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #402
        0x101,
        (
            "#1016F#2PAhaha... It's, uh, a nice\x01",
            "sentiment, at least!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D997")

    label("loc_D953")

    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #403
        0x101,
        (
            "#1016F#2PAhaha... It's, uh, a nice\x01",
            "sentiment, at least!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA31")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as fixed all phones\x01",      # 0
            "Set as only fixed here\x01",       # 1
            "No change\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DA1F"),
        (1, "loc_DA28"),
        (SWITCH_DEFAULT, "loc_DA31"),
    )


    label("loc_DA1F")

    OP_A2(0x2003)
    OP_A2(0x2005)
    Jump("loc_DA31")

    label("loc_DA28")

    OP_A3(0x2003)
    OP_A3(0x2005)
    Jump("loc_DA31")

    label("loc_DA31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE37")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DB05")
    TurnDirection(0x108, 0x8, 400)

    def lambda_DA57():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DA57)
    Sleep(100)

    def lambda_DA6A():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DA6A)

    ChrTalk(    #404
        0x108,
        (
            "#070FAnd with that, all the phones\x01",
            "should work now.\x02\x03",

            "We should return to the professor\x01",
            "and Captain Schwarz and inform\x01",
            "them of our success.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DC9E")

    label("loc_DB05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DBE1")
    TurnDirection(0x103, 0x8, 400)

    def lambda_DB20():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DB20)
    Sleep(100)

    def lambda_DB33():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DB33)

    ChrTalk(    #405
        0x103,
        (
            "#020FWell, then! That's all the\x01",
            "phones made functional.\x02\x03",

            "We should let Professor Russell and Captain\x01",
            "Schwarz know about our success\x01",
            "and what's been going on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DC9E")

    label("loc_DBE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DC9E")
    TurnDirection(0x106, 0x8, 400)

    def lambda_DBFC():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DBFC)
    Sleep(100)

    def lambda_DC0F():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DC0F)

    ChrTalk(    #406
        0x106,
        (
            "#051FAll right, that's all the phones\x01",
            "workin' again.\x02\x03",

            "We oughtta get back to Gramps and the\x01",
            "captain and let 'em know what's what.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC9E")

    OP_59()
    OP_28(0x9B, 0x4, 0x10)
    OP_AF(0x67, 0x9B)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x9B, 0x1, 0x100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DD2B")
    OP_8C(0x8, 90, 400)

    ChrTalk(    #407
        0x8,
        (
            "#651F#1PYou guys have done great!\x02\x03",

            "I can take care of anything\x01",
            "that comes up now!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD89")

    label("loc_DD2B")

    OP_8C(0x8, 90, 400)

    ChrTalk(    #408
        0x8,
        (
            "#651F#1PYou guys have done great!\x02\x03",

            "I can take care of anything\x01",
            "that comes up now!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD89")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DDCD")

    ChrTalk(    #409
        0x108,
        (
            "#070FIs there anything else\x01",
            "we can help with?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE34")

    label("loc_DDCD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DE08")

    ChrTalk(    #410
        0x103,
        "#020FNeed a hand with anything else?\x02",
    )

    CloseMessageWindow()
    Jump("loc_DE34")

    label("loc_DE08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DE34")

    ChrTalk(    #411
        0x106,
        "#051FNeed anything else?\x02",
    )

    CloseMessageWindow()

    label("loc_DE34")

    Jump("loc_E05F")

    label("loc_DE37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DEF2")
    TurnDirection(0x108, 0x8, 400)

    def lambda_DE52():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DE52)
    Sleep(100)

    def lambda_DE65():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DE65)

    ChrTalk(    #412
        0x108,
        (
            "#070FWe must depart soon to assist\x01",
            "the other guildhouses.\x02\x03",

            "Before we leave, though, is there\x01",
            "anything else we can help with?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E05F")

    label("loc_DEF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DFC1")
    TurnDirection(0x103, 0x8, 400)

    def lambda_DF0D():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DF0D)
    Sleep(100)

    def lambda_DF20():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DF20)

    ChrTalk(    #413
        0x103,
        (
            "#020FWell, at this point, it's time to put\x01",
            "our weary feet back on the road\x01",
            "to help the other guildhouses.\x02\x03",

            "Need help with anything before we go?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E05F")

    label("loc_DFC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E05F")
    TurnDirection(0x106, 0x8, 400)

    def lambda_DFDC():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DFDC)
    Sleep(100)

    def lambda_DFEF():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DFEF)

    ChrTalk(    #414
        0x106,
        (
            "#051FWell, we gotta get a move on and\x01",
            "get the rest of the guild going, but...\x02\x03",

            "Need anything else?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E05F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E135")
    OP_8C(0x8, 90, 400)

    ChrTalk(    #415
        0x8,
        (
            "#655F#1PRight, hmm.\x02\x03",

            "#650FCheck the postings on the board, if you could.\x02\x03",

            "Also, if you could check the places outside\x01",
            "the city limits, like the orphanage and\x01",
            "school, I'd appreciate it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E1FA")

    label("loc_E135")

    OP_8C(0x8, 90, 400)

    ChrTalk(    #416
        0x8,
        (
            "#655F#1PRight, hmm.\x02\x03",

            "#650FCheck the postings on the board, if you could.\x02\x03",

            "Also, if you could check the places outside\x01",
            "the city limits, like the orphanage and\x01",
            "school, I'd appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E1FA")


    ChrTalk(    #417
        0x101,
        (
            "#1015F#2PYeah, I can see how you'd need\x01",
            "a patrol at a time like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x102,
        "#1040FWe'll keep an eye out as best we can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0x8,
        "#651F#1PThanks!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #420
        (
            "\x07\x05With the phone fixed, you can call the team from\x01",
            "another branch to Ruan. If you wish to call them,\x01",
            "select 'Call Allies' when speaking to Jean.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_4B(0x8, 255)
    OP_A2(0x2001)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E34E")
    OP_A2(0x2091)
    Jump("loc_E351")

    label("loc_E34E")

    OP_A3(0x2091)

    label("loc_E351")

    OP_28(0x9B, 0x2, 0x4)
    OP_28(0x9B, 0x1, 0x8)
    OP_6D(-2150, 0, 43020, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -2150, 0, 43020, 135)
    SetChrPos(0x1, -2150, 0, 43020, 135)
    SetChrPos(0x2, -2150, 0, 43020, 135)
    SetChrPos(0x3, -2150, 0, 43020, 135)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_19_C4EF end

    def Function_20_E3EF(): pass

    label("Function_20_E3EF")

    OP_8E(0xFE, 0xFFFFF22C, 0x0, 0xACA8, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_20_E3EF end

    def Function_21_E40B(): pass

    label("Function_21_E40B")

    OP_8E(0xFE, 0xFFFFF22C, 0x0, 0xB0F4, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_21_E40B end

    def Function_22_E427(): pass

    label("Function_22_E427")

    OP_8E(0xFE, 0xFFFFF6A0, 0x0, 0xACA8, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_22_E427 end

    def Function_23_E443(): pass

    label("Function_23_E443")

    OP_8E(0xFE, 0xFFFFF876, 0x0, 0xAA8C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFF6A0, 0x0, 0xB0F4, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_23_E443 end

    def Function_24_E473(): pass

    label("Function_24_E473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E48D")
    Return()

    label("loc_E48D")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E4AD")
    Call(0, 29)
    Call(0, 30)
    FadeToBright(0, 0)

    label("loc_E4AD")

    OP_22(0xC3, 0x1, 0x64)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x0, 0x0, 0xFF, -6670, 1900, 46840, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_4A(0x8, 255)

    ChrTalk(    #421
        0x101,
        "#1004FWhoa!\x02",
    )

    CloseMessageWindow()

    def lambda_E52A():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_E52A)

    def lambda_E538():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_E538)
    Sleep(100)

    def lambda_E54B():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_E54B)
    OP_8C(0x3, 315, 400)

    ChrTalk(    #422
        0x8,
        "#653F#6PA call already? THAT was fast.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-6390, 0, 46350, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(2220, 0)
    OP_6C(315000, 0)
    OP_6E(313, 0)
    SetChrPos(0x101, -550, 0, 39990, 315)
    SetChrPos(0x102, 80, 0, 40550, 315)
    SetChrPos(0xF8, 180, 0, 39140, 315)
    SetChrPos(0xF9, 840, 0, 39800, 315)
    OP_8E(0x8, 0xFFFFE796, 0x0, 0xB70C, 0x7D0, 0x0)
    OP_8C(0x8, 270, 400)
    Sleep(700)
    OP_23(0xC3)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    PlayEffect(0x1, 0x1, 0xFF, -6670, 1900, 46840, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x101, 0x1)
    OP_43(0x102, 0x1, 0x0, 0x15)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0x14)
    Sleep(200)
    OP_43(0xF9, 0x1, 0x0, 0x17)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x16)

    ChrTalk(    #423
        0x8,
        (
            "#652F#4PHello, Bracer Guild, Ruan branch.\x02\x03",

            "#650FOh! Elnan!\x02\x03",

            "#651FI was just thinking of calling\x01",
            "YOU, actually.\x02\x03",

            "No, no, the phone only started\x01",
            "working a second ago. Good timing.\x02\x03",

            "#653FEstelle's group?\x01",
            "They're right here, actually.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)

    def lambda_E79D():
        OP_6D(-5690, 0, 46380, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E79D)

    def lambda_E7B5():
        OP_67(0, 6020, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E7B5)
    OP_6E(330, 1200)

    ChrTalk(    #424
        0x101,
        "#1004F#2P(Elnan wants us?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x102,
        (
            "#1044F(Seems like it.\x01",
            "I wonder what's going on.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x8,
        (
            "#652F#4PYes... Yes.\x02\x03",

            "...\x02\x03",

            "#650FYes, I understand, I'll tell them.\x02\x03",

            "I'll give you another call about the situation\x01",
            "over here once I have a better picture.\x02\x03",

            "#651FGood luck over there.\x01",
            "Talk to you later.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E93D")

    ChrTalk(    #427
        0x106,
        (
            "#052FJean, that was Elnan?\x01",
            "What's up?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E96C")

    label("loc_E93D")


    ChrTalk(    #428
        0x101,
        "#1015F#2PUm, Jean, that was Elnan, right?\x02",
    )

    CloseMessageWindow()

    label("loc_E96C")

    OP_8E(0x8, 0xFFFFE9BC, 0x0, 0xB02C, 0x7D0, 0x0)
    OP_8C(0x8, 90, 400)

    ChrTalk(    #429
        0x8,
        (
            "#650F#6PYeah, he's still at the Grancel branch.\x02\x03",

            "Apparently, Her Majesty wants to\x01",
            "talk to you all about something.\x02\x03",

            "They'd like for you to stop by Grancel\x01",
            "when you get the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0x101,
        "#1004F#2PThe QUEEN?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EA9F")

    ChrTalk(    #431
        0x106,
        (
            "#052FKinda outta the blue...\x01",
            "Wonder what's up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB37")

    label("loc_EA9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EAF2")

    ChrTalk(    #432
        0x103,
        (
            "#023FWell, that's a bit of a shock.\x01",
            "I wonder what she wants.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB37")

    label("loc_EAF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB37")

    ChrTalk(    #433
        0x108,
        (
            "#073FThis is a surprise.\x01",
            "I wonder what she wants.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EBCE")

    ChrTalk(    #434
        0x8,
        (
            "#656F#6PElnan didn't share any details.\x02\x03",

            "It seemed like something he wasn't\x01",
            "comfortable talking about over the phone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EC57")

    label("loc_EBCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EC57")

    ChrTalk(    #435
        0x8,
        (
            "#656F#6PElnan didn't share any details.\x02\x03",

            "It seemed like something he wasn't\x01",
            "comfortable talking about over the phone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC57")


    ChrTalk(    #436
        0x101,
        (
            "#1015F#2PSomething you can't say over the phone...\x02\x03",

            "#1026FI get it, phone calls run the\x01",
            "risk of being intercepted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0x102,
        "#1042FIt must be something secret, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0x8,
        (
            "#650F#6PElnan said it wasn't a huge\x01",
            "emergency, though.\x02\x03",

            "You can stop by whenever you find the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0x101,
        "#1006F#2PHmm. Okay, then.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EDCC")

    ChrTalk(    #440
        0x106,
        (
            "#051FWe'll get over there at\x01",
            "some point, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EDFA")

    label("loc_EDCC")


    ChrTalk(    #441
        0x102,
        "#1040FWe'll try to find some time, then.\x02",
    )

    CloseMessageWindow()

    label("loc_EDFA")

    OP_A2(0x2002)
    OP_28(0x9B, 0x1, 0x200)
    OP_28(0x9B, 0x1, 0x400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 255)
    OP_44(0x101, 0x2)
    OP_44(0x102, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)
    OP_6D(-2150, 0, 43020, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -2150, 0, 43020, 135)
    SetChrPos(0x1, -2150, 0, 43020, 135)
    SetChrPos(0x2, -2150, 0, 43020, 135)
    SetChrPos(0x3, -2150, 0, 43020, 135)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_24_E473 end

    def Function_25_EEC1(): pass

    label("Function_25_EEC1")

    OP_8E(0xFE, 0xFFFFF22C, 0x0, 0xAE2E, 0x7D0, 0x0)

    def lambda_EEDB():

        label("loc_EEDB")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_EEDB")

    QueueWorkItem2(0xFE, 2, lambda_EEDB)
    Return()

    # Function_25_EEC1 end

    def Function_26_EEE7(): pass

    label("Function_26_EEE7")

    OP_8E(0xFE, 0xFFFFF22C, 0x0, 0xB0FE, 0x7D0, 0x0)

    def lambda_EF01():

        label("loc_EF01")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_EF01")

    QueueWorkItem2(0xFE, 2, lambda_EF01)
    Return()

    # Function_26_EEE7 end

    def Function_27_EF0D(): pass

    label("Function_27_EF0D")

    OP_8E(0xFE, 0xFFFFF222, 0x0, 0xAB36, 0x7D0, 0x0)

    def lambda_EF27():

        label("loc_EF27")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_EF27")

    QueueWorkItem2(0xFE, 2, lambda_EF27)
    Return()

    # Function_27_EF0D end

    def Function_28_EF33(): pass

    label("Function_28_EF33")

    OP_8E(0xFE, 0xFFFFF876, 0x0, 0xAA8C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF4DE, 0x0, 0xB3D8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF22C, 0x0, 0xB3E2, 0x7D0, 0x0)

    def lambda_EF75():

        label("loc_EF75")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_EF75")

    QueueWorkItem2(0xFE, 2, lambda_EF75)
    Return()

    # Function_28_EF33 end

    def Function_29_EF81(): pass

    label("Function_29_EF81")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EFFA"),
        (1, "loc_F000"),
        (SWITCH_DEFAULT, "loc_F006"),
    )


    label("loc_EFFA")

    OP_A2(0x1200)
    Jump("loc_F006")

    label("loc_F000")

    OP_A2(0x1201)
    Jump("loc_F006")

    label("loc_F006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_F014")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_F018")

    label("loc_F014")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_F018")

    Return()

    # Function_29_EF81 end

    def Function_30_F019(): pass

    label("Function_30_F019")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_30_F019 end

    SaveToFile()

Try(main)
