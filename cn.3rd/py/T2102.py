from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '城中老年男子',                         # 9
        '城中中年妇女',                         # 10
        '城中小男孩',                           # 11
        '森特',                                 # 12
        '贵族中年男子',                         # 13
        '贵族女孩',                             # 14
        '哈尔德',                               # 15
        '林德号',                               # 16
        '林德号影子',                           # 17
        '小孩',                                 # 18
        '贵族女子',                             # 19
        '贵族男子',                             # 20
        '森达',                                 # 21
        '秘书凯诺娜',                           # 22
        '基库',                                 # 23
        '目标用照相机',                         # 24
        '卢安市·北街区',                       # 25
        '',                                     # 26
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
        "Function_4_27F5",         # 04, 4
        "Function_5_2836",         # 05, 5
        "Function_6_2863",         # 06, 6
        "Function_7_28B9",         # 07, 7
        "Function_8_3F15",         # 08, 8
        "Function_9_3F56",         # 09, 9
        "Function_10_3F87",        # 0A, 10
        "Function_11_3FBD",        # 0B, 11
        "Function_12_400A",        # 0C, 12
        "Function_13_4034",        # 0D, 13
        "Function_14_4096",        # 0E, 14
        "Function_15_40D7",        # 0F, 15
        "Function_16_4138",        # 10, 16
        "Function_17_4180",        # 11, 17
        "Function_18_41DF",        # 12, 18
        "Function_19_4245",        # 13, 19
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
        "男人的声音",
        "……正等着您呢。\x02",
    )

    CloseMessageWindow()

    def lambda_877():
        OP_6D(99400, 0, 103440, 2500)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_877)

    def lambda_88F():
        OP_67(0, 4240, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_88F)

    def lambda_8A7():
        OP_6C(50000, 2500)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_8A7)
    WaitChrThread(0x1F, 0x0)
    OP_82(0x2, 0x2)
    SetChrPos(0x10C, 97560, 1000, 93000, 0)

    def lambda_8D0():
        OP_8E(0xFE, 0x17D18, 0x0, 0x1881C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_8D0)
    WaitChrThread(0x10C, 0x1)
    Sleep(300)

    ChrTalk(    #1
        0x10C,
        "#1855F…………是你吗，森达。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x1C,
        (
            "#5P好久不见了，上校。\x02\x03",

            "您看起来气色不错，太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10C,
        (
            "#1851F我已经不是上校了。\x02\x03",

            "#1859F虽然大家总是忽视这一点……\x01",
            "就算我怎么努力说明也不行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x1C,
        (
            "#5P……不，\x01",
            "今天请务必让我称您为上校。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10C,
        "#1853F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x1C,
        (
            "#5P…………上校，\x01",
            "我有些事想请教您。\x02\x03",

            "虽属越级，\x01",
            "还是这样把您约出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10C,
        (
            "#1855F……只要力所能及\x01",
            "我会尽力解答的。\x02\x03",

            "#1851F不必客气……\x02\x03",

            "有什么想不通的事\x01",
            "就尽管说吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x1C)
    Sleep(500)

    ChrTalk(    #8
        0x1C,
        (
            "#5P…………上校，\x01",
            "那我就问了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x1C,
        "#5P为什么要离开军队呢。\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #10
        0x1C,
        (
            "#5P#3S您的爱国心\x01",
            "到底去了哪里！#2S\x02",
        )
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
            "#1859F………你……………\x01",
            "好像恢复军职了啊。\x02\x03",

            "#1850F…………那我就放心了。\x02\x03",

            "#1856F你在士官学校也是特别优秀的人才。\x01",
            "如果没有碰到我……\x02\x03",

            "#1855F要是我没把你卷进去，\x01",
            "现在就算位居校级\x01",
            "也不奇怪……\x02\x03",

            "……真是对不起了………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #12
        0x1C,
        (
            "#5P……上校，\x01",
            "我绝对没有责备您的意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x1C,
        (
            "#5P……您比任何人\x01",
            "都为这个国家着想。\x01",
            "那份爱国心是真心实意的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x1C,
        (
            "#5P发誓要追随您，\x01",
            "令我感到十分幸福。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x1C,
        (
            "#5P的确，事到如今\x01",
            "我也很难再往上晋升……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x1C,
        "#5P……但这种事根本无所谓。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x1C,
        (
            "#5P我要回归军队，\x01",
            "再度为国出力。\x01",
            "这样我就感到很幸福了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x1C,
        (
            "#5P……我从一开始，\x01",
            "就毫无怨恨您的念头。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #19
        0x1C,
        "#5P…………但是……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x1C,
        (
            "#5P上校，\x01",
            "您又如何了呢。\x02",
        )
    )

    Jump("loc_EF6")

    label("loc_EF6")

    CloseMessageWindow()

    ChrTalk(    #21
        0x1C,
        (
            "#5P……曾经那样\x01",
            "为国家的将来而担忧的您……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x1C,
        (
            "#5P却无心再度\x01",
            "为国出力，\x01",
            "早早地就离开了军队……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x1C,
        (
            "#5P而现在居然还开起了公司，\x01",
            "和有钱人做生意……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #24
        0x1C,
        (
            "#5P#4S您……您的爱国心\x01",
            "到底上哪儿去了！！#2S\x02",
        )
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
        "#5P……上校，回归军队吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x1C,
        (
            "#5P您应该恢复军职，\x01",
            "发挥您的实力！\x02",
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
            "#1855F………………抱歉。\x02\x03",

            "我不打算再回军队了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #28
        0x1C,
        "#5P#40W………………为什么……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #29
        0x1C,
        "#5P#3S…………这是为什么！？#2S\x02",
    )

    OP_7C(0x0, 0x12C, 0xFA0, 0x64)
    CloseMessageWindow()
    OP_22(0x169, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #30
        0x1C,
        (
            "#5P您已经\x01",
            "充分偿还了罪过。\x02",
        )
    )

    Jump("loc_11E0")

    label("loc_11E0")

    CloseMessageWindow()

    ChrTalk(    #31
        0x1C,
        (
            "#5P摩尔根将军和卡西乌斯准将，\x01",
            "都在期待您的回归。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x1C,
        (
            "#5P我们所有人，\x01",
            "都衷心企盼着您！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x1C,
        (
            "#5P……然而，\x01",
            "您却为何摆出这种姿态………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x1C,
        "#5P……以这副样子……向我道歉呢……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10C,
        (
            "#1856F……森达，\x01",
            "我绝非舍弃了自己的爱国心。\x02\x03",

            "……不如说………………\x02",
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
            "#1855F……我犯下了重大的罪责。\x02\x03",

            "引发了那样的事件，\x01",
            "波及了众多人民……\x02\x03",

            "虽然在许多人的帮助下\x01",
            "我察觉到了自己的过错……\x02\x03",

            "#1858F……………但我的心，\x01",
            "却毫无任何变化。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x1C,
        "#5P上……上校……………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10C,
        (
            "#1856F经过那样重大的事件，\x01",
            "我的忧国之心\x01",
            "绝无任何动摇。\x02\x03",

            "即使是现在，\x01",
            "依然怀有想为利贝尔\x01",
            "献身的冲动……\x02\x03",

            "#1855F………我………………\x01",
            "和计划政变时相比\x01",
            "完全没有任何改变。\x02\x03",

            "……我正是对此感到恐惧。\x02",
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
            "#5P#30W……怎………………\x01",
            "…………怎么会…………\x02\x03",

            "#20W#5P……那么………\x01",
            "您并不是丧失了爱国心………\x02\x03",

            "#5P反倒是因为依然保持着爱国心\x01",
            "才无法留在军队的……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10C,
        (
            "#1855F………………抱歉……\x01",
            "我不该跟你说的。\x02\x03",

            "#1856F将你们卷进来的\x01",
            "不是别人，就是我……\x02\x03",

            "……………我真的\x01",
            "觉得非常抱歉……\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x1, 0x2)

    def lambda_165F():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_165F)
    Sleep(1000)

    ChrTalk(    #41
        0x1C,
        (
            "#5P……………………\x02\x03",

            "#5P……您、您…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x1C,
        (
            "#5P这不可能……\x01",
            "……您应该更加…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10C,
        (
            "#1852F……不过，你不要误会。\x02\x03",

            "森达，我绝对不是\x01",
            "在逃避自己的软弱。\x02\x03",

            "绝不是以降级和处分为耻\x01",
            "才离开军队的。\x02\x03",

            "#1855F我在那之后考虑了很久。\x01",
            "我到底应该怎么做才行……\x02\x03",

            "到底在哪里走错了路……\x02\x03",

            "#1852F然后，我突然察觉到了。\x01",
            "我所忽略的重大事实。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x10C, 0x0, 0x0, 0x6)

    def lambda_180D():
        OP_6D(99200, 0, 104280, 28000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_180D)

    def lambda_1825():
        OP_6C(45000, 28000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_1825)

    def lambda_1835():
        OP_6B(3900, 28000)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_1835)

    def lambda_1845():
        OP_8E(0xFE, 0x17D18, 0x0, 0x18C40, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_1845)
    WaitChrThread(0x10C, 0x1)
    OP_8C(0x10C, 270, 400)
    Sleep(300)

    ChrTalk(    #44
        0x10C,
        (
            "#1856F#12P……我设置情报部，\x01",
            "为了保卫国家而收集情报。\x02\x03",

            "然而，我自己\x01",
            "对于情报到底从何而来，\x01",
            "却几乎完全不知道。\x02\x03",

            "#1855F情报并不是独立存在的。\x01",
            "正是因为人们在利用，\x01",
            "它才会作为情报而存在。\x02\x03",

            "而根据不同的立场和视角，\x01",
            "其价值也会孑然迥异……\x02\x03",

            "#1856F我的爱国心开始扭曲，\x01",
            "或许就是因为我\x01",
            "愚蠢得没有察觉这一点。\x02\x03",

            "误以为自己所见的价值是绝对的，\x01",
            "不知不觉，我开始只收集\x01",
            "对自己有利的情报。\x02\x03",

            "而其结果，\x01",
            "就是为了支持我脆弱的心灵\x01",
            "而开始寻求强大的力量……\x02",
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
            "#1855F#12P……对当时的我来说，\x01",
            "如果能从与军方相异的视角出发\x01",
            "看待事物就好了。\x02\x03",

            "……不是像军队一样\x01",
            "将国家和人民系统化的视角。\x02\x03",

            "不是采取对国家无利的事\x01",
            "就要完全舍去的做法。\x02\x03",

            "要从高处俯瞰利贝尔和其它各国，\x01",
            "从自由的视角出发\x01",
            "找出更多样化的情报价值……\x02",
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
            "#5P……而能够实现这点的\x01",
            "就是现在的公司……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10C,
        (
            "#1855F#12P………………就是这样。\x02\x03",

            "#1856F我也不知道这是否\x01",
            "为避免重蹈覆辙的正确方法。\x02\x03",

            "在反复思考之前，\x01",
            "或许还有应该做的事情。\x02\x03",

            "#1852F然而，\x01",
            "当想到这个国家需要新视角之时，\x01",
            "我就决定要辞去军职。\x02\x03",

            "军队构建军队的情报机关即可。\x01",
            "既然有准将在，\x01",
            "就轮不到我来担心了吧。\x02\x03",

            "然而民间没有这样的机构。\x02\x03",

            "本身就缺乏进行有组织的情报收集\x01",
            "和正确分析这种想法。\x02\x03",

            "#1855F……所以我以一介民众的身份\x01",
            "兴办了『Ｒ＆Ａ Research』。\x02\x03",

            "我相信这是现在\x01",
            "自己应该做的事……\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x10C, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E21")

    def lambda_1DEC():
        OP_6D(99200, 0, 104280, 5000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_1DEC)

    def lambda_1E04():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_1E04)

    def lambda_1E14():
        OP_6B(3900, 6000)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_1E14)
    Jump("loc_1F3E")

    label("loc_1E21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E69")

    def lambda_1E34():
        OP_6D(99200, 0, 104280, 4000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_1E34)

    def lambda_1E4C():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_1E4C)

    def lambda_1E5C():
        OP_6B(3900, 4000)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_1E5C)
    Jump("loc_1F3E")

    label("loc_1E69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EB1")

    def lambda_1E7C():
        OP_6D(99200, 0, 104280, 3000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_1E7C)

    def lambda_1E94():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_1E94)

    def lambda_1EA4():
        OP_6B(3900, 3000)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_1EA4)
    Jump("loc_1F3E")

    label("loc_1EB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EF9")

    def lambda_1EC4():
        OP_6D(99200, 0, 104280, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_1EC4)

    def lambda_1EDC():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_1EDC)

    def lambda_1EEC():
        OP_6B(3900, 2000)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_1EEC)
    Jump("loc_1F3E")

    label("loc_1EF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F3E")

    def lambda_1F0C():
        OP_6D(99200, 0, 104280, 1000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_1F0C)

    def lambda_1F24():
        OP_6C(45000, 1000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_1F24)

    def lambda_1F34():
        OP_6B(3900, 1000)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_1F34)

    label("loc_1F3E")

    WaitChrThread(0x1F, 0x0)
    OP_62(0x1C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x1C)
    Sleep(500)

    ChrTalk(    #48
        0x1C,
        (
            "#5P您已经…………\x01",
            "不会再回军队了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10C,
        (
            "#1851F#12P……如果说对军队毫无眷恋\x01",
            "那也是谎言…………\x02\x03",

            "#1850F然而，\x01",
            "我想成为支持这个国家的\x01",
            "另一双眼睛。\x02\x03",

            "#1855F……森达，\x01",
            "这就是现在我新的爱国方式。\x02\x03",

            "希望你能理解……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x1C,
        "#5P#40W…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x1C,
        "#5P#40W您实在……太懦弱了…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x1C,
        (
            "#5P您的想法应该是正确的吧。\x01",
            "您总是那样正直，让人毫无反驳的余地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x1C,
        "#5P然而…………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #54
        0x1C,
        (
            "#5P#3S您已经不再是那个\x01",
            "说要开拓利贝尔未来的您了……！#2S\x02",
        )
    )

    OP_7C(0x0, 0x190, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #55
        0x1C,
        (
            "#5P已经后会无期了吧！\x01",
            "恕我失礼……！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    def lambda_21AD():
        OP_6D(100470, 0, 100750, 2000)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_21AD)

    def lambda_21C5():
        OP_8E(0xFE, 0x18268, 0x0, 0x1912C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_21C5)
    WaitChrThread(0x1C, 0x1)

    def lambda_21E5():
        OP_8E(0xFE, 0x18268, 0x3E8, 0x15F90, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_21E5)
    WaitChrThread(0x1C, 0x1)
    SetChrFlags(0x1C, 0x80)
    Sleep(1000)

    def lambda_220F():
        OP_6D(99290, 0, 102820, 3000)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_220F)

    def lambda_2227():
        OP_6C(48000, 3000)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_2227)

    def lambda_2237():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_2237)
    Sleep(1000)
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0x10C)
    Sleep(500)

    ChrTalk(    #56
        0x10C,
        (
            "#1856F#5P……不是的………………#2380W \x01",
            "#20W不是这样的，森达……\x02\x03",

            "我………………………………\x02\x03",

            "#1855F（虽然下定决心，\x01",
            "  打算走上新的道路……）\x02\x03",

            "（但这选择是否正确，\x01",
            "  我却并无确信。）\x02\x03",

            "（……现在也一直在迷惘。）\x02\x03",

            "（至今还为\x01",
            "  这条道路是否错误\x01",
            "  而感到不安……）\x02",
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
            "#1859F#5P（我没有像准将那样\x01",
            "  果断的魄力………）\x02\x03",

            "#1858F（我果然还是不行……）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 99300, 500, 92000, 0)

    NpcTalk(    #58
        0x1D,
        "女性的声音",
        "#5P…………所长……\x02",
    )

    CloseMessageWindow()
    OP_62(0x10C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #59
        0x10C,
        "#1855F#5P…………凯诺娜吗……\x02",
    )

    CloseMessageWindow()

    def lambda_24AB():
        OP_6D(99790, 0, 102150, 4000)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_24AB)

    def lambda_24C3():
        OP_67(0, 3900, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_24C3)

    def lambda_24DB():
        OP_6B(3770, 4000)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_24DB)

    def lambda_24EB():
        OP_6C(58000, 4000)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_24EB)
    OP_43(0x1D, 0x3, 0x0, 0x5)
    WaitChrThread(0x1D, 0x3)
    WaitChrThread(0x1C, 0x0)
    Sleep(500)

    ChrTalk(    #60
        0x1D,
        (
            "#1861F#11P……回去吧。\x01",
            "会感冒的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10C,
        "#1856F#6P凯诺娜，我……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x1D,
        (
            "#1861F#11P……他一定\x01",
            "也只是在迷惘而已。\x02\x03",

            "无法忘怀情报部的热情，\x01",
            "还在寻求\x01",
            "心灵的归宿吧。\x02\x03",

            "#1862F……总有一天，\x01",
            "他一定能够明白的。\x02\x03",

            "因为我也是一样……\x02",
        )
    )

    Jump("loc_261E")

    label("loc_261E")

    CloseMessageWindow()
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10C)
    Sleep(500)

    ChrTalk(    #63
        0x10C,
        (
            "#1855F#6P……是吗…………\x02\x03",

            "#1851F呵呵，是啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10C, 0x1D, 400)
    Sleep(500)

    NpcTalk(    #64
        0x10C,
        "理查德所长",
        "#1850F#6P回去吧，凯诺娜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x1D,
        "#1862F#11P…………是。\x02",
    )

    CloseMessageWindow()

    def lambda_26E7():
        OP_8C(0x10C, 180, 300)
        ExitThread()

    QueueWorkItem(0x10C, 2, lambda_26E7)
    Sleep(200)
    OP_8C(0x1D, 180, 300)
    WaitChrThread(0x10C, 0x2)

    def lambda_2706():
        OP_8E(0xFE, 0x17D18, 0x3E8, 0x15F90, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_2706)
    Sleep(200)

    def lambda_2726():
        OP_8E(0xFE, 0x183E4, 0x3E8, 0x15F90, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_2726)
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

    def Function_4_27F5(): pass

    label("Function_4_27F5")


    def lambda_27FB():
        OP_8E(0xFE, 0x17F0C, 0x0, 0x13C68, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_27FB)
    WaitChrThread(0x10C, 0x1)

    def lambda_281B():
        OP_8E(0xFE, 0x17F0C, 0x3E8, 0x15F90, 0x157C, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_281B)
    WaitChrThread(0x10C, 0x1)
    Return()

    # Function_4_27F5 end

    def Function_5_2836(): pass

    label("Function_5_2836")


    def lambda_283C():
        OP_8E(0xFE, 0x183E4, 0x0, 0x18BB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_283C)
    WaitChrThread(0x1D, 0x1)
    TurnDirection(0x1D, 0x10C, 400)
    Sleep(300)
    Return()

    # Function_5_2836 end

    def Function_6_2863(): pass

    label("Function_6_2863")

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

    # Function_6_2863 end

    def Function_7_28B9(): pass

    label("Function_7_28B9")

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

    def lambda_29F7():
        OP_6D(134880, 8150, 96190, 5000)
        ExitThread()

    QueueWorkItem(0x10C, 3, lambda_29F7)

    def lambda_2A0F():
        OP_8E(0xFE, 0x20ECC, 0x1FD6, 0x18B00, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_2A0F)
    WaitChrThread(0x10C, 0x1)

    def lambda_2A2F():
        OP_8E(0xFE, 0x20ECC, 0x1FD6, 0x1782C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_2A2F)
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
        "#1855F#5P（……果然，我还心存迷惘。）\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10C, 270, 400)

    def lambda_2B01():
        OP_6D(99880, 0, 102800, 5000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_2B01)

    def lambda_2B19():
        OP_67(0, 5060, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_2B19)
    WaitChrThread(0x1F, 0x0)
    Sleep(500)
    FadeToDark(300, 0, -101)
    OP_C4(0x0, 0x800)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #67
        (
            "\x18\x07\x0C我的爱国心，\x01",
            "最终还是无法改变任何东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #68
        (
            "\x18\x07\x0C保持原样的自己，\x01",
            "是否真能走上正确的道路呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #69
        (
            "\x18\x07\x0C说到底，\x01",
            "人以一己之力是否能开拓正确的道路呢。\x02",
        )
    )

    Jump("loc_2C11")

    label("loc_2C11")

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #70
        (
            "\x18\x07\x0C……虽然找不到答案…………\x01",
            "现在，就在自己所相信的道路上走下去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #71
        (
            "\x18\x07\x0C相信着那些纠正我的错误，\x01",
            "并支持我的人们……\x02",
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
    SetChrName("女性的声音")

    AnonymousTalk(    #72
        "\x07\x00所长…………？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("女性的声音")

    AnonymousTalk(    #73
        "\x07\x00您怎么了？\x02",
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
        "理查德所长",
        (
            "#1853F啊、啊啊…………\x01",
            "……凯诺娜吗。\x02\x03",

            "#1851F我都说\x01",
            "不用来送行了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x1D,
        (
            "#1860F#5P那怎么能行。\x02\x03",

            "为上司送行\x01",
            "是部下的职责。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #76
        0x10C,
        "理查德所长",
        (
            "#1859F……凯诺娜，\x01",
            "现在已经不是在军队了，\x01",
            "不要这么刻板嘛。\x02\x03",

            "#1850F啊啊，\x01",
            "还有句话忘了说。\x02\x03",

            "……我不在的时候，\x01",
            "事务所那边就拜托你了。\x02\x03",

            "虽然我想\x01",
            "不会这么早就\x01",
            "来什么很重要的委托……\x02",
        )
    )

    Jump("loc_2F31")

    label("loc_2F31")

    CloseMessageWindow()

    ChrTalk(    #77
        0x1D,
        (
            "#1861F#5P……请交给我吧。\x02\x03",

            "任何委托\x01",
            "我都会恳切谨慎对待的。\x02\x03",

            "#1862F我至少会明白，\x01",
            "所长您即使对于很小的委托\x01",
            "也会十分期待的心情。\x02",
        )
    )

    Jump("loc_2FD6")

    label("loc_2FD6")

    CloseMessageWindow()

    NpcTalk(    #78
        0x10C,
        "理查德所长",
        "#1851F哈哈……拜托你了。\x02",
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

    def lambda_30E4():
        OP_6D(131480, 10300, 81060, 15000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_30E4)

    def lambda_30FC():
        OP_6C(45000, 15000)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_30FC)

    def lambda_310C():
        OP_8F(0xFE, 0x21340, 0x9C4, 0x14244, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_310C)
    WaitChrThread(0x17, 0x2)
    WaitChrThread(0x18, 0x2)

    def lambda_3131():
        OP_8F(0xFE, 0x21340, 0x3E8, 0x14244, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_3131)
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

    def lambda_325A():
        OP_8E(0xFE, 0x20404, 0x2008, 0x141CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_325A)
    Sleep(200)
    OP_4A(0x1A, 255)
    OP_43(0x1A, 0x3, 0x0, 0xE)
    Sleep(100)
    OP_4A(0x19, 255)

    def lambda_328E():
        OP_8E(0xFE, 0x20404, 0x2008, 0x16FF8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_328E)
    WaitChrThread(0x19, 0x1)

    def lambda_32AE():
        OP_8E(0xFE, 0x20404, 0x2008, 0x141CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_32AE)
    Sleep(300)
    OP_4A(0x15, 255)
    OP_43(0x15, 0x3, 0x0, 0xF)
    Sleep(3000)

    def lambda_32DE():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x10C, 2, lambda_32DE)
    Sleep(150)

    def lambda_32F1():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_32F1)
    WaitChrThread(0x10C, 0x2)

    def lambda_3304():
        OP_8E(0xFE, 0x20B70, 0x1FD6, 0x174BC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_3304)
    WaitChrThread(0x1D, 0x2)

    def lambda_3324():
        OP_8E(0xFE, 0x20A6C, 0x1FD6, 0x179D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_3324)
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
        "理查德所长",
        (
            "#1853F#6P你是………\x01",
            "………基库吗………？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x1D,
        "#1864F#5P尤、尤莉亚的隼……！？\x02",
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

    def lambda_34D4():
        OP_8C(0xFE, 270, 0)
        ExitThread()

    QueueWorkItem(0x10C, 2, lambda_34D4)
    OP_44(0x1D, 0x3)

    def lambda_34E6():
        OP_8C(0xFE, 180, 0)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_34E6)
    Sleep(500)

    ChrTalk(    #81
        0x1E,
        "#311F#5P啾！\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #82
        0x1D,
        (
            "#1864F#5P居、居然大摇大摆的就\x01",
            "停在阁下的手臂上……\x02\x03",

            "#1865F哼………………！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10C, 0xFFFFFE70, 2000, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #83
        0x1E,
        "#310F#5P啾、啾～……！？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #84
        0x10C,
        "理查德所长",
        (
            "#1499F#11P……凯诺娜。\x01",
            "不准开枪哦。\x02\x03",

            "#1850F还有别再叫我阁下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x1E,
        "#310F#5P啾、啾！\x02",
    )

    CloseMessageWindow()
    OP_62(0x10C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #86
        "\x07\x05基库的脚上系着纸条。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    NpcTalk(    #87
        0x10C,
        "理查德所长",
        (
            "#1853F#11P？？？\x02\x03",

            "这是给我的……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x1E,
        "#310F#5P啾啾～！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #89
        "\x07\x05理查德取下基库脚上的纸条。\x02",
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
        "理查德所长",
        (
            "#1852F#11P这、这是…………\x02\x03",

            "似乎是军队\x01",
            "司令部的书简……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10C, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #91
        0x1D,
        (
            "#1864F#5P军队司令部的……？\x02\x03",

            "为什么亲卫队的传令员\x01",
            "会送来这个……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10C)
    Sleep(500)

    NpcTalk(    #92
        0x10C,
        "理查德所长",
        (
            "#1859F#11P谁知道呢……\x01",
            "因为那个人总是喜欢乱使唤人嘛。\x02\x03",

            "#1851F……谢谢你，基库。\x02\x03",

            "我接受这个委托，\x01",
            "请帮忙转达。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x1E,
        "#311F#5P啾～☆\x02",
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

    def lambda_3910():
        OP_8E(0x1E, 0x23F64, 0x2B8E, 0x170D4, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_3910)

    def lambda_392B():

        label("loc_392B")

        TurnDirection(0xFE, 0x1E, 500)
        OP_48()
        Jump("loc_392B")

    QueueWorkItem2(0x10C, 2, lambda_392B)
    Sleep(100)

    def lambda_3941():

        label("loc_3941")

        TurnDirection(0xFE, 0x1E, 500)
        OP_48()
        Jump("loc_3941")

    QueueWorkItem2(0x1D, 2, lambda_3941)
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
            "#1864F#5P那、那个……所长……？\x02\x03",

            "那封书简不会是……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10C, 0x1D, 400)
    Sleep(300)

    def lambda_39C8():
        OP_8F(0xFE, 0x20B0C, 0x1FD6, 0x17674, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_39C8)
    WaitChrThread(0x10C, 0x1)
    Sleep(300)

    NpcTalk(    #95
        0x10C,
        "理查德所长",
        "#1859F#12P嗯，就是这么回事。\x02",
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

    def lambda_3A53():
        OP_6D(135280, 8150, 92700, 3000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_3A53)

    def lambda_3A6B():
        OP_6C(50000, 3000)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3A6B)

    def lambda_3A7B():
        OP_67(0, 4700, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_3A7B)
    OP_43(0x10C, 0x3, 0x0, 0xB)
    Sleep(2500)
    OP_63(0x1D)
    WaitChrThread(0x1F, 0x0)

    ChrTalk(    #96
        0x1D,
        (
            "#1864F#5P………出差辛苦了。\x02\x03",

            "我王国军也很关心\x01",
            "『赤色星座』的动向，\x01",
            "希望能顺便调查………\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10C, 0x3)
    Sleep(300)
    OP_8C(0x10C, 90, 400)
    Sleep(500)

    NpcTalk(    #97
        0x10C,
        "理查德所长",
        (
            "#1859F哎呀哎呀……\x02\x03",

            "#1851F这个的情报费\x01",
            "可是很贵的哦，准将。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_8C(0x10C, 180, 400)
    FadeToDark(2000, 0, -1)

    def lambda_3B94():
        OP_8E(0xFE, 0x202EC, 0x20A8, 0x1395C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_3B94)
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

    def lambda_3C62():
        OP_6D(160160, 8200, 82340, 12000)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_3C62)

    def lambda_3C7A():
        OP_8F(0xFE, 0x27100, 0xDDE, 0x14050, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3C7A)

    def lambda_3C95():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3C95)
    Sleep(600)

    def lambda_3CB5():
        OP_8F(0xFE, 0x27100, 0x11C6, 0x14050, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3CB5)

    def lambda_3CD0():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3CD0)
    Sleep(700)

    def lambda_3CF0():
        OP_8F(0xFE, 0x27100, 0x15AE, 0x14050, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3CF0)

    def lambda_3D0B():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3D0B)
    Sleep(800)

    def lambda_3D2B():
        OP_8F(0xFE, 0x27100, 0x1996, 0x14050, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3D2B)

    def lambda_3D46():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3D46)
    Sleep(900)

    def lambda_3D66():
        OP_8F(0xFE, 0x27100, 0x1D7E, 0x14050, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3D66)

    def lambda_3D81():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3D81)
    Sleep(1500)

    def lambda_3DA1():
        OP_8F(0xFE, 0x27100, 0x2166, 0x14050, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3DA1)

    def lambda_3DBC():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3DBC)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    OP_43(0x17, 0x3, 0x0, 0xD)

    def lambda_3DF2():
        OP_8F(0xFE, 0x27100, 0x254E, 0x14050, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3DF2)

    def lambda_3E0D():
        OP_8F(0xFE, 0x27100, 0x4B0, 0x14050, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3E0D)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #98
        "\x07\x00Episode『谨此接受调查委托』　～Fin～\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F08")
    Sleep(1000)
    OP_28(0xE, 0x4, 0x10)
    OP_28(0xE, 0x4, 0x20)
    OP_3E(0x2EB, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #99
        "\x07\x00得到了\x1F\xEB\x02\x07\x00。\x02",
    )

    Jump("loc_3ECF")

    label("loc_3ECF")

    CloseMessageWindow()
    AddMira(10000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #100
        "\x07\x00得到了\x07\x02１００００米拉\x07\x00。\x02",
    )

    Jump("loc_3EFC")

    label("loc_3EFC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_3F08")

    OP_A2(0x2504)
    NewScene("ED6_DT21/M3110   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_7_28B9 end

    def Function_8_3F15(): pass

    label("Function_8_3F15")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F40")
    OP_97(0x1E, 0x20B70, 0x174BC, 0x57E40, 0x1B58, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3F3D")
    Jump("loc_3F40")

    label("loc_3F3D")

    Jump("Function_8_3F15")

    label("loc_3F40")

    OP_97(0x1E, 0x20B70, 0x174BC, 0x15F90, 0x1770, 0x1)
    Return()

    # Function_8_3F15 end

    def Function_9_3F56(): pass

    label("Function_9_3F56")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F86")
    TurnDirection(0xFE, 0x1E, 900)
    Sleep(700)
    TurnDirection(0xFE, 0x1E, 800)
    Sleep(1000)
    TurnDirection(0xFE, 0x1E, 1000)
    Sleep(1100)
    Jump("Function_9_3F56")

    label("loc_3F86")

    Return()

    # Function_9_3F56 end

    def Function_10_3F87(): pass

    label("Function_10_3F87")

    Sleep(200)

    label("loc_3F8C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FBC")
    TurnDirection(0xFE, 0x1E, 800)
    Sleep(1000)
    TurnDirection(0xFE, 0x1E, 1000)
    Sleep(700)
    TurnDirection(0xFE, 0x1E, 900)
    Sleep(1100)
    Jump("loc_3F8C")

    label("loc_3FBC")

    Return()

    # Function_10_3F87 end

    def Function_11_3FBD(): pass

    label("Function_11_3FBD")

    OP_8C(0x10C, 255, 400)

    def lambda_3FCA():
        OP_8E(0xFE, 0x202EC, 0x20A8, 0x16DDC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_3FCA)
    WaitChrThread(0x10C, 0x1)

    def lambda_3FEA():
        OP_8E(0xFE, 0x202EC, 0x20A8, 0x15F90, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 1, lambda_3FEA)
    WaitChrThread(0x10C, 0x1)
    Sleep(300)
    Return()

    # Function_11_3FBD end

    def Function_12_400A(): pass

    label("Function_12_400A")

    OP_B0(0xB, 0x32)
    OP_6F(0xB, 61)
    OP_70(0xB, 0xA0)
    OP_73(0xB)
    OP_71(0x200B, 0x0)
    ExitThread()
    OP_6F(0xB, 161)
    OP_70(0xB, 0x104)
    Return()

    # Function_12_400A end

    def Function_13_4034(): pass

    label("Function_13_4034")

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

    # Function_13_4034 end

    def Function_14_4096(): pass

    label("Function_14_4096")


    def lambda_409C():
        OP_8E(0xFE, 0x20404, 0x1FD6, 0x17700, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_409C)
    WaitChrThread(0x1A, 0x1)

    def lambda_40BC():
        OP_8E(0xFE, 0x20404, 0x1FD6, 0x141CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_40BC)
    WaitChrThread(0x1A, 0x1)
    Return()

    # Function_14_4096 end

    def Function_15_40D7(): pass

    label("Function_15_40D7")


    def lambda_40DD():
        OP_8E(0xFE, 0x1F568, 0x2008, 0x171EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_40DD)
    WaitChrThread(0x15, 0x1)

    def lambda_40FD():
        OP_8E(0xFE, 0x20404, 0x2008, 0x171EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_40FD)
    WaitChrThread(0x15, 0x1)

    def lambda_411D():
        OP_8E(0xFE, 0x20404, 0x2008, 0x141CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_411D)
    WaitChrThread(0x15, 0x1)
    Return()

    # Function_15_40D7 end

    def Function_16_4138(): pass

    label("Function_16_4138")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #101
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_4138 end

    def Function_17_4180(): pass

    label("Function_17_4180")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #102
        (
            "\x07\x05定期船起降坪\x01",
            "≡　开往柏斯市\x01",
            "≡　开往蔡斯市\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_17_4180 end

    def Function_18_41DF(): pass

    label("Function_18_41DF")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #103
        (
            "\x07\x05※请勿携带易燃物和危险品\x01",
            "　　　　　利贝尔飞艇公社\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_41DF end

    def Function_19_4245(): pass

    label("Function_19_4245")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #104
        (
            "\x07\x05　　　飞艇坪塔台　　　　\x01",
            "　※无关人员禁止入内　　\x01",
            "      『利贝尔飞艇公社』　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_19_4245 end

    SaveToFile()

Try(main)
