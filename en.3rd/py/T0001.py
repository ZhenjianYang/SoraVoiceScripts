from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Villager 1',                           # 9
        'Villager 1',                           # 10
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
        'Treasure Chest',                       # 28
        'Sitting',                              # 29
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
        "Function_5_137C",         # 05, 5
        "Function_6_13AC",         # 06, 6
        "Function_7_1448",         # 07, 7
        "Function_8_1574",         # 08, 8
        "Function_9_1598",         # 09, 9
        "Function_10_15BE",        # 0A, 10
        "Function_11_15E5",        # 0B, 11
        "Function_12_1603",        # 0C, 12
        "Function_13_162A",        # 0D, 13
        "Function_14_164A",        # 0E, 14
        "Function_15_165D",        # 0F, 15
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
    OP_57(0x0, 0x0, 0x12, "#1CTest Menu")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1370")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Test Maps\x01",                    # 0
            "Game Maps\x01",                    # 1
            "Characters\x01",                   # 2
            "Monsters\x01",                     # 3
            "Battle\x01",                       # 4
            "Battle (Algorithm Test)\x01",      # 5
            "Battle (Map Check)\x01",           # 6
            "Minigames\x01",                    # 7
            "Events\x01",                       # 8
            "Episodes\x01",                     # 9
            "Shop Test\x01",                    # 10
            "Character Art Change\x01",         # 11
            "Trap Land\x01",                    # 12
            "Portraits\x01",                    # 13
            "Party Select Menu\x01",            # 14
            "Blur\x01",                         # 15
            "Save Menu\x01",                    # 16
            "Set all handbook flags\x01",       # 17
            "Get all recipes\x01",              # 18
            "Game Clear\x01",                   # 19
            "Camp Menu\x01",                    # 20
            "Episode Test\x01",                 # 21
            "Stress Test\x01",                  # 22
            "Cancel\x01",                       # 23
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_892"),
        (1, "loc_899"),
        (2, "loc_8A0"),
        (3, "loc_8A7"),
        (4, "loc_8AE"),
        (5, "loc_8B5"),
        (6, "loc_8BC"),
        (7, "loc_8C3"),
        (8, "loc_8CA"),
        (9, "loc_8D1"),
        (10, "loc_8D8"),
        (11, "loc_8E4"),
        (12, "loc_A78"),
        (13, "loc_A84"),
        (14, "loc_CE3"),
        (15, "loc_F6E"),
        (16, "loc_FA0"),
        (17, "loc_FA4"),
        (18, "loc_FAB"),
        (19, "loc_FB2"),
        (20, "loc_FCE"),
        (21, "loc_1214"),
        (22, "loc_125E"),
        (SWITCH_DEFAULT, "loc_1360"),
    )


    label("loc_892")

    Call(0, 6)
    Jump("loc_136D")

    label("loc_899")

    Call(3, 8)
    Jump("loc_136D")

    label("loc_8A0")

    Call(3, 0)
    Jump("loc_136D")

    label("loc_8A7")

    Call(3, 4)
    Jump("loc_136D")

    label("loc_8AE")

    Call(2, 0)
    Jump("loc_136D")

    label("loc_8B5")

    Call(1, 0)
    Jump("loc_136D")

    label("loc_8BC")

    Call(2, 1)
    Jump("loc_136D")

    label("loc_8C3")

    Call(2, 17)
    Jump("loc_136D")

    label("loc_8CA")

    Call(4, 2)
    Jump("loc_136D")

    label("loc_8D1")

    Call(5, 0)
    Jump("loc_136D")

    label("loc_8D8")

    OP_5F(0x0)
    OP_56(0x0)
    Call(0, 7)
    Jump("loc_136D")

    label("loc_8E4")


    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Estelle (SC), Joshua (SC)\x01",      # 0
            "Estelle (FC), Joshua (FC)\x01",      # 1
            "Joshua (Without Stigma)\x01",        # 2
            "Joshua (3rd)\x01",                   # 3
            "Scherazard (Age 18)\x01",            # 4
            "Scherazard (3rd)\x01",               # 5
            "Scherazard (FC)\x01",                # 6
            "Olivier (3rd)\x01",                  # 7
            "Olivier (FC)\x01",                   # 8
            "Kloe (Formal)\x01",                  # 9
            "Kloe (Uniform)\x01",                 # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9EB"),
        (1, "loc_9FC"),
        (2, "loc_A0D"),
        (3, "loc_A17"),
        (4, "loc_A21"),
        (5, "loc_A2B"),
        (6, "loc_A35"),
        (7, "loc_A3F"),
        (8, "loc_A49"),
        (9, "loc_A53"),
        (10, "loc_A5D"),
        (SWITCH_DEFAULT, "loc_A67"),
    )


    label("loc_9EB")

    OP_BB(0x0, 0x1, 0x0)
    OP_BB(0x1, 0x1, 0x1)
    Jump("loc_A67")

    label("loc_9FC")

    OP_BB(0x0, 0x1, 0x1E)
    OP_BB(0x1, 0x1, 0x1F)
    Jump("loc_A67")

    label("loc_A0D")

    OP_BB(0x1, 0x1, 0x1C)
    Jump("loc_A67")

    label("loc_A17")

    OP_BB(0x1, 0x1, 0x1A)
    Jump("loc_A67")

    label("loc_A21")

    OP_BB(0x2, 0x1, 0x18)
    Jump("loc_A67")

    label("loc_A2B")

    OP_BB(0x2, 0x1, 0x19)
    Jump("loc_A67")

    label("loc_A35")

    OP_BB(0x2, 0x1, 0x2)
    Jump("loc_A67")

    label("loc_A3F")

    OP_BB(0x3, 0x1, 0x1B)
    Jump("loc_A67")

    label("loc_A49")

    OP_BB(0x3, 0x1, 0x3)
    Jump("loc_A67")

    label("loc_A53")

    OP_BB(0x4, 0x1, 0x1D)
    Jump("loc_A67")

    label("loc_A5D")

    OP_BB(0x4, 0x1, 0x4)
    Jump("loc_A67")

    label("loc_A67")

    OP_5F(0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_BD()
    Jump("loc_136D")

    label("loc_A78")

    NewScene("ED6_DT21/A0019   ._SN", 0, 0, 0)
    IdleLoop()
    Jump("loc_136D")

    label("loc_A84")

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
        "わお\x02",
    )

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
    Jump("loc_136D")

    label("loc_CE3")

    OP_5F(0x0)
    OP_56(0x0)

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Organize 1 Team (w/Cancel)\x01",                           # 0
            "Organize 1 Team (Kevin, Ries) (w/Cancel)\x01",             # 1
            "Organize 1 Team (Kevin)\x01",                              # 2
            "Organize 1 Team (Joshua) (w/Cancel)\x01",                  # 3
            "Organize 2 Teams (Kevin, Ries)\x01",                       # 4
            "Organize 4 Teams (Kevin, Ries)\x01",                       # 5
            "Organize 4 Teams (Kevin, Ries, Estelle, Joshua)\x01",      # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E07"),
        (1, "loc_E1E"),
        (2, "loc_E35"),
        (3, "loc_E4C"),
        (4, "loc_E63"),
        (5, "loc_E7A"),
        (6, "loc_E91"),
        (SWITCH_DEFAULT, "loc_EA8"),
    )


    label("loc_E07")

    OP_DD(0x1, 0x0, 0x1, 0, 0, 0, 0)
    Jump("loc_EA8")

    label("loc_E1E")

    OP_DD(0x1, 0x0, 0x1, 16640, 0, 0, 0)
    Jump("loc_EA8")

    label("loc_E35")

    OP_DD(0x1, 0x0, 0x0, 256, 0, 0, 0)
    Jump("loc_EA8")

    label("loc_E4C")

    OP_DD(0x1, 0x0, 0x1, 2, 0, 0, 0)
    Jump("loc_EA8")

    label("loc_E63")

    OP_DD(0x2, 0x1, 0x0, 256, 16384, 0, 0)
    Jump("loc_EA8")

    label("loc_E7A")

    OP_DD(0x4, 0x0, 0x1, 0, 0, 0, 16640)
    Jump("loc_EA8")

    label("loc_E91")

    OP_DD(0x4, 0x0, 0x1, 256, 16384, 1, 2)
    Jump("loc_EA8")

    label("loc_EA8")

    OP_5F(0x2)
    OP_DF(0x0, 0x1, 0x1)
    OP_E0(265, 0x40, 0x2)
    OP_E0(265, 0x41, 0x3)
    OP_E0(271, 0x42, 0x2)
    OP_E0(271, 0x43, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE0")

    ChrTalk(    #1
        0x0,
        "Estelle\x02",
    )

    Jump("loc_EEB")

    label("loc_EE0")


    ChrTalk(    #2
        0x0,
        "Aaaah!\x02",
    )


    label("loc_EEB")

    CloseMessageWindow()
    ClearChrFlags(0x4, 0x8)
    SetChrChipByIndex(0x4, 3)
    OP_8E(0x4, 0xFA0, 0x0, 0xFA0, 0x1388, 0x0)

    ChrTalk(    #3
        0x4,
        "Aah.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E1(0x6, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F3C")

    ChrTalk(    #4
        0x0,
        "Tita is in party 1.\x02",
    )

    CloseMessageWindow()

    label("loc_F3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E1(0x6, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6B")

    ChrTalk(    #5
        0x0,
        "Tita is in Party 1, slot 1.\x02",
    )

    CloseMessageWindow()

    label("loc_F6B")

    Jump("loc_136D")

    label("loc_F6E")

    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)

    ChrTalk(    #6
        0xEE,
        "Blur\x02",
    )

    Sleep(2000)
    OP_15(0x1F4)

    ChrTalk(    #7
        0xEE,
        "Off!\x02",
    )

    CloseMessageWindow()
    Jump("loc_136D")

    label("loc_FA0")

    ShowSaveMenu()
    Jump("loc_136D")

    label("loc_FA4")

    Call(5, 43)
    Jump("loc_136D")

    label("loc_FAB")

    Call(5, 44)
    Jump("loc_136D")

    label("loc_FB2")

    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x12B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x22AE)
    FadeToDark(500, 0, -1)
    ShowSaveMenu()
    OP_B4(0x1)
    Jump("loc_136D")

    label("loc_FCE")

    EventBegin(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_A3(0x0)

    label("loc_FD8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11FE")
    FadeToDark(1000, 0, -1)
    OP_0D()

    AnonymousTalk(    #8
        (
            "\x06\x18\x07\x05* Reorganizing party.\x01",
            "  Select your members, make any necessary changes,\x01",
            "  and then select Proceed to continue.\x07\x00\x02",
        )
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Organize Party\x01",        # 0
            "Change Equipment\x01",      # 1
            "Proceed\x01",               # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1106")
    OP_A2(0x0)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05* Reorganizing party.\x01",
            "  Please select your members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    Jump("loc_11FB")

    label("loc_1106")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1172")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_113F")
    OP_C0(0x13, 0x78, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_116F")

    label("loc_113F")


    AnonymousTalk(    #10
        "\x07\x05* Please select your party first.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)

    label("loc_116F")

    Jump("loc_11FB")

    label("loc_1172")

    SetChrName("")

    AnonymousTalk(    #11
        "\x06\x18\x07\x05Proceed?\x07\x00\x02",
    )

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
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11DB")
    SetChrName("")

    AnonymousTalk(    #12
        "\x06\x18\x07\x05Proceeding.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_11FE")

    label("loc_11DB")

    SetChrName("")

    AnonymousTalk(    #13
        "\x06\x18\x07\x05Returning to menu.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_11FE")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(0, 0)
    OP_0D()
    Jump("loc_136D")

    label("loc_11FB")

    Jump("loc_FD8")

    label("loc_1214")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1243")

    ChrTalk(    #14
        0x0,
        "Entering Episode 4.\x02",
    )

    OP_E3(0x0, 0x4, 32768, 0x0)
    Jump("loc_125B")

    label("loc_1243")


    ChrTalk(    #15
        0x0,
        "Exiting episode.\x02",
    )

    OP_E3(0x1, 0x0)

    label("loc_125B")

    Jump("loc_136D")

    label("loc_125E")

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
    Jump("loc_136D")

    label("loc_1360")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_136D")

    label("loc_136D")

    Jump("loc_6F0")

    label("loc_1370")

    OP_5F(0x0)
    OP_56(0x0)
    OP_DA()
    ClearMapFlags(0x80)
    Return()

    # Function_4_6AE end

    def Function_5_137C(): pass

    label("Function_5_137C")

    EventBegin(0x0)
    Sleep(1000)

    ChrTalk(    #16
        0x0,
        "Select party for this event.\x02",
    )

    Sleep(2000)
    EventEnd(0x0)
    Return()

    # Function_5_137C end

    def Function_6_13AC(): pass

    label("Function_6_13AC")


    AnonymousTalk(    #17
        "\x06テストマップを選んでくださいよ。\x02",
    )


    label("loc_13D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1438")

    Menu(
        1,
        10,
        100,
        1,
        (
            "Test Map 20\x01",      # 0
            "Test Map 21\x01",      # 1
            "Cancel\x01",           # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1419"),
        (1, "loc_1422"),
        (SWITCH_DEFAULT, "loc_142B"),
    )


    label("loc_1419")

    NewScene("ED6_DT21/T0020   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_1422")

    NewScene("ED6_DT21/T0021   ._SN", 0, 0, 0)
    IdleLoop()

    label("loc_142B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13D0")

    label("loc_1438")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_13AC end

    def Function_7_1448(): pass

    label("Function_7_1448")

    SetChrName("Shop-chan")

    AnonymousTalk(    #18
        "\x06Which shop?\x02",
    )


    Menu(
        1,
        10,
        100,
        1,
        (
            "Base Shop\x01",            # 0
            "Normal Shop\x01",          # 1
            "Base Factory\x01",         # 2
            "Factory\x01",              # 3
            "Inn\x01",                  # 4
            "Guild\x01",                # 5
            "Read Book\x01",            # 6
            "Casino Exchange\x01",      # 7
            "All Monuments\x01",        # 8
            "Cancel\x01",               # 9
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1507"),
        (1, "loc_150E"),
        (2, "loc_1515"),
        (3, "loc_151C"),
        (4, "loc_1523"),
        (5, "loc_152A"),
        (6, "loc_1531"),
        (7, "loc_1539"),
        (8, "loc_1540"),
        (SWITCH_DEFAULT, "loc_1566"),
    )


    label("loc_1507")

    Call(0, 8)
    Jump("loc_1569")

    label("loc_150E")

    Call(0, 9)
    Jump("loc_1569")

    label("loc_1515")

    Call(0, 10)
    Jump("loc_1569")

    label("loc_151C")

    Call(0, 14)
    Jump("loc_1569")

    label("loc_1523")

    Call(0, 11)
    Jump("loc_1569")

    label("loc_152A")

    Call(0, 12)
    Jump("loc_1569")

    label("loc_1531")

    OP_B8(0x347, 0x0)
    Jump("loc_1569")

    label("loc_1539")

    Call(0, 13)
    Jump("loc_1569")

    label("loc_1540")

    OP_AA(0)
    OP_AA(256)
    OP_AA(512)
    OP_AA(768)
    OP_AA(1024)
    OP_AA(1280)
    OP_AA(1536)
    Jump("loc_1569")

    label("loc_1566")

    Jump("loc_1569")

    label("loc_1569")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_1448 end

    def Function_8_1574(): pass

    label("Function_8_1574")


    ChrTalk(    #19
        0x0,
        "Welcome to the Base Shop!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0xA)
    Return()

    # Function_8_1574 end

    def Function_9_1598(): pass

    label("Function_9_1598")


    ChrTalk(    #20
        0x0,
        "Welcome to the Normal Shop!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0xB)
    Return()

    # Function_9_1598 end

    def Function_10_15BE(): pass

    label("Function_10_15BE")


    ChrTalk(    #21
        0x0,
        "Welcome to the Base Factory!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x0)
    Return()

    # Function_10_15BE end

    def Function_11_15E5(): pass

    label("Function_11_15E5")


    ChrTalk(    #22
        0x0,
        "Welcome to the Inn!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x5)
    Return()

    # Function_11_15E5 end

    def Function_12_1603(): pass

    label("Function_12_1603")


    ChrTalk(    #23
        0x0,
        "Welcome to the Guild!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_2A(0x65, 0x66, 0x1, 0xFFFF)
    Return()

    # Function_12_1603 end

    def Function_13_162A(): pass

    label("Function_13_162A")


    ChrTalk(    #24
        0x0,
        "This is the exchange.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x69)
    Return()

    # Function_13_162A end

    def Function_14_164A(): pass

    label("Function_14_164A")


    ChrTalk(    #25
        0x0,
        "Welcome!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A9(0x1)
    Return()

    # Function_14_164A end

    def Function_15_165D(): pass

    label("Function_15_165D")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16F5")
    Jump("loc_1737")

    label("loc_16F5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1711")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1737")

    label("loc_1711")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_172D")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1737")

    label("loc_172D")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1737")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x23, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x23, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    ChrTalk(    #26
        0xFE,
        "Ah.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    ClearChrFlags(0xFE, 0x10)
    Return()

    # Function_15_165D end

    SaveToFile()

Try(main)
