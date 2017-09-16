from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C0500   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0500.x',
        MapIndex            = 20,
        MapDefaultBGM       = "ed60031",
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
        'Target Camera',                        # 9
        ' ',                                    # 10
        ' ',                                    # 11
        ' ',                                    # 12
        ' ',                                    # 13
        ' ',                                    # 14
        'ダーティーラッツ',                     # 15
        'ダーティーラッツ',                     # 16
        'ガーフライヤーズ',                     # 17
        'ガーフライヤーズ',                     # 18
        'ガーフライヤーズ',                     # 19
        'ダーティーラッツ',                     # 20
        'ダーティーラッツ',                     # 21
        'ガーフライヤーズ',                     # 22
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
        Unknown_32              = 45,
        Unknown_34              = 45,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 20,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10110 ._CH',             # 00
        'ED6_DT09/CH10111 ._CH',             # 01
        'ED6_DT09/CH10270 ._CH',             # 02
        'ED6_DT09/CH10271 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT09/CH10110P._CP',             # 00
        'ED6_DT09/CH10111P._CP',             # 01
        'ED6_DT09/CH10270P._CP',             # 02
        'ED6_DT09/CH10271P._CP',             # 03
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
        X                   = 2000,
        Z                   = 0,
        Y                   = 10000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x141,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -17000,
        Z                   = 0,
        Y                   = 14000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x141,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -20000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x141,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -24000,
        Z                   = 460,
        Y                   = 37000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x141,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -28000,
        Z                   = 0,
        Y                   = 55800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x141,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 11000,
        Z                   = 0,
        Y                   = 0,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -1000,
        Z                   = 0,
        Y                   = 14000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -20000,
        Z                   = 0,
        Y                   = 16000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -4000,
        Z                   = 0,
        Y                   = 30000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -20000,
        Z                   = 0,
        Y                   = 51000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -24000,
        Z                   = 460,
        Y                   = 37000,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28000,
        Z                   = 0,
        Y                   = 55800,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x30,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -19000,
        Z                   = 0,
        Y                   = 29000,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 1,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 2000,
        Y                   = 0,
        Z                   = 10000,
        Range               = 3000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = -17000,
        Y                   = 0,
        Z                   = 14000,
        Range               = 3000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -20000,
        Y                   = 0,
        Z                   = 28000,
        Range               = 3000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -24000,
        Y                   = 0,
        Z                   = 37000,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = -28000,
        Y                   = 0,
        Z                   = 55800,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = 6170,
        Y                   = -1000,
        Z                   = 2310,
        Range               = 8320,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0xFFFFF5B0,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = 4180,
        Y                   = -1000,
        Z                   = 1490,
        Range               = -1300,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x127A,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )


    DeclActor(
        TriggerX            = 3200,
        TriggerZ            = 0,
        TriggerY            = -17000,
        TriggerRange        = 800,
        ActorX              = 3200,
        ActorZ              = 1000,
        ActorY              = -17000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -28000,
        TriggerZ            = 0,
        TriggerY            = 57000,
        TriggerRange        = 800,
        ActorX              = -28000,
        ActorZ              = 1000,
        ActorY              = 57000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1500,
        TriggerZ            = 0,
        TriggerY            = 30000,
        TriggerRange        = 800,
        ActorX              = -1500,
        ActorZ              = 1000,
        ActorY              = 30000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -19960,
        TriggerZ            = 0,
        TriggerY            = 53960,
        TriggerRange        = 800,
        ActorX              = -19960,
        ActorZ              = 1000,
        ActorY              = 53960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -19960,
        TriggerZ            = 0,
        TriggerY            = 53960,
        TriggerRange        = 800,
        ActorX              = -19960,
        ActorZ              = 1000,
        ActorY              = 53960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -19960,
        TriggerZ            = 0,
        TriggerY            = 51810,
        TriggerRange        = 800,
        ActorX              = -19960,
        ActorZ              = 0,
        ActorY              = 51810,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15800,
        TriggerZ            = 0,
        TriggerY            = -160,
        TriggerRange        = 1000,
        ActorX              = 15800,
        ActorZ              = 1000,
        ActorY              = -160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_446",          # 00, 0
        "Function_1_47C",          # 01, 1
        "Function_2_71E",          # 02, 2
        "Function_3_734",          # 03, 3
        "Function_4_793",          # 04, 4
        "Function_5_899",          # 05, 5
        "Function_6_AF6",          # 06, 6
        "Function_7_F7F",          # 07, 7
        "Function_8_1162",         # 08, 8
        "Function_9_1482",         # 09, 9
        "Function_10_17B2",        # 0A, 10
        "Function_11_1DE9",        # 0B, 11
        "Function_12_205B",        # 0C, 12
        "Function_13_2342",        # 0D, 13
        "Function_14_258A",        # 0E, 14
        "Function_15_26EA",        # 0F, 15
        "Function_16_2926",        # 10, 16
    )


    def Function_0_446(): pass

    label("Function_0_446")

    SetChrPos(0x101, 1370, 0, -15162, 0)
    SetChrPos(0x102, 1370, 0, -15162, 0)
    OP_69(0x101, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 4)), scpexpr(EXPR_END)), "loc_47B")
    SetChrFlags(0x14, 0x80)

    label("loc_47B")

    Return()

    # Function_0_446 end

    def Function_1_47C(): pass

    label("Function_1_47C")

    ClearMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_4A4")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_625")

    label("loc_4A4")

    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_505")
    Call(0, 16)
    SetChrPos(0x0, 2000, 0, 7000, 0)
    OP_30(0x0)
    OP_69(0x101, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_505")
    OP_A2(0x5)

    label("loc_505")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53E")
    Call(0, 16)
    SetChrPos(0x0, -13680, 0, 14260, 270)
    OP_30(0x0)
    OP_69(0x101, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53E")
    OP_A2(0x6)

    label("loc_53E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_577")
    Call(0, 16)
    SetChrPos(0x0, -19860, 0, 24930, 0)
    OP_30(0x0)
    OP_69(0x101, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_577")
    OP_A2(0x7)

    label("loc_577")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B0")
    Call(0, 16)
    SetChrPos(0x0, -21300, 150, 37200, 270)
    OP_30(0x0)
    OP_69(0x101, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B0")
    OP_A2(0x8)

    label("loc_5B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E9")
    Call(0, 16)
    SetChrPos(0x0, -27900, 0, 53010, 0)
    OP_30(0x0)
    OP_69(0x101, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E9")
    OP_A2(0x9)

    label("loc_5E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5F5")
    SetChrFlags(0x9, 0x80)

    label("loc_5F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_601")
    SetChrFlags(0xA, 0x80)

    label("loc_601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_60D")
    SetChrFlags(0xB, 0x80)

    label("loc_60D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_619")
    SetChrFlags(0xC, 0x80)

    label("loc_619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_625")
    SetChrFlags(0xD, 0x80)

    label("loc_625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_637")
    OP_6F(0x1, 0)
    Jump("loc_63E")

    label("loc_637")

    OP_6F(0x1, 60)

    label("loc_63E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_650")
    OP_6F(0x2, 0)
    Jump("loc_657")

    label("loc_650")

    OP_6F(0x2, 60)

    label("loc_657")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x20)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x1, 0x8000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_67A")
    OP_64(0x5, 0x1)
    Jump("loc_6C3")

    label("loc_67A")

    LoadEffect(0x6, "map\\\\evsepith.eff")
    PlayEffect(0x6, 0x6, 0xFF, -19960, 200, 51810, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_6C3")

    OP_6F(0x0, 0)
    OP_72(0x0, 0x10)
    OP_22(0x1CD, 0x1, 0x64)
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 15800, 1000, -160, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_47C end

    def Function_2_71E(): pass

    label("Function_2_71E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_733")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_71E")

    label("loc_733")

    Return()

    # Function_2_71E end

    def Function_3_734(): pass

    label("Function_3_734")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #0
        "\x07\x05The door is rusted and appears to be locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_3_734 end

    def Function_4_793(): pass

    label("Function_4_793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_7A6")
    NewScene("ED6_DT01/T0100   ._SN", 1, 0, 0)
    IdleLoop()
    Jump("loc_898")

    label("loc_7A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_878")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_822")

    ChrTalk(    #1
        0x102,
        (
            "#012FWait a minute, Estelle.\x02\x03",

            "#012FWe still haven't retrieved the\x01",
            "object we're looking for.\x02",
        )
    )

    Jump("loc_871")

    label("loc_822")


    ChrTalk(    #2
        0x102,
        (
            "#012FWe need to get what we came down\x01",
            "here for before we head back up top.\x02",
        )
    )


    label("loc_871")

    CloseMessageWindow()
    TalkEnd(0xFF)
    Jump("loc_898")

    label("loc_878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88F")
    OP_A2(0x22F)
    NewScene("ED6_DT01/T0100   ._SN", 2, 0, 0)
    IdleLoop()
    Jump("loc_898")

    label("loc_88F")

    NewScene("ED6_DT01/T0100   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_898")

    Return()

    # Function_4_793 end

    def Function_5_899(): pass

    label("Function_5_899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_8A1")
    Return()

    label("loc_8A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_8A9")
    Return()

    label("loc_8A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8B5")
    EventBegin(0x1)
    Jump("loc_AB2")

    label("loc_8B5")

    EventBegin(0x0)
    OP_92(0x1, 0x0, 0x320, 0xBB8, 0x0)

    def lambda_8CB():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8CB)

    def lambda_8D9():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8D9)
    OP_69(0x9, 0x3E8)
    Sleep(400)

    ChrTalk(    #3
        0x101,
        "#002FMonsters at 12 o'clock.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        (
            "#012FBe careful not to let them take\x01",
            "advantage of your blind side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#002FGot it!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #6
        (
            "\x07\x05※Monsters cannot be seen from far away. They will become visible\x01",
            "as you approach them.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #7
        (
            "\x07\x05※The conditions at the start of a battle will change depending on how a\x01",
            "monster is engaged. Engaging an enemy from behind is advantageous, while\x01",
            "being attacked by an enemy from behind is disadvantageous.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x0)

    label("loc_AB2")


    def lambda_AB8():
        OP_92(0x0, 0x9, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_AB8)

    def lambda_ACD():
        OP_92(0x1, 0x9, 0x320, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_ACD)
    Sleep(200)
    Battle(0x11, 0x10000B, 0x0, 0x0, 0x9)

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrPos(0x101, 1810, 0, 10700, 0)
    SetChrPos(0x102, 1810, 0, 9370, 0)
    OP_69(0x101, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #1001
        0x101,
        (
            "#502Fふふん、思ったより楽勝ね。\x02\x03",

            "#508Fよ～し、\x01",
            "この調子で先に進むわよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #1002
        0x102,
        (
            "#010Fエステル、ちょっと待って。\x02\x03",

            "#010F今、戦った魔獣の情報を\x01",
            "魔獣手帳に記しておこう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #1003
        0x101,
        (
            "#008Fあっと、そうだったわね。\x02\x03",

            "#502Fさらさらさらっと……\x02\x03",

            "#006Fよしっ、これでオッケーね。\x02",
        )
    )

    CloseMessageWindow()

    EventEnd(0x2)
    SetMapFlags(0x1)
    Return()

    # Function_5_899 end

    def Function_6_AF6(): pass

    label("Function_6_AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_AFE")
    Return()

    label("loc_AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_B06")
    Return()

    label("loc_B06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x14)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x1E)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x1E)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x32)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x32)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BA(0x0, 0x41)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_BA(0x1, 0x41)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF2")
    EventBegin(0x0)
    OP_92(0x1, 0x0, 0x320, 0xBB8, 0x0)

    def lambda_B65():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B65)

    def lambda_B73():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B73)
    OP_69(0xA, 0x3E8)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB6")

    ChrTalk(    #8
        0x101,
        "#002FMore company straight ahead!\x02",
    )

    CloseMessageWindow()

    label("loc_BB6")


    ChrTalk(    #9
        0x102,
        (
            "#012FHmm...\x01",
            "Physical attacks might not\x01",
            "work on this one.\x02\x03",

            "#012FLet's try out some arts attacks\x01",
            "before we move on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#002FI'm all for that!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #11
        (
            "\x07\x05※Quartz are installed in the 'Orbment' screen.\x01",
            "The 'Orbment' screen can be accessed by\x01",
            "selecting the 'Orbment' tab.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    EventEnd(0x0)
    OP_A2(0xA)
    Return()

    label("loc_CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_CFE")
    EventBegin(0x2)
    Jump("loc_F3B")

    label("loc_CFE")

    EventBegin(0x0)
    OP_92(0x1, 0x0, 0x320, 0xBB8, 0x0)

    def lambda_D14():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D14)

    def lambda_D22():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D22)
    OP_69(0xA, 0x3E8)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5D")

    ChrTalk(    #12
        0x101,
        "#002FHere come some more!\x02",
    )

    CloseMessageWindow()

    label("loc_D5D")


    ChrTalk(    #13
        0x102,
        (
            "#012FDepending on the enemy, some\x01",
            "physical attacks may be\x01",
            "ineffective.\x02\x03",

            "#012FLet's use arts, not physical attacks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#005FOkay!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #15
        (
            "\x07\x05※Arts are effective on enemies that are good at avoiding physical attacks.\x01",
            "Arts also make long range attacks possible, but they require time to be cast.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #16
        (
            "\x07\x05※EP is consumed when arts are used. EP can be recovered by resting at\x01",
            "inns, hotels, or by using charge stations and other items, like an EP Charge.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x1)
    OP_A2(0xA)

    label("loc_F3B")


    def lambda_F41():
        OP_92(0x0, 0xA, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_F41)

    def lambda_F56():
        OP_92(0x1, 0xA, 0x320, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_F56)
    Sleep(200)
    Battle(0x12, 0x10000B, 0x0, 0x0, 0xA)
    EventEnd(0x2)
    SetMapFlags(0x1)
    Return()

    # Function_6_AF6 end

    def Function_7_F7F(): pass

    label("Function_7_F7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_F87")
    Return()

    label("loc_F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_F8F")
    Return()

    label("loc_F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F9B")
    EventBegin(0x2)
    Jump("loc_111E")

    label("loc_F9B")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_92(0x1, 0x0, 0x320, 0xBB8, 0x0)

    def lambda_FB6():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FB6)

    def lambda_FC4():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FC4)
    OP_69(0xB, 0x3E8)
    Sleep(400)

    ChrTalk(    #17
        0x102,
        (
            "#012FEstelle, let's try using crafts\x01",
            "this time around.\x02\x03",

            "#012FSince crafts have other effects\x01",
            "besides just dealing out damage,\x01",
            "they're worth a shot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#005FRoger that!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #19
        (
            "\x07\x05※Crafts have range limits, but can be utilized instantly. CP is gained by\x01",
            "dealing out or receiving damage during battle.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x2)

    label("loc_111E")


    def lambda_1124():
        OP_92(0x101, 0xB, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1124)

    def lambda_1139():
        OP_92(0x102, 0xB, 0x320, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1139)
    Sleep(200)
    Battle(0x13, 0x10000B, 0x0, 0x0, 0xB)
    EventEnd(0x2)
    SetMapFlags(0x1)
    Return()

    # Function_7_F7F end

    def Function_8_1162(): pass

    label("Function_8_1162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_116A")
    Return()

    label("loc_116A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1172")
    Return()

    label("loc_1172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_117E")
    EventBegin(0x2)
    Jump("loc_143E")

    label("loc_117E")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_92(0x1, 0x0, 0x320, 0xBB8, 0x0)

    def lambda_1199():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1199)

    def lambda_11A7():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11A7)
    OP_69(0xC, 0x3E8)
    Sleep(400)

    ChrTalk(    #20
        0x101,
        (
            "#509FOh, what a surprise.\x01",
            "Another creepy thing.\x02\x03",

            "#509FI wish there were an easier\x01",
            "way to take care of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        (
            "#012FOne blow using an S-Craft\x01",
            "or S-Break should do the trick\x01",
            "for just about any enemy.\x02\x03",

            "#012FThe catch is, our CP has to be\x01",
            "at least 100 to pull off one of\x01",
            "those moves.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #22
        (
            "\x07\x05※These devastating attacks can only be unleashed when the CP gauge is\x01",
            "above 100.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #23
        (
            "\x07\x05※S-Breaks are actions which allow S-Crafts to be immediately unleashed\x01",
            "while ignoring the battle order.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #24
        (
            "\x07\x05S-Crafts, which are unleashed as S-Breaks, can be changed by going to\x01",
            "'Tactics' and then 'Set S-Break' within the main menu.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x3)

    label("loc_143E")


    def lambda_1444():
        OP_92(0x0, 0xC, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1444)

    def lambda_1459():
        OP_92(0x1, 0xC, 0x320, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1459)
    Sleep(200)
    Battle(0x10, 0x10000B, 0x0, 0x0, 0xC)
    EventEnd(0x2)
    SetMapFlags(0x1)
    Return()

    # Function_8_1162 end

    def Function_9_1482(): pass

    label("Function_9_1482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_148A")
    Return()

    label("loc_148A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1492")
    Return()

    label("loc_1492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_149E")
    EventBegin(0x2)
    Jump("loc_176E")

    label("loc_149E")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_92(0x1, 0x0, 0x320, 0xBB8, 0x0)

    def lambda_14B9():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14B9)

    def lambda_14C7():
        TurnDirection(0xFE, 0xD, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14C7)
    OP_6D(-28300, 0, 54500, 1000)
    Sleep(400)

    ChrTalk(    #25
        0x101,
        (
            "#000FSo that's the treasure chest\x01",
            "we're after, huh?\x02\x03",

            "#000FIf we've made it this far,\x01",
            "the rest is gonna be a\x01",
            "piece of cake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        (
            "#010FSeems like we've got a little\x01",
            "breathing room at least.\x02\x03",

            "#010FLet's pay close attention to\x01",
            "our battle order this time.\x02\x03",

            "#010FThere should be a number of\x01",
            "ways to get more mileage out\x01",
            "of our actions.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #27
        "\x07\x05※During battle there are several bonuses which can be allotted to turns.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #28
        (
            "\x07\x05※Turn bonuses have the same effect regardless of whether they are\x01",
            "allotted to an ally or a foe. Using S-Breaks to ignore the battle order makes\x01",
            "it easy to jump in and strip an enemy of their turn bonus.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x4)

    label("loc_176E")


    def lambda_1774():
        OP_92(0x0, 0xD, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1774)

    def lambda_1789():
        OP_92(0x1, 0xD, 0x320, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1789)
    Sleep(200)
    Battle(0xF, 0x10000B, 0x0, 0x0, 0xD)
    EventEnd(0x2)
    SetMapFlags(0x1)
    Return()

    # Function_9_1482 end

    def Function_10_17B2(): pass

    label("Function_10_17B2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D7F")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_92(0x1, 0x0, 0x320, 0xBB8, 0x0)
    OP_8B(0x0, 0xFFFF92A0, 0xDEA8, 0x0)
    OP_8B(0x1, 0xFFFF92A0, 0xDEA8, 0x0)
    OP_51(0x8, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x8, 0x5DC)
    OP_28(0xA, 0x1, 0x2)
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #29
        "\x07\x00Found \x07\x02Small Box\x07\x00 x2.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_3E(0x373, 2)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #30
        0x101,
        (
            "#505FHmm...that's weird.\x01",
            "There's a couple of boxes inside\x01",
            "the treasure chest.\x02\x03",

            "#501FThe fact that there's not just one,\x01",
            "but two, is kinda interesting, too.\x01",
            "Wonder what's inside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        (
            "#014FRemember, Estelle, our mission\x01",
            "is to search and retrieve only.\x02\x03",

            "#014FI'm pretty sure looking inside\x01",
            "those boxes doesn't fall under\x01",
            "our mission objective.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#502FYou're no fun at all, Joshua.\x02\x03",

            "#502FThis has nothing to do with our\x01",
            "mission. It's what I like to call\x01",
            "good, honest curiosity.\x02\x03",

            "#502F...\x02\x03",

            "#006F...You know, we're the only ones\x01",
            "down here. We can get away with\x01",
            "a teensy-weensy peek, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        (
            "#014F...\x02\x03",

            "#015FIf you feel like flunking today's\x01",
            "test, then by all means,\x01",
            "be my guest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#580FDid you just say the 'F' word?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        (
            "#010FYep. Opening one of those boxes\x01",
            "could result in an automatic fail\x01",
            "for the both of us.\x02\x03",

            "#010FIf this were a real job, the\x01",
            "contents of those boxes\x01",
            "would belong to the client.\x02\x03",

            "#010FAnd as long as they were\x01",
            "nothing illegal, we would\x01",
            "have no right to open them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#007FI know you're right, Joshua...\x01",
            "But I just can't help myself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        (
            "#019FIf you absolutely have to know\x01",
            "what's inside, why not ask\x01",
            "Miss Schera when we get back?\x02\x03",

            "#010FBut for now we need to focus\x01",
            "on getting out of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#006FAll right, all right.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x28A)
    Sleep(30)
    EventEnd(0x0)
    Jump("loc_1DE3")

    label("loc_1D7F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #39
        "\x07\x05By looking inside this chest again, you flunk! ...Just kidding.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Sleep(30)

    label("loc_1DE3")

    ClearMapFlags(0x8000000)
    Return()

    # Function_10_17B2 end

    def Function_11_1DE9(): pass

    label("Function_11_1DE9")

    SetMapFlags(0x8000000)
    EventBegin(0x0)
    OP_82(0x6, 0x0)
    OP_84(0x6)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #40
        "\x07\x00Found \x07\x02Quartz Fragment\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(400)
    OP_3E(0x325, 1)
    OP_64(0x5, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_204D")

    ChrTalk(    #41
        0x101,
        (
            "#000FI see now.\x02\x03",

            "The thing we saw shining through\x01",
            "the sewer grate was this.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #42
        0x102,
        (
            "#010FSeems like it.\x02\x03",

            "A quartz fragment, huh...?\x01",
            "Now we know why it was\x01",
            "shining so much.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #43
        0x101,
        (
            "#000FThe way it sparkles is so beautiful.\x02\x03",

            "This is made of septium too, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#010FLoosely speaking, yes...\x02\x03",

            "But let's talk about it later.\x02\x03",

            "This isn't really the place to\x01",
            "have a leisurely chat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#004FI guess you're right.\x02\x03",

            "No normal person would want\x01",
            "to stay here any longer than\x01",
            "they had to.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4, 0x1, 0x20)
    Jump("loc_2053")

    label("loc_204D")

    OP_28(0x4, 0x1, 0x8000)

    label("loc_2053")

    EventEnd(0x0)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1DE9 end

    def Function_12_205B(): pass

    label("Function_12_205B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_206A")
    Return()

    label("loc_206A")

    EventBegin(0x0)
    OP_28(0xA, 0x1, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2121")
    TurnDirection(0x102, 0x101, 0)
    Sleep(100)

    ChrTalk(    #46
        0x102,
        (
            "#010FThere appears to be a recovery\x01",
            "point set up over there.\x02\x03",

            "Let's use it if our HP and EP\x01",
            "become low before engaging\x01",
            "in any further battles.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21B1")

    label("loc_2121")

    TurnDirection(0x102, 0x101, 0)
    Sleep(100)

    ChrTalk(    #47
        0x102,
        (
            "#010FWait a minute, Estelle.\x02\x03",

            "There appears to be a recovery point\x01",
            "over there, so we should use it if our\x01",
            "HP or EP become low.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21B1")

    Sleep(100)

    def lambda_21BC():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_21BC)

    def lambda_21CA():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_21CA)
    OP_6D(13300, 0, -130, 1500)
    TurnDirection(0x102, 0x101, 0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #48
        "\x07\x05※Orbment charging stations are recovery points set up in dangerous areas.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #49
        (
            "\x07\x05※As a recovery point is approached, a '!' mark will appear and two choices\x01",
            "will be displayed by pressing the OK button. By selecting the 'Rest' option,\x01",
            "all HP and EP will be restored.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(100)
    OP_69(0x0, 0x5DC)

    ChrTalk(    #50
        0x101,
        "#000FSounds like a plan to me!\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_12_205B end

    def Function_13_2342(): pass

    label("Function_13_2342")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xA, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_2351")
    Return()

    label("loc_2351")

    EventBegin(0x0)
    OP_28(0xA, 0x1, 0x8000)
    OP_8C(0x102, 90, 0)
    Sleep(100)

    ChrTalk(    #51
        0x102,
        (
            "#010FThere appears to be a recovery\x01",
            "point set up over there.\x02\x03",

            "Let's use it if our HP and EP\x01",
            "become low before engaging\x01",
            "in any further battles.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_2404():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2404)

    def lambda_2412():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2412)
    OP_6D(13300, 0, -130, 1500)
    TurnDirection(0x102, 0x101, 0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #52
        (
            "\x07\x05※Orbment charging stations are recovery\x01",
            "points set up in dangerous areas.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #53
        (
            "\x07\x05※As a recovery point is approached, a '!' mark will appear\x01",
            "and two choices will be displayed by pressing the OK button.\x01",
            "By selecting the 'Rest' option, all HP and EP will be restored.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(100)
    OP_69(0x0, 0x5DC)

    ChrTalk(    #54
        0x101,
        "#000FSounds like a plan to me!\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_13_2342 end

    def Function_14_258A(): pass

    label("Function_14_258A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x51, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2685")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_2604")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #55
        "\x07\x00Found \x07\x02Reviving Balm\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x28B)
    Jump("loc_2682")

    label("loc_2604")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #56
        (
            "\x07\x00Found \x07\x02Reviving Balm\x07\x00 in chest.\x01",
            "Inventory full so gave up \x07\x02Reviving Balm\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_2682")

    Jump("loc_26DC")

    label("loc_2685")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #57
        "\x07\x05The chest is empty...because of you. Nice work, hero.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_83(0xF, 0x8)

    label("loc_26DC")

    TalkEnd(0xFF)
    Sleep(30)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_258A end

    def Function_15_26EA(): pass

    label("Function_15_26EA")

    OP_28(0xA, 0x1, 0x8000)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #58
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_290B")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 15800, 1000, -160, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x32)
    OP_73(0x3)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 15800, 1000, -160, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    SetChrPos(0x0, 14290, 0, -230, 92)
    SetChrPos(0x1, 14290, 0, -230, 92)
    SetChrPos(0x2, 14290, 0, -230, 92)
    SetChrPos(0x3, 14290, 0, -230, 92)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Sleep(3500)
    OP_82(0x1, 0x2)
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 15800, 1000, -160, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x3, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_290B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2925")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2925")

    Return()

    # Function_15_26EA end

    def Function_16_2926(): pass

    label("Function_16_2926")

    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_51(0x101, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    Return()

    # Function_16_2926 end

    SaveToFile()

Try(main)
