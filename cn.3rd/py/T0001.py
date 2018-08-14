from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 调试地图

    CreateScenaFile(
        FileName            = 'T0001   ._SN',
        MapName             = 'map1',
        Location            = 'T0001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0001   ._SN',
            'ED6_DT21/T0001_1 ._SN',
            'ED6_DT21/T0001_2 ._SN',
            'ED6_DT21/T0001_3 ._SN',
            'ED6_DT21/T0001_4 ._SN',
            'ED6_DT21/T0001_5 ._SN',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '居民1',                                # 9
        '居民1',                                # 10
        '00',                                   # 11
        '01',                                   # 12
        '02',                                   # 13
        '03',                                   # 14
        '04',                                   # 15
        '05',                                   # 16
        '06',                                   # 17
        '07',                                   # 18
        '08',                                   # 19
        '09',                                   # 20
        '10',                                   # 21
        '11',                                   # 22
        '12',                                   # 23
        '13',                                   # 24
        '14',                                   # 25
        '15',                                   # 26
        '16',                                   # 27
        '宝箱',                                 # 28
        '坐',                                   # 29
        '',                                     # 30
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
        EntryFunctionIndex      = 2,
    )


    AddCharChip(
        'ED6_DT07/CH01000 ._CH',             # 00
        'ED6_DT09/CH10020 ._CH',             # 01
        'ED6_DT27/CHDUMMY ._CH',             # 02
        'ED6_DT27/CHDUMMY ._CH',             # 03
        'ED6_DT27/CHDUMMY ._CH',             # 04
        'ED6_DT27/CHDUMMY ._CH',             # 05
        'ED6_DT27/CHDUMMY ._CH',             # 06
        'ED6_DT27/CHDUMMY ._CH',             # 07
        'ED6_DT27/CHDUMMY ._CH',             # 08
        'ED6_DT27/CHDUMMY ._CH',             # 09
        'ED6_DT27/CHDUMMY ._CH',             # 0A
        'ED6_DT27/CHDUMMY ._CH',             # 0B
        'ED6_DT27/CHDUMMY ._CH',             # 0C
        'ED6_DT27/CHDUMMY ._CH',             # 0D
        'ED6_DT27/CHDUMMY ._CH',             # 0E
        'ED6_DT27/CHDUMMY ._CH',             # 0F
        'ED6_DT27/CHDUMMY ._CH',             # 10
        'ED6_DT27/CHDUMMY ._CH',             # 11
        'ED6_DT27/CHDUMMY ._CH',             # 12
        'ED6_DT27/CH03153 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH01000P._CP',             # 00
        'ED6_DT09/CH10020P._CP',             # 01
        'ED6_DT27/CHDUMMYP._CP',             # 02
        'ED6_DT27/CHDUMMYP._CP',             # 03
        'ED6_DT27/CHDUMMYP._CP',             # 04
        'ED6_DT27/CHDUMMYP._CP',             # 05
        'ED6_DT27/CHDUMMYP._CP',             # 06
        'ED6_DT27/CHDUMMYP._CP',             # 07
        'ED6_DT27/CHDUMMYP._CP',             # 08
        'ED6_DT27/CHDUMMYP._CP',             # 09
        'ED6_DT27/CHDUMMYP._CP',             # 0A
        'ED6_DT27/CHDUMMYP._CP',             # 0B
        'ED6_DT27/CHDUMMYP._CP',             # 0C
        'ED6_DT27/CHDUMMYP._CP',             # 0D
        'ED6_DT27/CHDUMMYP._CP',             # 0E
        'ED6_DT27/CHDUMMYP._CP',             # 0F
        'ED6_DT27/CHDUMMYP._CP',             # 10
        'ED6_DT27/CHDUMMYP._CP',             # 11
        'ED6_DT27/CHDUMMYP._CP',             # 12
        'ED6_DT27/CH03153P._CP',             # 13
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = -4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2000,
        Z                   = 0,
        Y                   = -2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3000,
        Z                   = 0,
        Y                   = -2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = -2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 5000,
        Z                   = 0,
        Y                   = -2000,
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
        X                   = 6000,
        Z                   = 0,
        Y                   = -2000,
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
        X                   = 7000,
        Z                   = 0,
        Y                   = -2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = -2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000,
        Z                   = 0,
        Y                   = -2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 10000,
        Z                   = 0,
        Y                   = -2000,
        Direction           = 0,
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
        X                   = 11000,
        Z                   = 0,
        Y                   = -2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = -2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 13000,
        Z                   = 0,
        Y                   = -2000,
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

    DeclNpc(
        X                   = 14000,
        Z                   = 0,
        Y                   = -2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 15000,
        Z                   = 0,
        Y                   = -2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = -2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17000,
        Z                   = 0,
        Y                   = -2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 18000,
        Z                   = 0,
        Y                   = -2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 19000,
        Z                   = 0,
        Y                   = -2000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -5000,
        Z                   = 0,
        Y                   = -6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -7000,
        Z                   = 0,
        Y                   = -7000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )


    DeclEvent(
        X                   = 0,
        Y                   = 0,
        Z                   = 0,
        Range               = 0,
        Unknown_10          = 0x0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x2,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = 0,
        Y                   = 0,
        Z                   = 0,
        Range               = 0,
        Unknown_10          = 0x0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x20,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = -170,
        TriggerZ            = 0,
        TriggerY            = 5890,
        TriggerRange        = 1000,
        ActorX              = -170,
        ActorZ              = 1000,
        ActorY              = 5890,
        Flags               = 0x7C,
        TalkScenaIndex      = 4,
        TalkFunctionIndex   = 38,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5930,
        TriggerZ            = 0,
        TriggerY            = 2120,
        TriggerRange        = 1000,
        ActorX              = 5930,
        ActorZ              = 1300,
        ActorY              = 2120,
        Flags               = 0x7C,
        TalkScenaIndex      = 4,
        TalkFunctionIndex   = 37,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_472",          # 00, 0
        "Function_1_51F",          # 01, 1
        "Function_2_54C",          # 02, 2
        "Function_3_6AD",          # 03, 3
        "Function_4_6AE",          # 04, 4
        "Function_5_13CE",         # 05, 5
        "Function_6_13F4",         # 06, 6
        "Function_7_1486",         # 07, 7
        "Function_8_15F8",         # 08, 8
        "Function_9_1617",         # 09, 9
        "Function_10_1636",        # 0A, 10
        "Function_11_1655",        # 0B, 11
        "Function_12_1670",        # 0C, 12
        "Function_13_1698",        # 0D, 13
        "Function_14_16B3",        # 0E, 14
        "Function_15_16CA",        # 0F, 15
    )


    def Function_0_472(): pass

    label("Function_0_472")

    OP_AA(0)
    OP_BB(0x1, 0x1, 0x1A)
    OP_BB(0x2, 0x1, 0x19)
    OP_BB(0x3, 0x1, 0x1B)
    OP_BB(0x4, 0x1, 0x1D)
    SetMapFlags(0x1000000)
    SetChrBattleFlags(0x10, 0x40)
    SetChrBattleFlags(0x11, 0x40)
    Event(0, 4)
    OP_DB(0x0, 0x8)
    OP_DB(0x0, 0xE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x47), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x48), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_509")
    OP_35(0x0, 0x0)
    OP_35(0x1, 0x0)
    OP_35(0x2, 0x0)
    OP_35(0x3, 0x0)
    OP_35(0x4, 0x0)
    OP_35(0x5, 0x0)
    OP_35(0x6, 0x0)
    OP_35(0x7, 0x0)
    OP_35(0x8, 0x0)
    OP_35(0x9, 0x0)
    OP_35(0xA, 0x0)
    OP_35(0xB, 0x0)
    OP_35(0xC, 0x0)
    OP_35(0xD, 0x0)
    OP_35(0xE, 0x0)
    OP_35(0xF, 0x0)

    label("loc_509")

    OP_43(0x0, 0x2, 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_51E")
    OP_A3(0x2505)
    Event(4, 42)

    label("loc_51E")

    Return()

    # Function_0_472 end

    def Function_1_51F(): pass

    label("Function_1_51F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54B")
    OP_CA(0x1, 0x3, 0xFFFFFFFF)
    OP_D0(134217735, 2000)
    OP_CA(0x1, 0x3, 0x0)
    OP_D0(134217735, 2000)
    Jump("Function_1_51F")

    label("loc_54B")

    Return()

    # Function_1_51F end

    def Function_2_54C(): pass

    label("Function_2_54C")

    OP_51(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0xC5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0xB1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x4F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_54C end

    def Function_3_6AD(): pass

    label("Function_3_6AD")

    Return()

    # Function_3_6AD end

    def Function_4_6AE(): pass

    label("Function_4_6AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B5, 1)), scpexpr(EXPR_END)), "loc_6BB")
    OP_A3(0x25A9)
    Jump("loc_6BE")

    label("loc_6BB")

    OP_A2(0x25A9)

    label("loc_6BE")

    OP_C4(0x0, 0x200)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x80)
    OP_57(0x0, 0x0, 0x12, "#1C菜单标题")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13C2")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "测试地图\x01",                  # 0
            "游戏地图\x01",                  # 1
            "角色一览\x01",                  # 2
            "魔兽一览\x01",                  # 3
            "战斗\x01",                      # 4
            "战斗（魔兽算法测试）\x01",      # 5
            "战斗（地图确认）\x01",          # 6
            "迷你游戏\x01",                  # 7
            "事件\x01",                      # 8
            "章节\x01",                      # 9
            "商店测试\x01",                  # 10
            "前篇后编角色替换新画\x01",      # 11
            "*Trap Land\x01",                # 12
            "头像\x01",                      # 13
            "组队选择菜单\x01",              # 14
            "*模糊（blur）\x01",             # 15
            "*出不来！存档菜单\x01",         # 16
            "手册标志树立完毕\x01",          # 17
            "菜谱收集完整\x01",              # 18
            "游戏通关\x01",                  # 19
            "Camp菜单\x01",                  # 20
            "章节测试\x01",                  # 21
            "test\x01",                      # 22
            "取消\x01",                      # 23
        )
    )

    Jump("loc_889")

    label("loc_889")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8F1"),
        (1, "loc_8F8"),
        (2, "loc_8FF"),
        (3, "loc_906"),
        (4, "loc_90D"),
        (5, "loc_914"),
        (6, "loc_91B"),
        (7, "loc_922"),
        (8, "loc_929"),
        (9, "loc_930"),
        (10, "loc_937"),
        (11, "loc_943"),
        (12, "loc_AC6"),
        (13, "loc_AD2"),
        (14, "loc_D34"),
        (15, "loc_F96"),
        (16, "loc_FDB"),
        (17, "loc_FDF"),
        (18, "loc_FE6"),
        (19, "loc_FED"),
        (20, "loc_1009"),
        (21, "loc_126C"),
        (22, "loc_12B0"),
        (SWITCH_DEFAULT, "loc_13B2"),
    )


    label("loc_8F1")

    Call(0, 6)
    Jump("loc_13BF")

    label("loc_8F8")

    Call(3, 8)
    Jump("loc_13BF")

    label("loc_8FF")

    Call(3, 0)
    Jump("loc_13BF")

    label("loc_906")

    Call(3, 4)
    Jump("loc_13BF")

    label("loc_90D")

    Call(2, 0)
    Jump("loc_13BF")

    label("loc_914")

    Call(1, 0)
    Jump("loc_13BF")

    label("loc_91B")

    Call(2, 1)
    Jump("loc_13BF")

    label("loc_922")

    Call(2, 17)
    Jump("loc_13BF")

    label("loc_929")

    Call(4, 2)
    Jump("loc_13BF")

    label("loc_930")

    Call(5, 0)
    Jump("loc_13BF")

    label("loc_937")

    OP_5F(0x0)
    OP_56(0x0)
    Call(0, 7)
    Jump("loc_13BF")

    label("loc_943")


    Menu(
        1,
        -1,
        -1,
        1,
        (
            "艾丝蒂尔(SC)、约修亚(SC)\x01",      # 0
            "艾丝蒂尔(FC)、约修亚(FC)\x01",      # 1
            "约修亚(没有SC纹章)\x01",            # 2
            "约修亚(AC服装)\x01",                # 3
            "雪拉(18岁)\x01",                    # 4
            "雪拉(AC服装)\x01",                  # 5
            "雪拉(旧服装)\x01",                  # 6
            "奥利维尔(AC服装)\x01",              # 7
            "奥利维尔(旧服装)\x01",              # 8
            "科洛丝(礼服)\x01",                  # 9
            "科洛丝(制服)\x01",                  # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A39"),
        (1, "loc_A4A"),
        (2, "loc_A5B"),
        (3, "loc_A65"),
        (4, "loc_A6F"),
        (5, "loc_A79"),
        (6, "loc_A83"),
        (7, "loc_A8D"),
        (8, "loc_A97"),
        (9, "loc_AA1"),
        (10, "loc_AAB"),
        (SWITCH_DEFAULT, "loc_AB5"),
    )


    label("loc_A39")

    OP_BB(0x0, 0x1, 0x0)
    OP_BB(0x1, 0x1, 0x1)
    Jump("loc_AB5")

    label("loc_A4A")

    OP_BB(0x0, 0x1, 0x1E)
    OP_BB(0x1, 0x1, 0x1F)
    Jump("loc_AB5")

    label("loc_A5B")

    OP_BB(0x1, 0x1, 0x1C)
    Jump("loc_AB5")

    label("loc_A65")

    OP_BB(0x1, 0x1, 0x1A)
    Jump("loc_AB5")

    label("loc_A6F")

    OP_BB(0x2, 0x1, 0x18)
    Jump("loc_AB5")

    label("loc_A79")

    OP_BB(0x2, 0x1, 0x19)
    Jump("loc_AB5")

    label("loc_A83")

    OP_BB(0x2, 0x1, 0x2)
    Jump("loc_AB5")

    label("loc_A8D")

    OP_BB(0x3, 0x1, 0x1B)
    Jump("loc_AB5")

    label("loc_A97")

    OP_BB(0x3, 0x1, 0x3)
    Jump("loc_AB5")

    label("loc_AA1")

    OP_BB(0x4, 0x1, 0x1D)
    Jump("loc_AB5")

    label("loc_AAB")

    OP_BB(0x4, 0x1, 0x4)
    Jump("loc_AB5")

    label("loc_AB5")

    OP_5F(0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_BD()
    Jump("loc_13BF")

    label("loc_AC6")

    NewScene("ED6_DT21/A0019   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_13BF")

    label("loc_AD2")

    OP_5F(0x0)
    OP_56(0x0)
    Sleep(1000)
    OP_AD(0x240061, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    OP_D9(0x0, "CTI00110")
    Sleep(2000)
    OP_D9(0x1)
    OP_C5(0x0, 0x0, 0x0, 0x200, 0x200, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x1FF, 0x1FF, 0xFFFFFF, 0x0, "C_VIS328._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    LoadEffect(0x0, "test\\portrait.eff")
    PlayEffect(0xC8, 0x1, 0xFF, 100, 155, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    OP_82(0x1, 0x0)
    OP_C5(0x1, 0xFF9C, 0xFF9C, 0x64, 0x64, 0x154, 0xFA, 0x300, 0x200, 0x0, 0x0, 0xFF, 0xFF, 0xFFFFFF, 0x0, "C_VIS001._CH")
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C5(0x0, 0xFF9C, 0xFF9C, 0x64, 0x64, 0x168, 0x104, 0x300, 0x200, 0x0, 0x0, 0xFF, 0xFF, 0xFFFFFF, 0x0, "C_VIS002._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C5(0x2, 0xFF9C, 0xFF9C, 0x64, 0x64, 0x17C, 0x104, 0x300, 0x200, 0x0, 0x0, 0xFF, 0xFF, 0xFFFFFF, 0x0, "C_VIS002._CH")
    OP_C6(0x2, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C5(0x3, 0xFF9C, 0xFF9C, 0x64, 0x64, 0x190, 0x104, 0x300, 0x200, 0x0, 0x0, 0xFF, 0xFF, 0xFFFFFF, 0x0, "C_VIS002._CH")
    OP_C6(0x3, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x0, 0, 0, 1000)
    OP_C6(0x0, 0x2, 90000, 2000, 0)
    OP_C7(0x0, 0x0, 0x0)

    AnonymousTalk(    #0
        "噢\x02",
    )

    Jump("loc_CB3")

    label("loc_CB3")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x0, 360000, 260000, 0)
    Sleep(1000)
    OP_C6(0x1, 0x4, 0, 0, 0)
    Sleep(1000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    OP_C6(0x0, 0x1, 0, 1000, 1000)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    OP_C6(0x3, 0x1, 10000, 0, 500)
    OP_C7(0x0, 0xFF, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    Jump("loc_13BF")

    label("loc_D34")

    OP_5F(0x0)
    OP_56(0x0)

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "１队伍选择 Cancel\x01",                        # 0
            "１チーム選択 (凯文, 莉丝) Cancel\x01",            # 1
            "１チーム選択 (凯文)\x01",                      # 2
            "１チーム選択 (约修亚) Cancel\x01",      # 3
            "２チーム選択 (凯文, 莉丝)\x01",                   # 4
            "４チーム選択 (凯文, 莉丝)\x01",                   # 5
            "４チーム選択 (凯文, 莉丝, 艾丝蒂尔, 约修亚)\x01",           # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E16"),
        (1, "loc_E2D"),
        (2, "loc_E44"),
        (3, "loc_E5B"),
        (4, "loc_E72"),
        (5, "loc_E89"),
        (6, "loc_EA0"),
        (SWITCH_DEFAULT, "loc_EB7"),
    )


    label("loc_E16")

    OP_DD(0x1, 0x0, 0x1, 0, 0, 0, 0)
    Jump("loc_EB7")

    label("loc_E2D")

    OP_DD(0x1, 0x0, 0x1, 16640, 0, 0, 0)
    Jump("loc_EB7")

    label("loc_E44")

    OP_DD(0x1, 0x0, 0x0, 256, 0, 0, 0)
    Jump("loc_EB7")

    label("loc_E5B")

    OP_DD(0x1, 0x0, 0x1, 2, 0, 0, 0)
    Jump("loc_EB7")

    label("loc_E72")

    OP_DD(0x2, 0x1, 0x0, 256, 16384, 0, 0)
    Jump("loc_EB7")

    label("loc_E89")

    OP_DD(0x4, 0x0, 0x1, 0, 0, 0, 16640)
    Jump("loc_EB7")

    label("loc_EA0")

    OP_DD(0x4, 0x0, 0x1, 256, 16384, 1, 2)
    Jump("loc_EB7")

    label("loc_EB7")

    OP_5F(0x2)
    OP_DF(0x0, 0x1, 0x1)
    OP_E0(265, 0x40, 0x2)
    OP_E0(265, 0x41, 0x3)
    OP_E0(271, 0x42, 0x2)
    OP_E0(271, 0x43, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EFE")

    ChrTalk(    #1
        0x0,
        "艾丝蒂尔\x02",
    )

    Jump("loc_EFB")

    label("loc_EFB")

    Jump("loc_F19")

    label("loc_EFE")


    ChrTalk(    #2
        0x0,
        "啊啊啊啊\x02",
    )

    Jump("loc_F19")

    label("loc_F19")

    CloseMessageWindow()
    ClearChrFlags(0x4, 0x8)
    SetChrChipByIndex(0x4, 3)
    OP_8E(0x4, 0xFA0, 0x0, 0xFA0, 0x1388, 0x0)

    ChrTalk(    #3
        0x4,
        "啊啊\x02",
    )

    Jump("loc_F49")

    label("loc_F49")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E1(0x6, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F6E")

    ChrTalk(    #4
        0x0,
        "提妲在队伍1。\x02",
    )

    CloseMessageWindow()

    label("loc_F6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E1(0x6, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F93")

    ChrTalk(    #5
        0x0,
        "提妲在队伍之1。\x02",
    )

    CloseMessageWindow()

    label("loc_F93")

    Jump("loc_13BF")

    label("loc_F96")

    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    ChrTalk(    #6
        0xEE,
        "*模糊（blur）\x02",
    )

    Sleep(2000)
    OP_15(0x1F4)

    ChrTalk(    #7
        0xEE,
        "那么\x02",
    )

    Jump("loc_FD7")

    label("loc_FD7")

    CloseMessageWindow()
    Jump("loc_13BF")

    label("loc_FDB")

    ShowSaveMenu()
    Jump("loc_13BF")

    label("loc_FDF")

    Call(5, 43)
    Jump("loc_13BF")

    label("loc_FE6")

    Call(5, 44)
    Jump("loc_13BF")

    label("loc_FED")

    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x12B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x22AE)
    FadeToDark(500, 0, -1)
    ShowSaveMenu()
    OP_B4(0x1)
    Jump("loc_13BF")

    label("loc_1009")

    EventBegin(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_A3(0x0)

    label("loc_1013")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1256")
    FadeToDark(1000, 0, -1)
    OP_0D()

    AnonymousTalk(    #8
        (
            "\x06\x18\x07\x05※进行队伍的重新编组。\x01",
            "　更换队员，进行必要的装备变更，\x01",
            "　确定后，请选择【继续】。\x07\x00\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【编成队伍】\x01",      # 0
            "【变更装备】\x01",      # 1
            "【继续】\x01",          # 2
        )
    )

    Jump("loc_10C5")

    label("loc_10C5")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1135")
    OP_A2(0x0)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "　请选择２名固定成员以外的同行者。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    Jump("loc_1253")

    label("loc_1135")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_116E")
    OP_C0(0x13, 0x78, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_119B")

    label("loc_116E")


    AnonymousTalk(    #10
        "\x07\x05※进行队伍的编组之后再选择。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)

    label("loc_119B")

    Jump("loc_1253")

    label("loc_119E")

    SetChrName("")

    AnonymousTalk(    #11
        "\x06\x18\x07\x05继续事件发展，可以吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_11F3")

    label("loc_11F3")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1235")
    SetChrName("")

    AnonymousTalk(    #12
        "\x06\x18\x07\x05继续事件发展。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_1256")

    label("loc_1235")

    SetChrName("")

    AnonymousTalk(    #13
        "\x06\x18\x07\x05返回选择画面。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1256")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(0, 0)
    OP_0D()
    Jump("loc_13BF")

    label("loc_1253")

    Jump("loc_1013")

    label("loc_126C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1297")

    ChrTalk(    #14
        0x0,
        "从章节4进入。\x02",
    )

    OP_E3(0x0, 0x4, 32768, 0x0)
    Jump("loc_12AD")

    label("loc_1297")


    ChrTalk(    #15
        0x0,
        "从章节离开。\x02",
    )

    OP_E3(0x1, 0x0)

    label("loc_12AD")

    Jump("loc_13BF")

    label("loc_12B0")

    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    OP_D2(0x270112, 0x270122, 0x2)
    OP_D2(0x270520, 0x27052D, 0x3)
    OP_D2(0x270506, 0x270513, 0x4)
    OP_D2(0x27053A, 0x270547, 0x5)
    OP_D2(0x270370, 0x27037D, 0x6)
    OP_D2(0x7021A, 0x70226, 0x7)
    OP_D2(0x70232, 0x7023E, 0x8)
    OP_D2(0x7024A, 0x70256, 0x9)
    OP_D2(0x270178, 0x270185, 0xA)
    OP_D2(0x70328, 0x7032F, 0xB)
    OP_D2(0x702B6, 0x702BD, 0xC)
    OP_D2(0x702D4, 0x702DB, 0xD)
    OP_D2(0x2702C4, 0x2702CE, 0xE)
    OP_D2(0x2702D8, 0x2702E2, 0xF)
    OP_D2(0x27044A, 0x27044E, 0x10)
    OP_D2(0x270240, 0x27024A, 0x11)
    OP_D2(0x2906D9, 0x2906DD, 0x12)
    Jump("loc_13BF")

    label("loc_13B2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13BF")

    label("loc_13BF")

    Jump("loc_6EF")

    label("loc_13C2")

    OP_5F(0x0)
    OP_56(0x0)
    OP_DA()
    ClearMapFlags(0x80)
    Return()

    # Function_4_6AE end

    def Function_5_13CE(): pass

    label("Function_5_13CE")

    EventBegin(0x0)
    Sleep(1000)

    ChrTalk(    #16
        0x0,
        "组队变更后的事件\x02",
    )

    Sleep(2000)
    EventEnd(0x0)
    Return()

    # Function_5_13CE end

    def Function_6_13F4(): pass

    label("Function_6_13F4")


    AnonymousTalk(    #17
        "\x06请选择测试地图哦。\x02",
    )


    label("loc_140C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1476")

    Menu(
        1,
        10,
        100,
        1,
        (
            "测试地图20\x01",      # 0
            "测试地图21\x01",      # 1
            "取消\x01",            # 2
        )
    )

    Jump("loc_1443")

    label("loc_1443")

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1457"),
        (1, "loc_1460"),
        (SWITCH_DEFAULT, "loc_1469"),
    )


    label("loc_1457")

    NewScene("ED6_DT21/T0020   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1460")

    NewScene("ED6_DT21/T0021   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1469")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_140C")

    label("loc_1476")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_13F4 end

    def Function_7_1486(): pass

    label("Function_7_1486")

    SetChrName("商店君")

    AnonymousTalk(    #18
        "\x06哪个店？\x02",
    )

    Jump("loc_14B1")

    label("loc_14B1")


    Menu(
        1,
        10,
        100,
        1,
        (
            "据点商店\x01",                 # 0
            "普通商店\x01",                 # 1
            "据点工房\x01",                 # 2
            "工房\x01",                     # 3
            "旅店\x01",                     # 4
            "协会\x01",                     # 5
            "读书（利贝尔通讯1）\x01",      # 6
            "娱乐场交换处\x01",             # 7
            "全部石碑旗子\x01",             # 8
            "取消\x01",                     # 9
        )
    )

    Jump("loc_1553")

    label("loc_1553")

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_158B"),
        (1, "loc_1592"),
        (2, "loc_1599"),
        (3, "loc_15A0"),
        (4, "loc_15A7"),
        (5, "loc_15AE"),
        (6, "loc_15B5"),
        (7, "loc_15BD"),
        (8, "loc_15C4"),
        (SWITCH_DEFAULT, "loc_15EA"),
    )


    label("loc_158B")

    Call(0, 8)
    Jump("loc_15ED")

    label("loc_1592")

    Call(0, 9)
    Jump("loc_15ED")

    label("loc_1599")

    Call(0, 10)
    Jump("loc_15ED")

    label("loc_15A0")

    Call(0, 14)
    Jump("loc_15ED")

    label("loc_15A7")

    Call(0, 11)
    Jump("loc_15ED")

    label("loc_15AE")

    Call(0, 12)
    Jump("loc_15ED")

    label("loc_15B5")

    OP_B8(0x347, 0x0)
    Jump("loc_15ED")

    label("loc_15BD")

    Call(0, 13)
    Jump("loc_15ED")

    label("loc_15C4")

    OP_AA(0)
    OP_AA(256)
    OP_AA(512)
    OP_AA(768)
    OP_AA(1024)
    OP_AA(1280)
    OP_AA(1536)
    Jump("loc_15ED")

    label("loc_15EA")

    Jump("loc_15ED")

    label("loc_15ED")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_1486 end

    def Function_8_15F8(): pass

    label("Function_8_15F8")


    ChrTalk(    #19
        0x0,
        "欢迎光临据点商店！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0xA)
    Return()

    # Function_8_15F8 end

    def Function_9_1617(): pass

    label("Function_9_1617")


    ChrTalk(    #20
        0x0,
        "欢迎光临普通商店！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0xB)
    Return()

    # Function_9_1617 end

    def Function_10_1636(): pass

    label("Function_10_1636")


    ChrTalk(    #21
        0x0,
        "欢迎光临据点工房！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x0)
    Return()

    # Function_10_1636 end

    def Function_11_1655(): pass

    label("Function_11_1655")


    ChrTalk(    #22
        0x0,
        "欢迎光临旅店！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x5)
    Return()

    # Function_11_1655 end

    def Function_12_1670(): pass

    label("Function_12_1670")


    ChrTalk(    #23
        0x0,
        "欢迎光临游击士协会！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_2A(0x65, 0x66, 0x1, 0xFFFF)
    Return()

    # Function_12_1670 end

    def Function_13_1698(): pass

    label("Function_13_1698")


    ChrTalk(    #24
        0x0,
        "这里是交换所。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x69)
    Return()

    # Function_13_1698 end

    def Function_14_16B3(): pass

    label("Function_14_16B3")


    ChrTalk(    #25
        0x0,
        "欢迎\x02",
    )

    Jump("loc_16C4")

    label("loc_16C4")

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x1)
    Return()

    # Function_14_16B3 end

    def Function_15_16CA(): pass

    label("Function_15_16CA")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    OP_51(0x23, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x23, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1762")
    Jump("loc_17A4")

    label("loc_1762")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_177E")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17A4")

    label("loc_177E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_179A")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17A4")

    label("loc_179A")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17A4")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x23, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x23, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #26
        0xFE,
        "啊啊\x02",
    )

    Jump("loc_17DA")

    label("loc_17DA")

    CloseMessageWindow()
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)
    Return()

    # Function_15_16CA end

    SaveToFile()

Try(main)
