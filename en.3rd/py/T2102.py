from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2102   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        'Middle Aged Man',                      # 9
        'Middle Aged Woman',                    # 10
        'Child and Man',                        # 11
        'Santos',                               # 12
        'Noble Middle-Aged Man',                # 13
        'Noble Girl',                           # 14
        'Hardt',                                # 15
        'Linde',                                # 16
        'Linde (Shadow)',                       # 17
        'Child',                                # 18
        'Noble Woman',                          # 19
        'Noble Man',                            # 20
        'Sender',                               # 21
        'Kanone',                               # 22
        'Sieg',                                 # 23
        'Target Camera',                        # 24
        'Ruan - North Block',                   # 25
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
        'ED6_DT07/CH01100 ._CH',             # 00
        'ED6_DT07/CH01020 ._CH',             # 01
        'ED6_DT07/CH01160 ._CH',             # 02
        'ED6_DT07/CH01660 ._CH',             # 03
        'ED6_DT07/CH01130 ._CH',             # 04
        'ED6_DT07/CH01210 ._CH',             # 05
        'ED6_DT07/CH01030 ._CH',             # 06
        'ED6_DT07/CH01290 ._CH',             # 07
        'ED6_DT07/CH02590 ._CH',             # 08
        'ED6_DT07/CH02500 ._CH',             # 09
        'ED6_DT07/CH02630 ._CH',             # 0A
        'ED6_DT07/CH02640 ._CH',             # 0B
        'ED6_DT07/CH02390 ._CH',             # 0C
        'ED6_DT07/CH02550 ._CH',             # 0D
        'ED6_DT07/CH02570 ._CH',             # 0E
        'ED6_DT07/CH02600 ._CH',             # 0F
        'ED6_DT07/CH01450 ._CH',             # 10
        'ED6_DT07/CH01450 ._CH',             # 11
        'ED6_DT07/CH01470 ._CH',             # 12
        'ED6_DT07/CH01120 ._CH',             # 13
        'ED6_DT07/CH01660 ._CH',             # 14
        'ED6_DT07/CH01470 ._CH',             # 15
        'ED6_DT07/CH01200 ._CH',             # 16
        'ED6_DT07/CH01180 ._CH',             # 17
        'ED6_DT07/CH01310 ._CH',             # 18
        'ED6_DT26/CH20797 ._CH',             # 19
        'ED6_DT07/CH02320 ._CH',             # 1A
        'ED6_DT07/CH02323 ._CH',             # 1B
        'ED6_DT26/CH20799 ._CH',             # 1C
        'ED6_DT26/CH20254 ._CH',             # 1D
        'ED6_DT26/CH20798 ._CH',             # 1E
    )

    AddCharChipPat(
        'ED6_DT07/CH01100P._CP',             # 00
        'ED6_DT07/CH01020P._CP',             # 01
        'ED6_DT07/CH01160P._CP',             # 02
        'ED6_DT07/CH01660P._CP',             # 03
        'ED6_DT07/CH01130P._CP',             # 04
        'ED6_DT07/CH01210P._CP',             # 05
        'ED6_DT07/CH01030P._CP',             # 06
        'ED6_DT07/CH01290P._CP',             # 07
        'ED6_DT07/CH02590P._CP',             # 08
        'ED6_DT07/CH02500P._CP',             # 09
        'ED6_DT07/CH02630P._CP',             # 0A
        'ED6_DT07/CH02640P._CP',             # 0B
        'ED6_DT07/CH02390P._CP',             # 0C
        'ED6_DT07/CH02550P._CP',             # 0D
        'ED6_DT07/CH02570P._CP',             # 0E
        'ED6_DT07/CH02600P._CP',             # 0F
        'ED6_DT07/CH01450P._CP',             # 10
        'ED6_DT07/CH01450P._CP',             # 11
        'ED6_DT07/CH01470P._CP',             # 12
        'ED6_DT07/CH01120P._CP',             # 13
        'ED6_DT07/CH01660P._CP',             # 14
        'ED6_DT07/CH01470P._CP',             # 15
        'ED6_DT07/CH01200P._CP',             # 16
        'ED6_DT07/CH01180P._CP',             # 17
        'ED6_DT07/CH01310P._CP',             # 18
        'ED6_DT26/CH20797P._CP',             # 19
        'ED6_DT07/CH02320P._CP',             # 1A
        'ED6_DT07/CH02323P._CP',             # 1B
        'ED6_DT26/CH20799P._CP',             # 1C
        'ED6_DT26/CH20254P._CP',             # 1D
        'ED6_DT26/CH20798P._CP',             # 1E
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Direction           = 180,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
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
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
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
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x1C5,
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

    DeclNpc(
        X                   = 71170,
        Z                   = 0,
        Y                   = 80860,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 108610,
        TriggerZ            = 6150,
        TriggerY            = 96910,
        TriggerRange        = 800,
        ActorX              = 108610,
        ActorZ              = 8350,
        ActorY              = 96910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 127080,
        TriggerZ            = 6150,
        TriggerY            = 100740,
        TriggerRange        = 800,
        ActorX              = 127080,
        ActorZ              = 8350,
        ActorY              = 100740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 122620,
        TriggerZ            = 400,
        TriggerY            = 100640,
        TriggerRange        = 800,
        ActorX              = 122620,
        ActorZ              = 1600,
        ActorY              = 100640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 140870,
        TriggerZ            = 1000,
        TriggerY            = 108000,
        TriggerRange        = 800,
        ActorX              = 140870,
        ActorZ              = 2000,
        ActorY              = 108000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 149330,
        TriggerZ            = 1000,
        TriggerY            = 108000,
        TriggerRange        = 800,
        ActorX              = 149330,
        ActorZ              = 2000,
        ActorY              = 108000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 103030,
        TriggerZ            = 1000,
        TriggerY            = 108000,
        TriggerRange        = 800,
        ActorX              = 103030,
        ActorZ              = 2000,
        ActorY              = 108000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 96980,
        TriggerZ            = 1000,
        TriggerY            = 108000,
        TriggerRange        = 800,
        ActorX              = 96980,
        ActorZ              = 2000,
        ActorY              = 108000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4BE",          # 00, 0
        "Function_1_500",          # 01, 1
        "Function_2_543",          # 02, 2
        "Function_3_6C0",          # 03, 3
        "Function_4_3451",         # 04, 4
        "Function_5_3492",         # 05, 5
        "Function_6_34BF",         # 06, 6
        "Function_7_3515",         # 07, 7
        "Function_8_4DB7",         # 08, 8
        "Function_9_4DF8",         # 09, 9
        "Function_10_4E29",        # 0A, 10
        "Function_11_4E5F",        # 0B, 11
        "Function_12_4EAC",        # 0C, 12
        "Function_13_4ED6",        # 0D, 13
        "Function_14_4F38",        # 0E, 14
        "Function_15_4F79",        # 0F, 15
        "Function_16_4FDA",        # 10, 16
        "Function_17_5029",        # 11, 17
        "Function_18_5094",        # 12, 18
        "Function_19_5113",        # 13, 19
    )


    def Function_0_4BE(): pass

    label("Function_0_4BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_4E0")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 7)
    Jump("loc_4FF")

    label("loc_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_4FF")
    OP_A3(0x2504)
    OP_A2(0x0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_4FF")

    Return()

    # Function_0_4BE end

    def Function_1_500(): pass

    label("Function_1_500")

    OP_16(0x2, 0xFA0, 0x4E20, 0xFFFF63C0, 0x230049)
    OP_22(0x1C5, 0x1, 0x64)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_542")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_539")
    OP_A3(0x0)
    OP_B1("T2102_1")
    Jump("loc_542")

    label("loc_539")

    OP_B1("T2102_0")

    label("loc_542")

    Return()

    # Function_1_500 end

    def Function_2_543(): pass

    label("Function_2_543")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_568")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_6AA")

    label("loc_568")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_581")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_6AA")

    label("loc_581")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59A")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_6AA")

    label("loc_59A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B3")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_6AA")

    label("loc_5B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CC")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_6AA")

    label("loc_5CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E5")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_6AA")

    label("loc_5E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FE")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_6AA")

    label("loc_5FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_617")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_6AA")

    label("loc_617")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_630")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_6AA")

    label("loc_630")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_649")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_6AA")

    label("loc_649")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_662")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_6AA")

    label("loc_662")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_6AA")

    label("loc_67B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_694")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_6AA")

    label("loc_694")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AA")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_6AA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6BF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_6AA")

    label("loc_6BF")

    Return()

    # Function_2_543 end

    def Function_3_6C0(): pass

    label("Function_3_6C0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    ClearMapFlags(0x100000)
    OP_22(0x1C3, 0x1, 0x64)
    OP_24(0x1C9, 0x64)
    LoadEffect(0x0, "map\\\\mp014_00.eff")
    OP_11(0x0, 0x0, 0x0, 0x80E8, 0x1FBD0, 0x0)
    OP_6D(91700, 0, 82840, 0)
    OP_67(0, 4740, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(60000, 0)
    OP_6E(370, 0)
    SetChrPos(0x10C, 70280, 0, 81000, 90)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 97560, 0, 103740, 180)
    PlayEffect(0x0, 0xFF, 0xFF, 97560, 0, 102700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 94660, 0, 81000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_43(0x10C, 0x3, 0x0, 0x4)
    Sleep(3500)

    def lambda_7F6():
        OP_6D(98540, 1000, 90480, 4000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_7F6)

    def lambda_80E():
        OP_67(0, 6880, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_80E)

    def lambda_826():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_826)

    def lambda_836():
        OP_6E(238, 4000)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_836)
    WaitChrThread(0x1F, 0x0)
    WaitChrThread(0x10C, 0x3)

    NpcTalk(    #0
        0x1C,
        "Man's Voice",
        "...I've been waiting for you.\x02",
    )

    CloseMessageWindow()

    def lambda_87F():
        OP_6D(99400, 0, 103440, 2500)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_87F)

    def lambda_897():
        OP_67(0, 4240, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_897)

    def lambda_8AF():
        OP_6C(50000, 2500)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_8AF)
    WaitChrThread(0x1F, 0x0)
    OP_82(0x2, 0x2)
    SetChrPos(0x10C, 97560, 1000, 93000, 0)

    def lambda_8D8():
        OP_8E(0xFE, 0x17D18, 0x0, 0x1881C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_8D8)
    WaitChrThread(0x10C, 0x1)
    Sleep(300)

    ChrTalk(    #1
        0x10C,
        "#1855F...So it was you, Sender.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x1C,
        (
            "#5PIndeed. It's good to see you again, Colonel.\x02\x03",

            "I'm pleased to see you're still well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10C,
        (
            "#1851FI'm not a colonel anymore, Sender.\x02\x03",

            "#1859FThough I feel as though saying as much has\x01",
            "become a hobby. No one around me seems\x01",
            "willing to correct themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x1C,
        (
            "#5POh, I'm aware. But today, I intend to address\x01",
            "you as Colonel nonetheless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10C,
        "#1853F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x1C,
        (
            "#5PI called you here because I have something\x01",
            "that I need to ask you.\x02\x03",

            "I hope you can forgive me for forcing you to\x01",
            "come out here with the weather so poor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10C,
        (
            "#1855FIf I can answer your questions, I will. \x02\x03",

            "#1851FDon't feel as if you need to hold back on my\x01",
            "account.\x02\x03",

            "If you can't accept something in the answer \x01",
            "I give you, by all means say so.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x1C)
    Sleep(500)

    ChrTalk(    #8
        0x1C,
        "#5PThen I'll get straight to the point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x1C,
        "#5PWhy did you leave the army behind, Colonel?\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #10
        0x1C,
        "#5P#3SWhat happened to your love for your country?!#2S\x02",
    )

    OP_7C(0x0, 0xFA, 0xFA0, 0x96)
    CloseMessageWindow()
    FadeToDark(10, 16777215, -1)
    OP_0D()
    PlayEffect(0x0, 0x1, 0xFF, 97560, 0, 102700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    OP_22(0x169, 0x0, 0x64)
    Sleep(1000)
    FadeToBright(2000, 16777215)
    OP_0D()
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10C)
    Sleep(500)

    ChrTalk(    #11
        0x10C,
        (
            "#1859FI see you, at least, returned to the military.\x02\x03",

            "#1850F...I was relieved to see that, in truth.\x02\x03",

            "#1856FYou were always an exceptionally capable soldier, \x01",
            "even back in the military academy. If you hadn't\x01",
            "had the misfortune of meeting me...\x02\x03",

            "#1855FIf you hadn't had the misfortune of being caught\x01",
            "up in my foolishness, you would probably be a\x01",
            "field officer by now.\x02\x03",

            "...I'm truly sorry about what I did to you.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #12
        0x1C,
        (
            "#5PPlease don't get me wrong, Colonel. I don't in any\x01",
            "way blame you or harbor resentment for what you\x01",
            "did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x1C,
        (
            "#5PYou thought about what was best for this country\x01",
            "more than anyone else I know. Your patriotism was\x01",
            "genuine and heartfelt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x1C,
        (
            "#5PI don't regret following you at all.\x01",
            "I'm honored that I could.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x1C,
        (
            "#5PIt's certainly true that doing so has become a\x01",
            "significant obstacle in my chances of promotion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x1C,
        "#5P...but I couldn't care less about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x1C,
        (
            "#5PAs long as I can continue to serve in the\x01",
            "military--to serve the country I love with\x01",
            "all my heart--I am happy. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x1C,
        (
            "#5PKnow that I harbor no ill feelings towards\x01",
            "you regarding the past.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #19
        0x1C,
        "#5P...But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x1C,
        "#5PWhat are you doing now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x1C,
        (
            "#5PYou used to worry for this country's future more\x01",
            "than any of us... You cared for it more than any\x01",
            "other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x1C,
        (
            "#5P...Yet instead of picking yourself up and trying\x01",
            "to work for your nation again, you left the army\x01",
            "behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x1C,
        (
            "#5PAnd now you're running some sort of company\x01",
            "that deals with the rich?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #24
        0x1C,
        "#5P#4SJust what happened to your patriotism?!#2S\x02",
    )

    OP_7C(0x0, 0x190, 0xFA0, 0xC8)
    CloseMessageWindow()
    FadeToDark(10, 16777215, -1)
    OP_0D()
    Sleep(200)
    OP_6D(97560, 0, 104600, 0)
    OP_67(0, 3900, -10000, 0)
    OP_6B(3560, 0)
    OP_6C(0, 0)
    OP_6E(238, 0)
    SetChrPos(0x10C, 97560, 0, 99580, 0)
    OP_22(0x169, 0x0, 0x64)
    Sleep(1000)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #25
        0x1C,
        "#5PI beg of you: return to the military.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x1C,
        (
            "#5PYou're a capable man. Those skills of yours\x01",
            "would be a valuable asset to the force,\x01",
            "and it's where you should be using them!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10C)
    Sleep(500)

    ChrTalk(    #27
        0x10C,
        (
            "#1855FI'm sorry, Sender.\x02\x03",

            "I cannot ever return to the army again.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #28
        0x1C,
        "#5P#40W...Why?\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #29
        0x1C,
        "#5P#3SWhy, Colonel?!#2S\x02",
    )

    OP_7C(0x0, 0x12C, 0xFA0, 0x64)
    CloseMessageWindow()
    OP_22(0x169, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #30
        0x1C,
        (
            "#5PYou've repented more than enough for your\x01",
            "actions!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x1C,
        (
            "#5PBoth General Morgan and Brigadier General Bright\x01",
            "actively desire your return!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x1C,
        (
            "#5PI and all of the other soldiers in my position would\x01",
            "be overjoyed to have you in our ranks again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x1C,
        (
            "#5PSo why? Why do you look at me with that sad\x01",
            "expression and tell me that it's not possible?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x1C,
        "#5PWhy would you apologize to me?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10C,
        (
            "#1856F...Make no mistake, Sender. I haven't abandoned\x01",
            "my love for my country; it burns as brightly in\x01",
            "my heart as it ever did.\x02\x03",

            "But what I did was...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10C)
    Sleep(500)

    ChrTalk(    #36
        0x10C,
        (
            "#1855FWhat I did was truly terrible.\x02\x03",

            "I organized a coup d'etat, destabilizing this\x01",
            "nation and disrupting the lives of countless\x01",
            "people.\x02\x03",

            "Thanks to the help of all those around me,\x01",
            "I was able to realize what a foolish mistake\x01",
            "I made...\x02\x03",

            "#1858FAnd yet in my heart, I feel exactly the same\x01",
            "way I always did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x1C,
        "#5PI'm...not sure what you mean.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10C,
        (
            "#1856FIn spite of all that happened, my love for\x01",
            "my country is unchanged.\x02\x03",

            "I still feel the blind desire to do anything\x01",
            "I can to aid Liberl, no matter how reckless\x01",
            "or dangerous it may be...\x02\x03",

            "#1855FI'm the same man I was when I plotted that\x01",
            "coup d'etat. Not a thing has changed.\x02\x03",

            "...That thought, Sender, terrifies me.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x1C)
    Sleep(500)
    WaitChrThread(0x1F, 0x0)

    ChrTalk(    #39
        0x1C,
        (
            "#5P#30W...Th... Then...\x02\x03",

            "#20W#5PYou didn't leave the military because you had\x01",
            "lost your love for your country...\x02\x03",

            "#5PYou're saying that you left it BECAUSE you still \x01",
            "love your country?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10C,
        (
            "#1855FForgive me... I have no right to be making excuses\x01",
            "to you and trying to justify myself.\x02\x03",

            "#1856FNot after I dragged all of you down with me and\x01",
            "ruined your lives forever.\x02\x03",

            "I truly am sorry for what I did to you and all of\x01",
            "the other members of the division.\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x1, 0x2)

    def lambda_1BF5():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_1BF5)
    Sleep(1000)

    ChrTalk(    #41
        0x1C,
        (
            "#5P...\x02\x03",

            "#5PY-You...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x1C,
        "#5PNo, you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10C,
        (
            "#1852F...Please don't misunderstand.\x02\x03",

            "I didn't leave the army in an attempt to run\x01",
            "from my own weakness. \x02\x03",

            "Nor did I leave it because I was ashamed of\x01",
            "the treatment I received for my actions.\x02\x03",

            "#1855FAfter what happened, I thought long and hard\x01",
            "about what I should have done instead of what\x01",
            "I did.\x02\x03",

            "Trying to work out where I'd gone wrong...\x02\x03",

            "#1852FAs I did that, I noticed something. Something\x01",
            "vitally important that I had failed to realize up\x01",
            "until that point.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x10C, 0x0, 0x0, 0x6)

    def lambda_1E1A():
        OP_6D(99200, 0, 104280, 28000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_1E1A)

    def lambda_1E32():
        OP_6C(45000, 28000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_1E32)

    def lambda_1E42():
        OP_6B(3900, 28000)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_1E42)

    def lambda_1E52():
        OP_8E(0xFE, 0x17D18, 0x0, 0x18C40, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1E52)
    WaitChrThread(0x10C, 0x1)
    OP_8C(0x10C, 270, 400)
    Sleep(300)

    ChrTalk(    #44
        0x10C,
        (
            "#1856F#12PAfter setting up the Intelligence Division, I began\x01",
            "gathering information and using it to protect Liberl.\x02\x03",

            "Yet thinking about it now, I didn't know the first\x01",
            "thing about the nature of information at the time.\x02\x03",

            "#1855FInformation isn't something that exists alone.\x01",
            "It only exists when people use it and see it as\x01",
            "something of worth.\x02\x03",

            "Furthermore, the value of that information can\x01",
            "change radically depending on the position and\x01",
            "perspective of those who look at it.\x02\x03",

            "#1856FI can't help but wonder if overlooking this simple\x01",
            "fact was what caused my patriotism to start to\x01",
            "become more of a force for harm than good.\x02\x03",

            "Somewhere along the line, I started to believe \x01",
            "that only information I saw as valuable was of\x01",
            "any importance.\x02\x03",

            "And as a result, I ended up wanting power in\x01",
            "order to compensate for the weakness of my\x01",
            "own heart.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10C)
    Sleep(500)

    ChrTalk(    #45
        0x10C,
        (
            "#1855F#12PThinking back, I think what I really needed was\x01",
            "a different perspective through which to view\x01",
            "information. One separate from the military.\x02\x03",

            "One that doesn't see a country or people's way of\x01",
            "life as a system, or as numbers and absolutes.\x02\x03",

            "I needed to be collecting information that was\x01",
            "disadvantageous to Liberl, too, rather than cast\x01",
            "it all aside.\x02\x03",

            "I needed to view us and the surrounding nations\x01",
            "in a variety of lights while collecting a wide\x01",
            "variety of information from a freer perspective.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x1C)
    Sleep(500)

    ChrTalk(    #46
        0x1C,
        (
            "#5PSo you believe the company you are running\x01",
            "now is capable of doing that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10C,
        (
            "#1855F#12P...Yes, I do.\x02\x03",

            "#1856FI can't say for sure that this will allow me to\x01",
            "avoid repeating my past mistakes.\x02\x03",

            "Perhaps there was something more important\x01",
            "that I should have been doing before giving\x01",
            "thought to any of this to begin with.\x02\x03",

            "#1852FBut in the end, I came to the conclusion that\x01",
            "Liberl needs a fresh perspective, and I then\x01",
            "resolved to leave the army.\x02\x03",

            "If it needs a means to gather intel, it can make\x01",
            "another Intelligence Division. That is for Brigadier\x01",
            "General Bright to worry about--not me.\x02\x03",

            "Still, the civilian population has no such group or\x01",
            "organization. It's never had one.\x02\x03",

            "I doubt anyone in the civilian world has ever\x01",
            "thought to create one in order to gather and\x01",
            "accurately analyze information, either.\x02\x03",

            "#1855F...That was why I, as a civilian like every other,\x01",
            "chose to establish R&A Research.\x02\x03",

            "Believing that I am the right person to be the\x01",
            "first to do so.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x10C, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_280B")

    def lambda_27D6():
        OP_6D(99200, 0, 104280, 5000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_27D6)

    def lambda_27EE():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_27EE)

    def lambda_27FE():
        OP_6B(3900, 6000)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_27FE)
    Jump("loc_2928")

    label("loc_280B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2853")

    def lambda_281E():
        OP_6D(99200, 0, 104280, 4000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_281E)

    def lambda_2836():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_2836)

    def lambda_2846():
        OP_6B(3900, 4000)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_2846)
    Jump("loc_2928")

    label("loc_2853")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_289B")

    def lambda_2866():
        OP_6D(99200, 0, 104280, 3000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_2866)

    def lambda_287E():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_287E)

    def lambda_288E():
        OP_6B(3900, 3000)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_288E)
    Jump("loc_2928")

    label("loc_289B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28E3")

    def lambda_28AE():
        OP_6D(99200, 0, 104280, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_28AE)

    def lambda_28C6():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_28C6)

    def lambda_28D6():
        OP_6B(3900, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_28D6)
    Jump("loc_2928")

    label("loc_28E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2928")

    def lambda_28F6():
        OP_6D(99200, 0, 104280, 1000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_28F6)

    def lambda_290E():
        OP_6C(45000, 1000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_290E)

    def lambda_291E():
        OP_6B(3900, 1000)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_291E)

    label("loc_2928")

    WaitChrThread(0x1F, 0x0)
    OP_62(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x1C)
    Sleep(500)

    ChrTalk(    #48
        0x1C,
        (
            "#5PYou truly don't have any intention of returning\x01",
            "to the military, do you...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10C,
        (
            "#1851F#12PIf I said there wasn't a part of me that longed\x01",
            "to return to my days of active service, I would\x01",
            "be lying.\x02\x03",

            "#1850FBut I'm hoping that through this, I will be able\x01",
            "to become another eye by which to support this\x01",
            "nation.\x02\x03",

            "#1855FAnd I see my current occupation as a new way to\x01",
            "show my love for my country.\x02\x03",

            "I...wonder if that makes any sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x1C,
        "#5P#40W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x1C,
        "#5P#40WYou're...a coward...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x1C,
        (
            "#5PNo doubt every word you are saying is objectively\x01",
            "correct. That's how you've always been. There's\x01",
            "never been room for rebuttal in your arguments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x1C,
        "#5PBut, Colonel?\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #54
        0x1C,
        (
            "#5P#3SYou're also no longer the man who swore\x01",
            "to forge this kingdom's future with his own\x01",
            "two hands!#2S\x02",
        )
    )

    OP_7C(0x0, 0x190, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #55
        0x1C,
        "#5PGoodbye, Colonel! We will never meet again!\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_2CA5():
        OP_6D(100470, 0, 100750, 2000)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_2CA5)

    def lambda_2CBD():
        OP_8E(0xFE, 0x18268, 0x0, 0x1912C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_2CBD)
    WaitChrThread(0x1C, 0x1)

    def lambda_2CDD():
        OP_8E(0xFE, 0x18268, 0x3E8, 0x15F90, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_2CDD)
    WaitChrThread(0x1C, 0x1)

    def lambda_2CFD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_2CFD)
    WaitChrThread(0x1C, 0x1)
    SetChrFlags(0x1C, 0x80)
    Sleep(1000)

    def lambda_2D1E():
        OP_6D(99290, 0, 102820, 3000)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_2D1E)

    def lambda_2D36():
        OP_6C(48000, 3000)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_2D36)

    def lambda_2D46():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_2D46)
    Sleep(1000)
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x10C)
    Sleep(500)

    ChrTalk(    #56
        0x10C,
        (
            "#1856F#5PThat's not true.\x01",
            "That's not true at all, Sender...\x02\x03",

            "I...\x02\x03",

            "#1855F(I've chosen the path I now walk believing it\x01",
            "to be right, certainly...)\x02\x03",

            "(...but even I don't know for sure if what I'm\x01",
            "doing is correct.)\x02\x03",

            "(Even now, I'm terrified of the possibility that\x01",
            "I might be making the wrong choice.)\x02\x03",

            "(I worry that the road I walk might be the\x01",
            "makings of yet another grave mistake...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10C)
    Sleep(500)

    ChrTalk(    #57
        0x10C,
        (
            "#1859F#5P(I just don't have the same power that Brigadier\x01",
            "General Bright does...)\x02\x03",

            "#1858F(I really am hopeless...)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 99300, 500, 92000, 0)

    NpcTalk(    #58
        0x1D,
        "Woman's Voice",
        "#5P...Sir?\x02",
    )

    CloseMessageWindow()
    OP_62(0x10C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #59
        0x10C,
        "#1855F#5PYou didn't have to come out here in the rain.\x02",
    )

    CloseMessageWindow()

    def lambda_3029():
        OP_6D(99790, 0, 102150, 4000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_3029)

    def lambda_3041():
        OP_67(0, 3900, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_3041)

    def lambda_3059():
        OP_6B(3770, 4000)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_3059)

    def lambda_3069():
        OP_6C(58000, 4000)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_3069)
    OP_43(0x1D, 0x3, 0x0, 0x5)
    WaitChrThread(0x1D, 0x3)
    WaitChrThread(0x1C, 0x0)
    Sleep(500)

    ChrTalk(    #60
        0x1D,
        (
            "#1861F#11PWe should return to the office. You'll catch a\x01",
            "cold staying out here much longer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10C,
        "#1856F#6PKanone, I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x1D,
        (
            "#1861F#11P...I'm sure he's just having trouble coming to\x01",
            "terms with his new life, too.\x02\x03",

            "He just can't forget the fervent enthusiasm of\x01",
            "the Intelligence Division. As if he doesn't feel\x01",
            "like he belongs in the world that's come after it...\x02\x03",

            "#1862FThe day will eventually come when he will be\x01",
            "able to understand what you said.\x02\x03",

            "That's exactly what happened to me, you know.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10C)
    Sleep(500)

    ChrTalk(    #63
        0x10C,
        (
            "#1855F#6P...True enough, I suppose.\x02\x03",

            "#1851FHaha... You're right.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10C, 0x1D, 400)
    Sleep(500)

    NpcTalk(    #64
        0x10C,
        "Richard",
        "#1850F#6PShall we be going, then, Kanone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x1D,
        "#1862F#11PYes, sir.\x02",
    )

    CloseMessageWindow()

    def lambda_3343():
        OP_8C(0x10C, 180, 300)
        ExitThread()

    QueueWorkItem(0x10C, 2, lambda_3343)
    Sleep(200)
    OP_8C(0x1D, 180, 300)
    WaitChrThread(0x10C, 0x2)

    def lambda_3362():
        OP_8E(0xFE, 0x17D18, 0x3E8, 0x15F90, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_3362)
    Sleep(200)

    def lambda_3382():
        OP_8E(0xFE, 0x183E4, 0x3E8, 0x15F90, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_3382)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_24(0x1C3, 0x5A)
    OP_24(0x1C5, 0x5A)
    OP_24(0x1C9, 0x64)
    Sleep(200)
    OP_24(0x1C3, 0x50)
    OP_24(0x1C5, 0x50)
    OP_24(0x1C9, 0x5F)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    OP_24(0x1C5, 0x46)
    OP_24(0x1C9, 0x5A)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    OP_24(0x1C5, 0x3C)
    OP_24(0x1C9, 0x55)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    OP_24(0x1C5, 0x32)
    OP_24(0x1C9, 0x50)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    OP_24(0x1C5, 0x28)
    OP_24(0x1C9, 0x4B)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    OP_24(0x1C5, 0x1E)
    OP_24(0x1C9, 0x46)
    Sleep(200)
    OP_24(0x1C3, 0x14)
    OP_24(0x1C5, 0x14)
    OP_24(0x1C9, 0x41)
    Sleep(200)
    OP_23(0x1C3)
    OP_23(0x1C5)
    OP_24(0x1C9, 0x3C)
    Sleep(200)
    OP_21()
    SetMapFlags(0x100000)
    OP_A2(0x2506)
    NewScene("ED6_DT21/T2110   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_3_6C0 end

    def Function_4_3451(): pass

    label("Function_4_3451")


    def lambda_3457():
        OP_8E(0xFE, 0x17F0C, 0x0, 0x13C68, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_3457)
    WaitChrThread(0x10C, 0x1)

    def lambda_3477():
        OP_8E(0xFE, 0x17F0C, 0x3E8, 0x15F90, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_3477)
    WaitChrThread(0x10C, 0x1)
    Return()

    # Function_4_3451 end

    def Function_5_3492(): pass

    label("Function_5_3492")


    def lambda_3498():
        OP_8E(0xFE, 0x183E4, 0x0, 0x18BB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_3498)
    WaitChrThread(0x1D, 0x1)
    TurnDirection(0x1D, 0x10C, 400)
    Sleep(300)
    Return()

    # Function_5_3492 end

    def Function_6_34BF(): pass

    label("Function_6_34BF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(7000)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(6000)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(5000)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(4000)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(3000)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_34BF end

    def Function_7_3515(): pass

    label("Function_7_3515")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(133860, 8150, 97340, 0)
    OP_67(0, 6060, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    StopSound(0x9470, 0x27100, 0x0)
    OP_6D(140050, 8150, 68460, 0)
    OP_67(0, 8100, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrPos(0x10C, 126700, 6150, 101120, 90)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x11, 132100, 8150, 94700, 180)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x40)
    SetChrPos(0x19, 131260, 8150, 95000, 180)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x40)
    SetChrPos(0x1A, 129840, 8300, 99220, 180)
    SetChrChipByIndex(0x1A, 30)
    SetChrSubChip(0x1A, 0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x15, 127460, 8150, 93820, 180)
    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_43(0x15, 0x0, 0x0, 0x2)
    OP_43(0x19, 0x0, 0x0, 0x2)
    FadeToBright(2000, 0)

    def lambda_3653():
        OP_6D(134880, 8150, 96190, 5000)
        ExitThread()

    QueueWorkItem(0x10C, 3, lambda_3653)

    def lambda_366B():
        OP_8E(0xFE, 0x20ECC, 0x1FD6, 0x18B00, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_366B)
    WaitChrThread(0x10C, 0x1)

    def lambda_368B():
        OP_8E(0xFE, 0x20ECC, 0x1FD6, 0x1782C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_368B)
    WaitChrThread(0x10C, 0x1)
    WaitChrThread(0x10C, 0x3)
    Fade(1000)
    OP_6D(136270, 8150, 97450, 0)
    OP_67(0, 6060, -10000, 0)
    OP_6B(3040, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    StopSound(0x9470, 0x186A0, 0x0)
    OP_0D()
    Sleep(300)
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10C)
    Sleep(500)

    ChrTalk(    #66
        0x10C,
        "#1855F#5P(I still have doubts about what I'm doing...)\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10C, 270, 400)

    def lambda_3767():
        OP_6D(99880, 0, 102800, 5000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_3767)

    def lambda_377F():
        OP_67(0, 5060, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_377F)
    WaitChrThread(0x1F, 0x0)
    Sleep(500)
    FadeToDark(300, 0, -101)
    OP_C4(0x0, 0x800)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #67
        (
            "\x18\x07\x0CNothing about my love for my country has\x01",
            "changed. Nothing at all.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #68
        (
            "\x18\x07\x0CSo is it even possible for me to find and walk\x01",
            "the right path this time?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #69
        (
            "\x18\x07\x0CIs it truly possible for any mortal to forge the\x01",
            "correct path through life?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #70
        (
            "\x18\x07\x0CI don't know...but all I can do is try to follow\x01",
            "the path I believe to be right in hopes that I'm\x01",
            "not mistaken.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #71
        (
            "\x18\x07\x0CBelieving in those who have supported me and \x01",
            "worked to right my wrongs...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 134860, 8150, 97680, 180)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)
    SetMessageWindowPos(340, 80, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #72
        "\x07\x00...Sir?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #73
        "\x07\x00Is something wrong, sir?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(1000)
    OP_6D(136000, 8150, 98180, 0)
    OP_67(0, 5060, -10000, 0)
    OP_6B(3360, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_71(0x40A, 0x0)
    ExitThread()
    OP_0D()
    OP_62(0x10C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x10C, 0x1D, 500)
    Sleep(300)

    NpcTalk(    #74
        0x10C,
        "Richard",
        (
            "#1853FO-Oh... You're here, Kanone?\x02\x03",

            "#1851FI did tell you that you didn't need to come\x01",
            "and see me off, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x1D,
        (
            "#1860F#5PYou did, but I'm afraid that simply won't do.\x02\x03",

            "Seeing off their superiors is the duty of a\x01",
            "subordinate.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #76
        0x10C,
        "Richard",
        (
            "#1859F...Perhaps in the military, but that is no longer\x01",
            "the world we live in. There's no need to act like\x01",
            "a soldier anymore.\x02\x03",

            "#1850FOh, and one more thing.\x02\x03",

            "Please do take good care of things in the\x01",
            "office while I'm gone.\x02\x03",

            "I think the odds of any large requests you'll\x01",
            "struggle to handle without me coming in are \x01",
            "fairly low, at least, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x1D,
        (
            "#1861F#5PLeave everything to me, sir.\x02\x03",

            "I'll be sure to handle every request that comes\x01",
            "in with care and kindness.\x02\x03",

            "#1862FI'm well aware you always look forward to taking \x01",
            "on small requests, too, so they will be given \x01",
            "the same high standard of service as any other.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #78
        0x10C,
        "Richard",
        "#1851FHaha... You know me too well.\x02",
    )

    CloseMessageWindow()
    OP_59()
    Sleep(500)
    OP_22(0xE2, 0x0, 0x64)
    Sleep(1500)
    Fade(1000)
    OP_6D(131480, 14300, 81060, 0)
    OP_67(0, 6250, -10000, 0)
    OP_6B(4940, 0)
    OP_6C(55000, 0)
    OP_6E(312, 0)
    OP_11(0xA4, 0xB7, 0xFF, 0x11170, 0x249F0, 0x0)
    OP_8C(0x10C, 180, 0)
    OP_22(0x79, 0x0, 0x64)
    SetChrPos(0x17, 136000, 17500, 82500, 90)
    SetChrPos(0x18, 136000, 1000, 82500, 90)
    SetChrFlags(0x17, 0x4)
    ClearChrFlags(0x17, 0x40)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x40)
    OP_A1(0x17, 0xB)
    OP_72(0x40B, 0x0)
    ExitThread()
    OP_72(0x200B, 0x0)
    ExitThread()
    OP_72(0x20B, 0x0)
    ExitThread()
    OP_71(0xB, 0x4)
    ExitThread()
    OP_71(0x400B, 0x0)
    ExitThread()
    OP_A1(0x18, 0x9)
    OP_72(0x409, 0x0)
    ExitThread()
    SetChrFlags(0x18, 0x4)

    def lambda_3EEC():
        OP_6D(131480, 10300, 81060, 15000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_3EEC)

    def lambda_3F04():
        OP_6C(45000, 15000)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3F04)

    def lambda_3F14():
        OP_8F(0xFE, 0x21340, 0x9C4, 0x14244, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_3F14)
    WaitChrThread(0x17, 0x2)
    WaitChrThread(0x18, 0x2)

    def lambda_3F39():
        OP_8F(0xFE, 0x21340, 0x3E8, 0x14244, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_3F39)
    WaitChrThread(0x17, 0x3)
    WaitChrThread(0x18, 0x3)
    OP_22(0xE2, 0x0, 0x64)
    OP_22(0x75, 0x0, 0x64)
    Sleep(2000)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    OP_B0(0xB, 0x32)
    OP_B0(0x9, 0x32)
    OP_6F(0xB, 100)
    OP_70(0xB, 0x1)
    OP_6F(0x9, 100)
    OP_70(0x9, 0x1)
    OP_22(0x76, 0x0, 0x64)
    OP_73(0xB)
    OP_73(0x9)
    Sleep(400)
    OP_B0(0x7, 0x2D)
    OP_6F(0x7, 100)
    OP_70(0x7, 0x0)
    OP_22(0x78, 0x0, 0x64)
    OP_73(0x7)
    Sleep(1000)
    OP_6F(0xB, 410)
    OP_70(0xB, 0x1CC)
    OP_22(0x6, 0x0, 0x64)
    Sleep(800)
    OP_22(0x6, 0x0, 0x64)
    OP_73(0xB)
    Fade(1000)
    OP_6D(136000, 8150, 98180, 0)
    OP_67(0, 5060, -10000, 0)
    OP_6B(3360, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x1A, 129840, 8150, 98480, 180)
    SetChrChipByIndex(0x1A, 22)
    SetChrSubChip(0x1A, 0)
    OP_43(0x1A, 0x0, 0x0, 0x2)
    OP_0D()
    OP_4A(0x11, 255)

    def lambda_4062():
        OP_8E(0xFE, 0x20404, 0x2008, 0x141CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4062)
    Sleep(200)
    OP_4A(0x1A, 255)
    OP_43(0x1A, 0x3, 0x0, 0xE)
    Sleep(100)
    OP_4A(0x19, 255)

    def lambda_4096():
        OP_8E(0xFE, 0x20404, 0x2008, 0x16FF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4096)
    WaitChrThread(0x19, 0x1)

    def lambda_40B6():
        OP_8E(0xFE, 0x20404, 0x2008, 0x141CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_40B6)
    Sleep(300)
    OP_4A(0x15, 255)
    OP_43(0x15, 0x3, 0x0, 0xF)
    Sleep(3000)

    def lambda_40E6():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x10C, 2, lambda_40E6)
    Sleep(150)

    def lambda_40F9():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_40F9)
    WaitChrThread(0x10C, 0x2)

    def lambda_410C():
        OP_8E(0xFE, 0x20B70, 0x1FD6, 0x174BC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_410C)
    WaitChrThread(0x1D, 0x2)

    def lambda_412C():
        OP_8E(0xFE, 0x20A6C, 0x1FD6, 0x179D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_412C)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x40)
    SetChrFlags(0x1E, 0x4)
    OP_51(0x1E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x1E, 147300, 11150, 93600, 270)
    OP_22(0x197, 0x0, 0x64)
    Sleep(500)
    OP_22(0x8C, 0x0, 0x64)
    OP_43(0x1E, 0x0, 0x0, 0x2)
    WaitChrThread(0x10C, 0x1)
    OP_62(0x10C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0x1D, 0x1)
    OP_62(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_8E(0x1E, 0x20B70, 0x25B2, 0x16EE0, 0x2328, 0x0)
    OP_A3(0x1)
    OP_43(0x1E, 0x3, 0x0, 0x8)
    OP_62(0x10C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x10C, 0x3, 0x0, 0x9)
    OP_62(0x1D, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x1D, 0x3, 0x0, 0xA)
    Sleep(1000)

    NpcTalk(    #79
        0x10C,
        "Richard",
        "#1853F#6PS-Sieg?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x1D,
        "#1864F#5PWhat on earth is Julia's bird doing here?!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    WaitChrThread(0x1E, 0x3)
    SetChrChipByIndex(0x1E, 29)
    SetChrSubChip(0x1E, 0)
    OP_8C(0x1E, 90, 400)
    OP_8F(0x1E, 0x208DC, 0x2102, 0x174BC, 0x3E8, 0x0)
    Fade(500)
    OP_44(0x1E, 0x0)
    SetChrPos(0x1E, 133240, 8950, 95420, 90)
    SetChrChipByIndex(0x1E, 27)
    SetChrSubChip(0x1E, 0)
    SetChrFlags(0x1E, 0x8)
    SetChrChipByIndex(0x10C, 28)
    SetChrSubChip(0x10C, 0)
    OP_0D()
    OP_44(0x10C, 0x3)

    def lambda_42C8():
        OP_8C(0xFE, 270, 0)
        ExitThread()

    QueueWorkItem(0x10C, 2, lambda_42C8)
    OP_44(0x1D, 0x3)

    def lambda_42DA():
        OP_8C(0xFE, 180, 0)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_42DA)
    Sleep(500)

    ChrTalk(    #81
        0x1E,
        "#311F#5PScree!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #82
        0x1D,
        (
            "#1864F#5PD-Don't you just sit on His Excellency's arm\x01",
            "as if it's your own personal property!\x02\x03",

            "#1865F*glare*\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10C, 0xFFFFFE70, 2000, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #83
        0x1E,
        "#310F#5PSc-Scree...?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #84
        0x10C,
        "Richard",
        (
            "#1499F#11PPlease, Kanone. There's no need to glare at\x01",
            "him like that.\x02\x03",

            "#1850FAlso, please stop calling me Your Excellency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x1E,
        "#310F#5PScree, scree!\x02",
    )

    CloseMessageWindow()
    OP_62(0x10C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #86
        "\x07\x05Richard then noticed that there was a note attached to Sieg's leg.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    NpcTalk(    #87
        0x10C,
        "Richard",
        (
            "#1853F#11PWhat's this...?\x02\x03",

            "It's addressed to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x1E,
        "#310F#5PScree, scree!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #89
        "\x07\x05Richard took the memo from Sieg's leg.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #90
        0x10C,
        "Richard",
        (
            "#1852F#11PTh-This looks like...\x02\x03",

            "...a letter from HQ?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #91
        0x1D,
        (
            "#1864F#5PAs in, military HQ?\x02\x03",

            "Why is the Royal Guard's carrier falcon\x01",
            "bringing a message to you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10C)
    Sleep(500)

    NpcTalk(    #92
        0x10C,
        "Richard",
        (
            "#1859F#11PWho knows? Its writer is a real slave driver,\x01",
            "though.\x02\x03",

            "#1851FThank you for delivering this, Sieg.\x02\x03",

            "Let him know that I accept his request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x1E,
        "#311F#5PScree! ☆\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    SetChrChipByIndex(0x10C, 65535)
    SetChrSubChip(0x10C, 0)
    ClearChrFlags(0x1E, 0x8)
    SetChrChipByIndex(0x1E, 29)
    SetChrSubChip(0x1E, 0)
    OP_43(0x1E, 0x0, 0x0, 0x2)
    SetChrPos(0x1E, 133240, 8350, 95420, 90)
    OP_0D()
    OP_22(0x8C, 0x0, 0x64)
    OP_8F(0x1E, 0x20594, 0x25B2, 0x174BC, 0x3E8, 0x0)
    SetChrChipByIndex(0x1E, 26)
    SetChrSubChip(0x1E, 0)
    OP_97(0x1E, 0x20B70, 0x174BC, 0x6DDD0, 0x1B58, 0x1)

    def lambda_476B():
        OP_8E(0x1E, 0x23F64, 0x2B8E, 0x170D4, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_476B)

    def lambda_4786():

        label("loc_4786")

        TurnDirection(0xFE, 0x1E, 500)
        OP_48()
        Jump("loc_4786")

    QueueWorkItem2(0x10C, 2, lambda_4786)
    Sleep(100)

    def lambda_479C():

        label("loc_479C")

        TurnDirection(0xFE, 0x1E, 500)
        OP_48()
        Jump("loc_479C")

    QueueWorkItem2(0x1D, 2, lambda_479C)
    WaitChrThread(0x1E, 0x1)
    SetChrFlags(0x1E, 0x80)
    Sleep(800)
    OP_44(0x10C, 0x2)
    OP_44(0x1D, 0x2)
    TurnDirection(0x1D, 0x10C, 400)
    Sleep(300)

    ChrTalk(    #94
        0x1D,
        (
            "#1864F#5PU-Umm... Sir...\x02\x03",

            "Was that...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10C, 0x1D, 400)
    Sleep(300)

    def lambda_4808():
        OP_8F(0xFE, 0x20B0C, 0x1FD6, 0x17674, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_4808)
    WaitChrThread(0x10C, 0x1)
    Sleep(300)

    NpcTalk(    #95
        0x10C,
        "Richard",
        "#1859F#12PSee for yourself.\x02",
    )

    CloseMessageWindow()
    OP_62(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_44(0x11, 0xFF)
    SetChrFlags(0x11, 0x80)
    OP_44(0x1A, 0xFF)
    SetChrFlags(0x1A, 0x80)
    OP_44(0x15, 0xFF)
    SetChrFlags(0x15, 0x80)

    def lambda_4888():
        OP_6D(135280, 8150, 92700, 3000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_4888)

    def lambda_48A0():
        OP_6C(50000, 3000)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_48A0)

    def lambda_48B0():
        OP_67(0, 4700, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_48B0)
    OP_43(0x10C, 0x3, 0x0, 0xB)
    Sleep(2500)
    OP_63(0x1D)
    WaitChrThread(0x1F, 0x0)

    ChrTalk(    #96
        0x1D,
        (
            "#1864F#5P...'Best of luck with your little trip.\x02\x03",

            "'We'd like to know what the Red Constellation is\x01",
            "up to, too, so we'd appreciate you looking into it \x01",
            "for us on the side.'\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10C, 0x3)
    Sleep(300)
    OP_8C(0x10C, 90, 400)
    Sleep(500)

    NpcTalk(    #97
        0x10C,
        "Richard",
        (
            "#1859FHonestly...\x02\x03",

            "#1851FI hope you don't think this information is going\x01",
            "to come cheap, Brigadier General.\x02",
        )
    )

    CloseMessageWindow()
    OP_C4(0x1, 0x20000000)
    OP_59()
    OP_8C(0x10C, 180, 400)
    FadeToDark(2000, 0, -1)

    def lambda_4A34():
        OP_8E(0xFE, 0x202EC, 0x20A8, 0x1395C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_4A34)
    OP_0D()
    OP_44(0x10C, 0x1)
    SetChrPos(0x10C, 121600, 6150, 100520, 0)
    OP_6D(135100, 8200, 82340, 0)
    OP_67(0, 11210, -10000, 0)
    OP_6B(4730, 0)
    OP_6C(45000, 0)
    OP_6E(302, 0)
    SetChrPos(0x1D, 139040, 8150, 93060, 180)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0xE2, 0x0, 0x64)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x64)
    OP_73(0x7)
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0xB, 1)
    OP_70(0xB, 0x3C)
    OP_73(0xB)
    Sleep(1500)
    OP_23(0x75)
    OP_22(0x77, 0x0, 0x64)
    OP_43(0x17, 0x2, 0x0, 0xC)

    def lambda_4B02():
        OP_6D(160160, 8200, 82340, 12000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_4B02)

    def lambda_4B1A():
        OP_8F(0xFE, 0x27100, 0xDDE, 0x14050, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4B1A)

    def lambda_4B35():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4B35)
    Sleep(600)

    def lambda_4B55():
        OP_8F(0xFE, 0x27100, 0x11C6, 0x14050, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4B55)

    def lambda_4B70():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4B70)
    Sleep(700)

    def lambda_4B90():
        OP_8F(0xFE, 0x27100, 0x15AE, 0x14050, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4B90)

    def lambda_4BAB():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4BAB)
    Sleep(800)

    def lambda_4BCB():
        OP_8F(0xFE, 0x27100, 0x1996, 0x14050, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4BCB)

    def lambda_4BE6():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4BE6)
    Sleep(900)

    def lambda_4C06():
        OP_8F(0xFE, 0x27100, 0x1D7E, 0x14050, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4C06)

    def lambda_4C21():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4C21)
    Sleep(1500)

    def lambda_4C41():
        OP_8F(0xFE, 0x27100, 0x2166, 0x14050, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4C41)

    def lambda_4C5C():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4C5C)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    OP_43(0x17, 0x3, 0x0, 0xD)

    def lambda_4C92():
        OP_8F(0xFE, 0x27100, 0x254E, 0x14050, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4C92)

    def lambda_4CAD():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4CAD)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_F7(0x9, 0xC, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #98
        "\x07\x00Side Story [I Accept Your Request] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DAA")
    Sleep(1000)
    OP_28(0xE, 0x4, 0x10)
    OP_28(0xE, 0x4, 0x20)
    OP_3E(0x2EB, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #99
        "\x07\x05Received \x1F\xEB\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(10000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #100
        "\x07\x05Received \x07\x0210,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_4DAA")

    OP_A2(0x2504)
    NewScene("ED6_DT21/M3110   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_7_3515 end

    def Function_8_4DB7(): pass

    label("Function_8_4DB7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4DE2")
    OP_97(0x1E, 0x20B70, 0x174BC, 0x57E40, 0x1B58, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4DDF")
    Jump("loc_4DE2")

    label("loc_4DDF")

    Jump("Function_8_4DB7")

    label("loc_4DE2")

    OP_97(0x1E, 0x20B70, 0x174BC, 0x15F90, 0x1770, 0x1)
    Return()

    # Function_8_4DB7 end

    def Function_9_4DF8(): pass

    label("Function_9_4DF8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E28")
    TurnDirection(0xFE, 0x1E, 900)
    Sleep(700)
    TurnDirection(0xFE, 0x1E, 800)
    Sleep(1000)
    TurnDirection(0xFE, 0x1E, 1000)
    Sleep(1100)
    Jump("Function_9_4DF8")

    label("loc_4E28")

    Return()

    # Function_9_4DF8 end

    def Function_10_4E29(): pass

    label("Function_10_4E29")

    Sleep(200)

    label("loc_4E2E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E5E")
    TurnDirection(0xFE, 0x1E, 800)
    Sleep(1000)
    TurnDirection(0xFE, 0x1E, 1000)
    Sleep(700)
    TurnDirection(0xFE, 0x1E, 900)
    Sleep(1100)
    Jump("loc_4E2E")

    label("loc_4E5E")

    Return()

    # Function_10_4E29 end

    def Function_11_4E5F(): pass

    label("Function_11_4E5F")

    OP_8C(0x10C, 255, 400)

    def lambda_4E6C():
        OP_8E(0xFE, 0x202EC, 0x20A8, 0x16DDC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_4E6C)
    WaitChrThread(0x10C, 0x1)

    def lambda_4E8C():
        OP_8E(0xFE, 0x202EC, 0x20A8, 0x15F90, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_4E8C)
    WaitChrThread(0x10C, 0x1)
    Sleep(300)
    Return()

    # Function_11_4E5F end

    def Function_12_4EAC(): pass

    label("Function_12_4EAC")

    OP_B0(0xB, 0x32)
    OP_6F(0xB, 61)
    OP_70(0xB, 0xA0)
    OP_73(0xB)
    OP_71(0x200B, 0x0)
    ExitThread()
    OP_6F(0xB, 161)
    OP_70(0xB, 0x104)
    Return()

    # Function_12_4EAC end

    def Function_13_4ED6(): pass

    label("Function_13_4ED6")

    OP_24(0x77, 0x5A)
    OP_24(0x1C5, 0x5A)
    Sleep(300)
    OP_24(0x77, 0x50)
    OP_24(0x1C5, 0x50)
    Sleep(300)
    OP_24(0x77, 0x46)
    OP_24(0x1C5, 0x46)
    Sleep(300)
    OP_24(0x77, 0x3C)
    OP_24(0x1C5, 0x3C)
    Sleep(300)
    OP_24(0x77, 0x32)
    OP_24(0x1C5, 0x32)
    Sleep(300)
    OP_24(0x77, 0x28)
    OP_24(0x1C5, 0x28)
    Sleep(300)
    OP_24(0x77, 0x1E)
    OP_24(0x1C5, 0x1E)
    Sleep(300)
    OP_23(0x77)
    OP_23(0x1C5)
    Return()

    # Function_13_4ED6 end

    def Function_14_4F38(): pass

    label("Function_14_4F38")


    def lambda_4F3E():
        OP_8E(0xFE, 0x20404, 0x1FD6, 0x17700, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4F3E)
    WaitChrThread(0x1A, 0x1)

    def lambda_4F5E():
        OP_8E(0xFE, 0x20404, 0x1FD6, 0x141CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4F5E)
    WaitChrThread(0x1A, 0x1)
    Return()

    # Function_14_4F38 end

    def Function_15_4F79(): pass

    label("Function_15_4F79")


    def lambda_4F7F():
        OP_8E(0xFE, 0x1F568, 0x2008, 0x171EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4F7F)
    WaitChrThread(0x15, 0x1)

    def lambda_4F9F():
        OP_8E(0xFE, 0x20404, 0x2008, 0x171EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4F9F)
    WaitChrThread(0x15, 0x1)

    def lambda_4FBF():
        OP_8E(0xFE, 0x20404, 0x2008, 0x141CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4FBF)
    WaitChrThread(0x15, 0x1)
    Return()

    # Function_15_4F79 end

    def Function_16_4FDA(): pass

    label("Function_16_4FDA")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #101
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_4FDA end

    def Function_17_5029(): pass

    label("Function_17_5029")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #102
        (
            "\x07\x05Airship Arrivals & Departures\x01\x09\x09",
            "⇒ To Bose\x01\x09\x09",
            "⇒ To Zeiss\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_5029 end

    def Function_18_5094(): pass

    label("Function_18_5094")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #103
        (
            "\x07\x05※Dangerous/combustible objects prohibited.\x01",
            "　　　　《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_5094 end

    def Function_19_5113(): pass

    label("Function_19_5113")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #104
        (
            "\x07\x05Traffic Control Tower\x01",
            "※All unauthorized personnel are prohibited.\x01",
            "《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_5113 end

    SaveToFile()

Try(main)
