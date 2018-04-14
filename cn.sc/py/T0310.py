from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0310   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0310.x',
        MapIndex            = 15,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 18,
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
        '卡西乌斯',                             # 9
        '雪拉扎德',                             # 10
        '凯文神父',                             # 11
        '目标用照相机',                         # 12
        '水壶',                                 # 13
        '红茶',                                 # 14
        '红茶',                                 # 15
        '红茶',                                 # 16
        '红茶',                                 # 17
        '药罐',                                 # 18
        '莱娜',                                 # 19
        '器皿',                                 # 20
        '器皿',                                 # 21
        '器皿',                                 # 22
        '沙拉',                                 # 23
        '面包',                                 # 24
        '餐具',                                 # 25
        '餐具',                                 # 26
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
        'ED6_DT27/CH03670 ._CH',             # 00
        'ED6_DT07/CH00020 ._CH',             # 01
        'ED6_DT07/CH02003 ._CH',             # 02
        'ED6_DT07/CH00023 ._CH',             # 03
        'ED6_DT07/CH00003 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
        'ED6_DT27/CH03003 ._CH',             # 06
        'ED6_DT07/CH00053 ._CH',             # 07
        'ED6_DT07/CH00033 ._CH',             # 08
        'ED6_DT07/CH00043 ._CH',             # 09
        'ED6_DT07/CH00063 ._CH',             # 0A
        'ED6_DT07/CH00073 ._CH',             # 0B
        'ED6_DT26/CH20320 ._CH',             # 0C
        'ED6_DT07/CH02003 ._CH',             # 0D
        'ED6_DT27/CH03740 ._CH',             # 0E
        'ED6_DT26/CH20332 ._CH',             # 0F
        'ED6_DT27/CH03743 ._CH',             # 10
        'ED6_DT06/CH20008 ._CH',             # 11
        'ED6_DT27/CH03740 ._CH',             # 12
        'ED6_DT26/CH20239 ._CH',             # 13
        'ED6_DT27/CH03740 ._CH',             # 14
        'ED6_DT27/CH03080 ._CH',             # 15
        'ED6_DT26/CH20232 ._CH',             # 16
        'ED6_DT27/CH03673 ._CH',             # 17
        'ED6_DT26/CH20263 ._CH',             # 18
        'ED6_DT26/CH20278 ._CH',             # 19
    )

    AddCharChipPat(
        'ED6_DT27/CH03670P._CP',             # 00
        'ED6_DT07/CH00020P._CP',             # 01
        'ED6_DT07/CH02003P._CP',             # 02
        'ED6_DT07/CH00023P._CP',             # 03
        'ED6_DT07/CH00003P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
        'ED6_DT27/CH03003P._CP',             # 06
        'ED6_DT07/CH00053P._CP',             # 07
        'ED6_DT07/CH00033P._CP',             # 08
        'ED6_DT07/CH00043P._CP',             # 09
        'ED6_DT07/CH00063P._CP',             # 0A
        'ED6_DT07/CH00073P._CP',             # 0B
        'ED6_DT26/CH20320P._CP',             # 0C
        'ED6_DT07/CH02003P._CP',             # 0D
        'ED6_DT27/CH03740P._CP',             # 0E
        'ED6_DT26/CH20332P._CP',             # 0F
        'ED6_DT27/CH03743P._CP',             # 10
        'ED6_DT06/CH20008P._CP',             # 11
        'ED6_DT27/CH03740P._CP',             # 12
        'ED6_DT26/CH20239P._CP',             # 13
        'ED6_DT27/CH03740P._CP',             # 14
        'ED6_DT27/CH03080P._CP',             # 15
        'ED6_DT26/CH20232P._CP',             # 16
        'ED6_DT27/CH03673P._CP',             # 17
        'ED6_DT26/CH20263P._CP',             # 18
        'ED6_DT26/CH20278P._CP',             # 19
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        Unknown3            = 1703941,
        ChipIndex           = 0x5,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
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
        Unknown3            = 1703941,
        ChipIndex           = 0x5,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 655365,
        ChipIndex           = 0x5,
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
        Unknown3            = 655365,
        ChipIndex           = 0x5,
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
        Unknown3            = 655365,
        ChipIndex           = 0x5,
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
        Unknown3            = 458757,
        ChipIndex           = 0x5,
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
        Unknown3            = 1769477,
        ChipIndex           = 0x5,
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
        Unknown3            = 1376261,
        ChipIndex           = 0x5,
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
        Unknown3            = 1376261,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 72990,
        TriggerZ            = 0,
        TriggerY            = -460,
        TriggerRange        = 800,
        ActorX              = 72990,
        ActorZ              = 1000,
        ActorY              = -460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9360,
        TriggerZ            = 0,
        TriggerY            = 68590,
        TriggerRange        = 800,
        ActorX              = 9260,
        ActorZ              = 800,
        ActorY              = 68720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 70420,
        TriggerZ            = 0,
        TriggerY            = 148490,
        TriggerRange        = 500,
        ActorX              = 70420,
        ActorZ              = 500,
        ActorY              = 148490,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 146290,
        TriggerZ            = 0,
        TriggerY            = 144760,
        TriggerRange        = 800,
        ActorX              = 147910,
        ActorZ              = 1500,
        ActorY              = 144780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 72010,
        TriggerZ            = 0,
        TriggerY            = 71390,
        TriggerRange        = 800,
        ActorX              = 72570,
        ActorZ              = 1500,
        ActorY              = 72600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_46E",          # 00, 0
        "Function_1_4FB",          # 01, 1
        "Function_2_9BC",          # 02, 2
        "Function_3_B39",          # 03, 3
        "Function_4_B69",          # 04, 4
        "Function_5_B6E",          # 05, 5
        "Function_6_2628",         # 06, 6
        "Function_7_2D0B",         # 07, 7
        "Function_8_2F45",         # 08, 8
        "Function_9_4CD2",         # 09, 9
        "Function_10_5062",        # 0A, 10
        "Function_11_5076",        # 0B, 11
        "Function_12_522B",        # 0C, 12
        "Function_13_5B84",        # 0D, 13
        "Function_14_5FB9",        # 0E, 14
        "Function_15_60B9",        # 0F, 15
        "Function_16_61CB",        # 10, 16
        "Function_17_6349",        # 11, 17
        "Function_18_64C5",        # 12, 18
        "Function_19_6615",        # 13, 19
        "Function_20_66B1",        # 14, 20
        "Function_21_6703",        # 15, 21
    )


    def Function_0_46E(): pass

    label("Function_0_46E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_488")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 5)
    Jump("loc_4FA")

    label("loc_488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_4A2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    Event(0, 6)
    Jump("loc_4FA")

    label("loc_4A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_4B3")
    OP_A3(0x10F2)
    Event(0, 7)
    Jump("loc_4FA")

    label("loc_4B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_4C4")
    OP_A3(0x10F3)
    Event(0, 8)
    Jump("loc_4FA")

    label("loc_4C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_4DE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F4)
    Event(0, 9)
    Jump("loc_4FA")

    label("loc_4DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FA")
    Event(0, 16)

    label("loc_4FA")

    Return()

    # Function_0_46E end

    def Function_1_4FB(): pass

    label("Function_1_4FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_530")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_10(0x8, 0x0)
    OP_10(0x9, 0x0)
    OP_10(0xA, 0x1)
    OP_10(0xB, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x3, 0x1)
    Jump("loc_53C")

    label("loc_530")

    OP_10(0x8, 0x1)
    OP_10(0x9, 0x1)
    OP_10(0xA, 0x0)
    OP_10(0xB, 0x0)

    label("loc_53C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_554")
    OP_72(0x4, 0x10)
    OP_65(0x0, 0x1)
    Jump("loc_55D")

    label("loc_554")

    OP_71(0x4, 0x10)
    OP_64(0x0, 0x1)

    label("loc_55D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_570")
    OP_65(0x1, 0x1)
    Jump("loc_574")

    label("loc_570")

    OP_64(0x1, 0x1)

    label("loc_574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_587")
    OP_65(0x2, 0x1)
    Jump("loc_58B")

    label("loc_587")

    OP_64(0x2, 0x1)

    label("loc_58B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 4)), scpexpr(EXPR_END)), "loc_5C8")
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 3070, 200, 71390, 180)
    SetChrChipByIndex(0x8, 13)
    ClearChrFlags(0x8, 0x80)

    label("loc_5C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 4)), scpexpr(EXPR_END)), "loc_99F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F7")
    SetChrPos(0x12, -1400, 0, 3140, 90)
    ClearChrFlags(0x12, 0x80)
    OP_43(0x12, 0x0, 0x0, 0x2)
    Jump("loc_99F")

    label("loc_5F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_742")
    SetChrPos(0x12, -1400, 0, 3140, 90)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x12, 0x80)
    OP_43(0x12, 0x0, 0x0, 0x2)
    SetChrPos(0x11, -630, 800, 2940, 0)
    SetChrSubChip(0x11, 31)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x13, -8290, 800, 1250, 0)
    SetChrPos(0x14, -9800, 800, 1250, 0)
    SetChrPos(0x15, -8290, 800, 290, 0)
    SetChrPos(0x17, -7870, 800, 270, 0)
    SetChrPos(0x18, -8000, 800, 1300, 0)
    SetChrPos(0x19, -10450, 800, 1290, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrSubChip(0x13, 1)
    SetChrSubChip(0x14, 1)
    SetChrSubChip(0x15, 1)
    SetChrSubChip(0x17, 12)
    LoadEffect(0x1, "map\\\\mp068_00.eff")
    PlayEffect(0x1, 0x1, 0xFF, -630, 0, 2940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_731"),
        (101, "loc_731"),
        (104, "loc_731"),
        (SWITCH_DEFAULT, "loc_739"),
    )


    label("loc_731")

    OP_22(0x119, 0x1, 0x5A)
    Jump("loc_73F")

    label("loc_739")

    OP_23(0x119)
    Jump("loc_73F")

    label("loc_73F")

    Jump("loc_99F")

    label("loc_742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E5")
    SetChrPos(0x13, -8290, 800, 1250, 0)
    SetChrPos(0x14, -9800, 800, 1250, 0)
    SetChrPos(0x15, -8290, 800, 290, 0)
    SetChrPos(0x17, -7870, 800, 270, 0)
    SetChrPos(0x18, -8000, 800, 1300, 0)
    SetChrPos(0x19, -10450, 800, 1290, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x17, 12)
    Jump("loc_99F")

    label("loc_7E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C6")
    SetChrPos(0x12, -1560, 0, 3990, 90)
    ClearChrFlags(0x12, 0x80)
    OP_43(0x12, 0x0, 0x0, 0x2)
    SetChrPos(0x13, -8290, 800, 1250, 0)
    SetChrPos(0x14, -9800, 800, 1250, 0)
    SetChrPos(0x15, -8290, 800, 290, 0)
    SetChrPos(0x16, -640, 600, 4330, 0)
    SetChrPos(0x17, -7870, 800, 270, 0)
    SetChrPos(0x18, -8000, 800, 1300, 0)
    SetChrPos(0x19, -10450, 800, 1290, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x17, 12)
    OP_6F(0x8, 0)
    Jump("loc_99F")

    label("loc_8C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 3)), scpexpr(EXPR_END)), "loc_99F")
    SetChrPos(0x12, -7000, 0, 1420, 270)
    ClearChrFlags(0x12, 0x80)
    OP_43(0x12, 0x0, 0x0, 0x2)
    SetChrPos(0x13, -8290, 800, 1250, 0)
    SetChrPos(0x14, -9800, 800, 1250, 0)
    SetChrPos(0x15, -8290, 800, 290, 0)
    SetChrPos(0x16, -9200, 800, 800, 0)
    SetChrPos(0x17, -7870, 800, 270, 0)
    SetChrPos(0x18, -8000, 800, 1300, 0)
    SetChrPos(0x19, -10450, 800, 1290, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x15, 0)
    SetChrSubChip(0x17, 12)
    OP_6F(0x8, 15)

    label("loc_99F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9AE")
    Jump("loc_9B8")

    label("loc_9AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 5)), scpexpr(EXPR_END)), "loc_9B8")
    OP_82(0x81, 0x0)

    label("loc_9B8")

    OP_82(0x80, 0x0)
    Return()

    # Function_1_4FB end

    def Function_2_9BC(): pass

    label("Function_2_9BC")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E1")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_B23")

    label("loc_9E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FA")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_B23")

    label("loc_9FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A13")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_B23")

    label("loc_A13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2C")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_B23")

    label("loc_A2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A45")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_B23")

    label("loc_A45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5E")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_B23")

    label("loc_A5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A77")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_B23")

    label("loc_A77")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A90")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_B23")

    label("loc_A90")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA9")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_B23")

    label("loc_AA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC2")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_B23")

    label("loc_AC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADB")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_B23")

    label("loc_ADB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF4")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_B23")

    label("loc_AF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0D")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_B23")

    label("loc_B0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B23")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_B23")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B38")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_B23")

    label("loc_B38")

    Return()

    # Function_2_9BC end

    def Function_3_B39(): pass

    label("Function_3_B39")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B50")
    Call(0, 12)
    Jump("loc_B68")

    label("loc_B50")

    TalkBegin(0x8)

    ChrTalk(    #0
        0x8,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x8)

    label("loc_B68")

    Return()

    # Function_3_B39 end

    def Function_4_B69(): pass

    label("Function_4_B69")

    Call(0, 13)
    Return()

    # Function_4_B69 end

    def Function_5_B6E(): pass

    label("Function_5_B6E")

    EventBegin(0x0)
    OP_6D(-900, 0, -2790, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(50000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x142, 0x80)
    SetChrPos(0x101, -1210, 0, -5810, 0)

    def lambda_BC9():
        OP_8E(0x101, 0xFFFFFC7C, 0x0, 0xFFFFF51A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BC9)
    WaitChrThread(0x101, 0x0)
    OP_8C(0x101, 270, 400)
    Sleep(300)
    OP_8C(0x101, 0, 400)
    OP_8C(0x101, 90, 400)
    Sleep(300)

    ChrTalk(    #1
        0x101,
        (
            "#001F我回来了，约修亚！\x02\x03",

            "喂，你已经回来了对不对！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #2
        0x101,
        (
            "#505F奇怪……\x02\x03",

            "约修亚……\x01",
            "他应该已经回来了呀……\x02\x03",

            "#004F啊，一定是在老爸的书房。\x02",
        )
    )

    CloseMessageWindow()
    OP_6A(0x101)
    OP_8E(0x101, 0x128E, 0x0, 0xFFFFFBC8, 0x1388, 0x0)
    OP_8C(0x101, 0, 400)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x13)
    OP_73(0x1)
    FadeToDark(1000, 0, -1)
    OP_8E(0x101, 0x155E, 0x0, 0x8B6, 0x1388, 0x0)
    OP_0D()
    SetChrPos(0x101, 2910, 0, 65200, 0)
    OP_69(0x101, 0x0)
    FadeToBright(1000, 0)
    OP_8E(0x101, 0xD2A, 0x0, 0x10982, 0x1388, 0x0)
    OP_0D()
    OP_20(0x1388)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #3
        0x101,
        "#586F………………………………\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x142, 0x80)
    OP_8C(0x101, 180, 400)
    Sleep(500)
    FadeToDark(1000, 0, -1)

    def lambda_DA0():
        OP_8E(0xFE, 0xB0E, 0x0, 0xFB4A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DA0)
    Sleep(500)
    OP_9F(0x101, 0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_0D()
    SetChrPos(0x142, -1200, 0, -5160, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x101, 5470, 0, 2230, 180)
    OP_69(0x101, 0x0)
    FadeToBright(1000, 0)

    def lambda_E09():
        OP_8E(0x142, 0xFFFFFDD0, 0x0, 0xFFFFF4CA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E09)

    def lambda_E24():
        OP_8E(0x101, 0x12C0, 0x0, 0xFFFFF4FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 0, lambda_E24)
    Sleep(1000)
    WaitChrThread(0x142, 0x0)
    OP_44(0x101, 0x0)

    def lambda_E4D():
        TurnDirection(0x142, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E4D)

    def lambda_E5B():
        OP_8E(0x101, 0x2A3A, 0x7D0, 0xFFFFF330, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 0, lambda_E5B)
    WaitChrThread(0x142, 0x0)
    FadeToDark(1000, 0, -1)

    def lambda_E85():
        OP_8E(0x101, 0x2ABC, 0x7D0, 0xFFFFFA38, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 0, lambda_E85)
    WaitChrThread(0x142, 0x0)

    def lambda_EA5():
        OP_8E(0x101, 0x21F2, 0xFA0, 0xFFFFFAE2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 0, lambda_EA5)
    OP_0D()
    SetChrPos(0x101, 81350, 0, -1130, 270)
    OP_69(0x101, 0x0)
    FadeToBright(1000, 0)
    OP_8E(0x101, 0x125B6, 0x0, 0xFFFFFC4A, 0x1388, 0x0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #4
        0x101,
        "#004F……对了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 500)
    Sleep(500)

    ChrTalk(    #5
        0x101,
        (
            "#586F这么说的话………他有可能\x01",
            "在我的房间里啊……？\x02\x03",

            "#503F糟了，我的内衣\x01",
            "好像都胡乱放在外面了……\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x13394, 0x0, 0xFFFFFDD0, 0x1388, 0x0)
    OP_8C(0x101, 0, 400)
    OP_72(0x3, 0x10)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x13)
    OP_73(0x3)
    FadeToDark(1000, 0, -1)
    OP_8E(0x101, 0x13344, 0x0, 0x5BE, 0x1388, 0x0)
    OP_0D()
    SetChrPos(0x101, 143760, 0, 139970, 0)
    OP_69(0x101, 0x0)
    FadeToBright(1000, 0)
    OP_8E(0x101, 0x235FA, 0x0, 0x231B8, 0x1388, 0x0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #6
        0x101,
        (
            "#587F…………………………………\x02\x03",

            "#506F还好……\x01",
            "原来没有放在外面。\x02\x03",

            "呼……不过如果是约修亚的话，\x01",
            "就算看到我的内衣\x01",
            "也不会有什么反应的………………\x02\x03",

            "#586F…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    def lambda_1101():
        OP_8E(0x101, 0x23190, 0x0, 0x222C2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1101)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x1)
    SetChrPos(0x101, 78660, 0, 1470, 180)
    OP_69(0x101, 0x0)
    FadeToBright(1000, 0)
    OP_8E(0x101, 0x13434, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    OP_0D()
    OP_8E(0x101, 0x11C6A, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    OP_8E(0x101, 0x11C6A, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(500)
    OP_22(0x71, 0x0, 0x64)
    Sleep(300)
    Sleep(1000)

    ChrTalk(    #7
        0x101,
        "#586F约修亚……我进去了哦？\x02",
    )

    CloseMessageWindow()
    OP_72(0x4, 0x10)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x13)
    OP_73(0x4)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    ClearMapFlags(0x1)
    OP_8E(0x101, 0x11DF0, 0x0, 0x6D6, 0x3E8, 0x0)
    OP_0D()
    OP_6D(70660, 0, 64780, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(50000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 70820, 0, 64790, 0)
    Sleep(500)
    OP_1D(0x50)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #8
        0x101,
        "#587F…………啊。\x02",
    )

    CloseMessageWindow()

    def lambda_1297():
        OP_6D(70630, 0, 71190, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1297)

    def lambda_12AF():
        OP_67(0, 6000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12AF)
    Sleep(1000)

    def lambda_12CC():
        OP_8E(0x101, 0x113D2, 0x0, 0x1163E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12CC)
    Sleep(3000)

    def lambda_12EC():
        OP_8E(0x101, 0x113D2, 0x0, 0x1163E, 0x3B6, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12EC)
    Sleep(2000)

    def lambda_130C():
        OP_8E(0x101, 0x113D2, 0x0, 0x1163E, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_130C)
    Sleep(1000)

    def lambda_132C():
        OP_8E(0x101, 0x113D2, 0x0, 0x1163E, 0x352, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_132C)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #9
        0x101,
        "#586F唉……是…是吗…\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x101, 22)
    SetChrSubChip(0x101, 0)
    OP_22(0xD1, 0x0, 0x50)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #10
        0x101,
        "#588F我……真像个大傻瓜啊……\x02",
    )

    CloseMessageWindow()
    OP_9F(0x142, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x142, 70840, 0, 64450, 50)

    def lambda_13D4():
        OP_9F(0x142, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x142, 0, lambda_13D4)
    OP_8E(0x142, 0x113AA, 0x0, 0x109A0, 0x5DC, 0x0)
    Sleep(500)

    ChrTalk(    #11
        0x142,
        (
            "#1067F#2P他……\x01",
            "好像不在啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#003F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x142,
        (
            "#2P#1060F那还有一种可能。\x02\x03",

            "他回来以后\x01",
            "又跑到城里去了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#588F#5P……不会的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x142,
        (
            "#2P#1065F呼……\x02\x03",

            "#1063F你好像总算明白了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#003F…………………………………\x02\x03",

            "#586F事实上……\x01",
            "我早就明白的……\x02\x03",

            "约修亚已经走了……\x02\x03",

            "不会再回家…\x01",
            "这些我都明白……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x142,
        "#2P#1067F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#588F可是……\x01",
            "这个房间是最后的希望了……\x02\x03",

            "除此之外，我再也想不出\x01",
            "约修亚会去的地方……\x02\x03",

            "所以……已经彻底没希望了。\x02\x03",

            "我再也……\x01",
            "见不到约修亚了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x142,
        (
            "#2P#1063F………………………………\x02\x03",

            "#1065F现在就放弃未免太早了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#587F…………？\x02",
    )

    CloseMessageWindow()

    def lambda_1650():
        OP_6D(71130, 0, 71690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1650)
    OP_8E(0x142, 0x117EC, 0x0, 0x115DA, 0x7D0, 0x0)
    OP_8C(0x142, 270, 400)
    WaitChrThread(0x101, 0x3)
    Sleep(500)

    ChrTalk(    #21
        0x142,
        (
            "#2P#1060F命运这种东西，\x01",
            "除了女神之外谁也不能断定。\x02\x03",

            "不到最后一刻\x01",
            "怎么能自己就先放弃呢。\x02\x03",

            "最重要的，你应该想想\x01",
            "自己到底该怎么做？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#003F#6P可、可是……\x02\x03",

            "就算我想找约修亚\x01",
            "也没有任何线索……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x142,
        (
            "#2P#1060F哎呀，那也没关系。\x02\x03",

            "虽然我不知道他是什么样的人，\x01",
            "不过……\x02\x03",

            "毕竟不可能没有任何理由\x01",
            "就直接消失的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    Sleep(500)

    ChrTalk(    #24
        0x101,
        "#587F#6P……啊………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x142,
        (
            "#2P#1063F最近你是否感觉到他的\x01",
            "言行或态度和平时比有什么不同？\x02\x03",

            "或者…在他的身上\x01",
            "是否发生了什么不正常的事情。\x02\x03",

            "你一直在他的身边，\x01",
            "这些事总该有些了解吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#580F#6P……啊……！\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_20(0x5DC)
    OP_AD(0x2400B8, 0x0, 0x0, 0x3E8)
    Sleep(1200)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    OP_AD(0x2400B9, 0x0, 0x0, 0x3E8)
    Sleep(1200)
    OP_AD(0x2400BA, 0x0, 0x0, 0x3E8)
    Sleep(1200)
    OP_AD(0x2400BB, 0x0, 0x0, 0x3E8)
    Sleep(1200)
    OP_AD(0x2400BC, 0x0, 0x0, 0x3E8)
    Sleep(1200)
    OP_AD(0x2400BD, 0x0, 0x0, 0x3E8)
    Sleep(1200)
    OP_AD(0x2400BE, 0x0, 0x0, 0x3E8)
    Sleep(1200)
    OP_AE(0x3E8)
    Sleep(1000)
    SetChrName("艾丝蒂尔")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #27
        "\x07\x00#580F#3S啊啊……！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_69(0x101, 0x0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrSubChip(0x101, 0)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    Sleep(1500)

    ChrTalk(    #28
        0x101,
        (
            "#580F#6P约修亚的样子变得奇怪～？\x01",
            "确实……是在我回到那休息处之后…\x02\x03",

            "……为什么……会这样？\x02\x03",

            "为什么我……\x01",
            "一点也回忆不起那时遇到的人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x142,
        (
            "#2P#1063F没、没事吧？\x01",
            "你的脸色好差啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    Sleep(500)

    ChrTalk(    #30
        0x101,
        "#587F#6P呼…嗯……我不要紧……\x02",
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    OP_8C(0x101, 0, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #31
        0x101,
        (
            "#002F#6P是吗……\x02\x03",

            "约修亚的目的\x01",
            "是要阻止邪恶的魔法师……\x02\x03",

            "#003F如果说…我当时遇到的那个人\x01",
            "就是魔法师的话……\x02\x03",

            "如果那个人和政变的幕后黑手\x01",
            "是同一个人的话……\x02\x03",

            "那他一定还会在利贝尔\x01",
            "酝酿着什么邪恶的计划……\x02\x03",

            "#586F那么，如果我以游击士的身份\x01",
            "前去阻止他的话，也许……\x02\x03",

            "……也许……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    SetChrPos(0x8, 70740, 0, 64890, 0)

    NpcTalk(    #32
        0x8,
        "男人的声音",
        "#1P……看来你终于理清思路了啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x76)
    Sleep(500)

    def lambda_1C4F():
        TurnDirection(0x142, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x142, 0, lambda_1C4F)

    def lambda_1C5D():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1C5D)

    def lambda_1C6B():
        OP_6D(70790, 0, 70530, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C6B)

    def lambda_1C83():
        OP_67(0, 6000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C83)
    Sleep(500)
    ClearChrFlags(0x8, 0x80)
    OP_9F(0x8, 0x0, 0x0, 0x0, 0x0, 0x0)

    def lambda_1CB0():
        OP_8E(0x8, 0x112A6, 0x0, 0x10DBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1CB0)

    def lambda_1CCB():
        OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1CCB)
    Sleep(500)

    def lambda_1CE2():
        OP_8E(0x142, 0x119C2, 0x0, 0x11260, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 1, lambda_1CE2)
    WaitChrThread(0x142, 0x1)

    def lambda_1D02():
        OP_8C(0x142, 225, 400)
        ExitThread()

    QueueWorkItem(0x142, 2, lambda_1D02)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 70740, 0, 64890, 0)
    OP_9F(0x9, 0x0, 0x0, 0x0, 0x0, 0x0)

    def lambda_1D31():
        OP_8E(0x9, 0x115EE, 0x0, 0x10A72, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D31)

    def lambda_1D4C():
        OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D4C)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #33
        0x101,
        (
            "#580F#5P老爸！？雪拉姐！？\x02\x03",

            "你们…为什么会在这里…？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x142, 250, 400)
    Sleep(500)

    ChrTalk(    #34
        0x142,
        (
            "#1060F#2P……抱歉，艾丝蒂尔。\x02\x03",

            "在下船的时候，我就和\x01",
            "协会的王都支部联系过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#004F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "#025F你真是吓死我们了。\x02\x03",

            "我到处找你，刚到协会时\x01",
            "正好接到了消息。\x02\x03",

            "#524F然后就和老师一起匆匆忙忙\x01",
            "坐上了即将起飞的货船赶了过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#586F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        "#1125F#6P嗯，事情就是这样。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 55, 400)
    Sleep(500)

    ChrTalk(    #39
        0x8,
        (
            "#1120F#6P你就是凯文神父吧？\x01",
            "你这次的联络真是帮了大忙。\x02\x03",

            "非常感谢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x142, 225, 400)
    Sleep(300)

    ChrTalk(    #40
        0x142,
        (
            "#1061F#2P啊哈哈～没什么啦。\x02\x03",

            "倒是我这个局外人在这里乱掺和，\x01",
            "真是不好意思啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#003F#5P那、那个……\x02\x03",

            "老爸，我……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 6, 400)
    Sleep(200)
    OP_8C(0x142, 250, 400)
    Sleep(200)

    ChrTalk(    #42
        0x8,
        (
            "#6P#1122F我明白。\x02\x03",

            "#1125F……让你不要深入调查什么的，\x01",
            "都只是我自私的想法。\x02\x03",

            "不管是身为男人还是身为父亲，\x01",
            "我都不该把自己的意志强加给你。\x02\x03",

            "#1120F因为这个我还被雪拉扎德骂了一顿呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#586F#5P雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        (
            "#021F呵呵～姐姐这次可是\x01",
            "完全站在你这边的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "#6P#1125F虽然我早有心理准备……\x01",
            "但这臭小子突然不辞而别，\x01",
            "确实让我也很难承受。\x02\x03",

            "所以我才不愿意你也踏上\x01",
            "这条危险的道路。\x02\x03",

            "莱娜用生命保护你了，\x01",
            "我实在不想你也和莱娜一样。\x02\x03",

            "#1120F……但现在我明白了，\x01",
            "我这种自私的想法不但对不起你。\x02\x03",

            "而且也对不起你妈妈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#587F#5P老爸……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "#6P#1122F……我现在军务缠身，\x01",
            "实在不能离开。\x02\x03",

            "不然就会让那些家伙\x01",
            "有可乘之机……\x02\x03",

            "因此这一次我可能完全\x01",
            "帮不上你。\x02\x03",

            "即使如此，你的决心也没有改变吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#003F#5P……嗯。\x02\x03",

            "虽然我还远未成熟，不过…\x01",
            "现在没有别的选择了……\x02\x03",

            "#002F我必须要努力试试看了。\x02\x03",

            "阻止『噬身之蛇』的阴谋，\x01",
            "然后把约修亚带回来给你看！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "#6P#1125F是吗……\x02\x03",

            "#1122F那样的话我也就不必再多说了。\x02\x03",

            "……作为一名游击士，\x01",
            "也作为一个普通的女孩子…\x02\x03",

            "你就去走自己的路吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#586F#5P……老爸……\x02",
    )

    CloseMessageWindow()

    def lambda_239A():
        OP_6D(70500, 0, 70000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_239A)
    SetChrFlags(0x8, 0x40)
    OP_8E(0x101, 0x112B0, 0x0, 0x11008, 0xBB8, 0x0)
    SetChrPos(0x101, 70300, 0, 69450, 180)
    SetChrFlags(0x8, 0x8)
    SetChrChipByIndex(0x101, 24)
    SetChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 12)

    def lambda_23F0():
        OP_6B(2700, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_23F0)

    def lambda_2400():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x142, 3, lambda_2400)
    OP_99(0x101, 0x0, 0x3, 0x3E8)
    Sleep(1000)

    ChrTalk(    #51
        0x101,
        "#5P#588F#40W我……我……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "#6P#1125F对了……\x01",
            "有件最重要的事忘了说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#5P#587F啊……？\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x3, 0x6, 0x3E8)
    Sleep(500)

    ChrTalk(    #54
        0x8,
        (
            "#6P#1122F艾丝蒂尔，拜托你。\x02\x03",

            "──请一定帮我将约修亚…\x01",
            "那个笨蛋儿子带回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#5P#586F……啊………\x02",
    )

    CloseMessageWindow()
    OP_99(0x101, 0x9, 0xB, 0x3E8)
    OP_99(0x101, 0xB, 0x9, 0x3E8)
    Sleep(500)

    ChrTalk(    #56
        0x101,
        (
            "#5P#1080F嗯……我知道了……\x02\x03",

            "为了我们全家……\x01",
            "能再次团聚在这里一起生活……\x02\x03",

            "#006F我一定会把约修亚带回来……！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1500)
    RemoveParty(0x41, 0xFF)
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    OP_C4(0x0, 0x10)
    FadeToBright(10, 0)
    OP_0D()
    PlayMovie(0x0, "ed6_2_op.avi", 0x7, 0x0)
    Sleep(2000)
    OP_56(0x2)
    FadeToDark(2000, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E2")
    OP_20(0x7D0)

    label("loc_25E2")

    OP_21()
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    Sleep(2000)
    OP_C4(0x1, 0x10)
    Sleep(1000)
    OP_AD(0x2400A3, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/T5100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_B6E end

    def Function_6_2628(): pass

    label("Function_6_2628")

    OP_BB(0x0, 0x0, 0x200042)
    OP_BB(0x0, 0x1, 0x1E)
    OP_BD()
    EventBegin(0x0)
    OP_6D(-7800, 200, 1380, 0)
    OP_67(0, 5720, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(246, 0)
    OP_82(0x81, 0x0)
    OP_77(0xD0, 0xAE, 0x5D, 0x0, 0x0)
    SetChrPos(0x8, -8130, 200, 2260, 180)
    SetChrPos(0x9, -9800, 200, 2200, 180)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -8220, 200, -630, 0)
    SetChrChipByIndex(0x8, 23)
    SetChrChipByIndex(0x9, 3)
    SetChrChipByIndex(0x101, 4)
    SetChrSubChip(0x8, 0)
    SetChrSubChip(0x9, 0)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #57
        0x8,
        (
            "#5P#1125F──如之前所说，\x01",
            "我并不会阻止你的行动。\x02\x03",

            "但说实话，就凭你现在的实力，\x01",
            "要与结社为敌实在是以卵击石。\x02\x03",

            "#1122F所以，艾丝蒂尔……\x01",
            "要不要去『卢·洛克尔』一趟呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#587F『卢·洛克尔』？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "#5P#1122F那是位于列曼自治州，\x01",
            "游击士协会所有的训练场。\x02\x03",

            "宿舍的周围有各种各样的\x01",
            "专业训练设施。\x02\x03",

            "#1125F训练内容涉及遗迹探索、突击、\x01",
            "野外生存、反恐等等……\x02\x03",

            "要想进行实战训练的话，\x01",
            "再没有比那里更合适的地方了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#505F有那样的地方吗……\x02\x03",

            "#003F不过…自治州的话…\x01",
            "也就是说那个训练场在外国了？\x02\x03",

            "#587F要是我……\x01",
            "在这种时候离开利贝尔的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x9,
        (
            "#026F#5P虽然从理论上说是外国，\x01",
            "不过坐国际飞船的话也只是１天的路程而已。\x02\x03",

            "训练时间嘛，嗯……\x01",
            "有１个月就可以了。\x02\x03",

            "#020F在这期间如果有什么特殊情况的话\x01",
            "我们会马上和你联络的。\x02\x03",

            "这样的话如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#003F…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "#5P#1122F当然了，我只是提个建议，\x01",
            "最后的决定权在你。\x02\x03",

            "自己好好考虑一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#500F……不用了，我已经决定了。\x02\x03",

            "#002F我要接受这个训练。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        "#023F#5P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "#5P#1120F嗯，竟然这么果断。\x02\x03",

            "看来你是有\x01",
            "自己的想法吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#586F嗯……是啊。\x02\x03",

            "#003F仔细想想的话，我至今为止\x01",
            "一直都是在依赖着约修亚。\x02\x03",

            "不管发生什么事情\x01",
            "也都是靠他来指引我。\x02\x03",

            "但是，从现在起\x01",
            "我必须要依靠自己的判断力了。\x02\x03",

            "#002F所以我……\x01",
            "要去那个训练场好好锻炼一下自己。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        "#524F#5P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#5P#1125F是吗。\x02\x03",

            "#1120F那么我明天就去\x01",
            "洛连特支部向训练场\x02\x03",

            "提出训练申请。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        "#006F嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "#021F#5P那个，艾丝蒂尔……\x02\x03",

            "在出发之前一起去\x01",
            "王都的百货店逛逛如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#004F啊，怎么了啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "#027F#5P为了庆祝你成为正游击士啊。\x02\x03",

            "难得有这么值得庆贺的大事，\x01",
            "姐姐要给你买一身新衣服！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0x101, 0x4)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T5110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_2628 end

    def Function_7_2D0B(): pass

    label("Function_7_2D0B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D2B")
    Call(0, 19)
    FadeToBright(0, 0)
    Call(0, 20)

    label("loc_2D2B")

    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    LoadEffect(0x1, "map\\\\mp068_00.eff")
    OP_6D(-280, 0, 3400, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x101, 0x80)
    SetChrPos(0x103, -1410, 0, 2670, 90)
    SetChrChipByIndex(0x11, 25)
    SetChrSubChip(0x11, 1)
    SetChrPos(0x11, -600, 200, 2900, 0)
    SetChrPos(0xC, -640, 600, 4330, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0x11, 0x4)
    PlayEffect(0x0, 0x0, 0xFF, -630, 700, 2940, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0xFF, -630, 0, 2940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    SetChrPos(0xF8, -9800, 200, -630, 0)
    SetChrPos(0xF9, -8200, 200, -630, 0)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (5, "loc_2E97"),
        (3, "loc_2E9F"),
        (4, "loc_2EA7"),
        (6, "loc_2EAF"),
        (7, "loc_2EB7"),
        (SWITCH_DEFAULT, "loc_2EBF"),
    )


    label("loc_2E97")

    SetChrChipByIndex(0xF8, 7)
    Jump("loc_2EBF")

    label("loc_2E9F")

    SetChrChipByIndex(0xF8, 8)
    Jump("loc_2EBF")

    label("loc_2EA7")

    SetChrChipByIndex(0xF8, 9)
    Jump("loc_2EBF")

    label("loc_2EAF")

    SetChrChipByIndex(0xF8, 10)
    Jump("loc_2EBF")

    label("loc_2EB7")

    SetChrChipByIndex(0xF8, 11)
    Jump("loc_2EBF")

    label("loc_2EBF")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_2EDC"),
        (3, "loc_2EE4"),
        (4, "loc_2EEC"),
        (6, "loc_2EF4"),
        (7, "loc_2EFC"),
        (SWITCH_DEFAULT, "loc_2F04"),
    )


    label("loc_2EDC")

    SetChrChipByIndex(0xF9, 7)
    Jump("loc_2F04")

    label("loc_2EE4")

    SetChrChipByIndex(0xF9, 8)
    Jump("loc_2F04")

    label("loc_2EEC")

    SetChrChipByIndex(0xF9, 9)
    Jump("loc_2F04")

    label("loc_2EF4")

    SetChrChipByIndex(0xF9, 10)
    Jump("loc_2F04")

    label("loc_2EFC")

    SetChrChipByIndex(0xF9, 11)
    Jump("loc_2F04")

    label("loc_2F04")

    FadeToBright(1500, 0)

    def lambda_2F13():
        OP_6D(-7440, 0, 2710, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F13)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0300   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_7_2D0B end

    def Function_8_2F45(): pass

    label("Function_8_2F45")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F65")
    Call(0, 19)
    FadeToBright(0, 0)
    Call(0, 20)

    label("loc_2F65")

    OP_6D(-8260, 200, 1880, 0)
    OP_67(0, 4880, -10000, 0)
    OP_6B(2740, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    SetChrPos(0x103, -8130, 200, 2260, 180)
    SetChrPos(0x101, -9800, 200, 2200, 180)
    SetChrPos(0xF8, -9800, 200, -630, 0)
    SetChrPos(0xF9, -8200, 200, -630, 0)
    SetChrChipByIndex(0x101, 6)
    SetChrChipByIndex(0x103, 3)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (5, "loc_3021"),
        (3, "loc_3029"),
        (4, "loc_3031"),
        (6, "loc_3039"),
        (7, "loc_3041"),
        (SWITCH_DEFAULT, "loc_3049"),
    )


    label("loc_3021")

    SetChrChipByIndex(0xF8, 7)
    Jump("loc_3049")

    label("loc_3029")

    SetChrChipByIndex(0xF8, 8)
    Jump("loc_3049")

    label("loc_3031")

    SetChrChipByIndex(0xF8, 9)
    Jump("loc_3049")

    label("loc_3039")

    SetChrChipByIndex(0xF8, 10)
    Jump("loc_3049")

    label("loc_3041")

    SetChrChipByIndex(0xF8, 11)
    Jump("loc_3049")

    label("loc_3049")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (5, "loc_3066"),
        (3, "loc_306E"),
        (4, "loc_3076"),
        (6, "loc_307E"),
        (7, "loc_3086"),
        (SWITCH_DEFAULT, "loc_308E"),
    )


    label("loc_3066")

    SetChrChipByIndex(0xF9, 7)
    Jump("loc_308E")

    label("loc_306E")

    SetChrChipByIndex(0xF9, 8)
    Jump("loc_308E")

    label("loc_3076")

    SetChrChipByIndex(0xF9, 9)
    Jump("loc_308E")

    label("loc_307E")

    SetChrChipByIndex(0xF9, 10)
    Jump("loc_308E")

    label("loc_3086")

    SetChrChipByIndex(0xF9, 11)
    Jump("loc_308E")

    label("loc_308E")

    SetChrChipByIndex(0x11, 25)
    SetChrSubChip(0x11, 1)
    SetChrPos(0x11, -600, 200, 2900, 0)
    SetChrPos(0xC, -9100, 800, 800, 0)
    SetChrPos(0xC, -640, 600, 4330, 0)
    SetChrPos(0xD, -9800, 800, 1100, 0)
    SetChrPos(0xE, -8500, 800, 1100, 0)
    SetChrPos(0xF, -9800, 800, 100, 0)
    SetChrPos(0x10, -8500, 800, 100, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #74
        0x101,
        (
            "#1016F#5P呼～\x01",
            "总算是到家了。\x02\x03",

            "#1017F外边都是雾气，\x01",
            "什么都看不清楚啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x103,
        "#021F呵呵，确实哦。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32E4")

    ChrTalk(    #76
        0x106,
        (
            "#051F看起来……雪拉扎德。\x02\x03",

            "你好像对这里的事情\x01",
            "很了解啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x103,
        (
            "#524F嗯，是啊。\x02\x03",

            "我和这个家可是\x01",
            "有着很深厚的感情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1015F#5P从我妈妈还活着的\x01",
            "时候开始……\x02\x03",

            "#1001F到现在已经有十几年了呢。  \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x103,
        "#526F嗯，是呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x107,
        (
            "#560F听说雪拉姐以前\x01",
            "是四处旅行的艺人呢。\x02\x03",

            "那后来是怎么和姐姐\x01",
            "认识的呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E59")

    label("loc_32E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3432")

    ChrTalk(    #81
        0x106,
        (
            "#051F看起来……雪拉扎德。\x02\x03",

            "你好像对这里的事情\x01",
            "很了解啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x103,
        (
            "#524F嗯，是啊。\x02\x03",

            "我和这个家可是\x01",
            "有着很深厚的感情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#1015F#5P从我妈妈还活着的\x01",
            "时候开始……\x02\x03",

            "#1001F到现在已经有十几年了呢。  \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x103,
        "#526F嗯，是呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x104,
        (
            "#030F雪拉以前好像是位\x01",
            "周游各地的艺人吧？\x02\x03",

            "是在怎样的机缘之下和艾丝蒂尔\x01",
            "相识的呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E59")

    label("loc_3432")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3580")

    ChrTalk(    #86
        0x106,
        (
            "#051F看起来……雪拉扎德。\x02\x03",

            "你好像对这里的事情\x01",
            "很了解啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x103,
        (
            "#524F嗯，是啊。\x02\x03",

            "我和这个家可是\x01",
            "有着很深厚的感情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        (
            "#1015F#5P从我妈妈还活着的\x01",
            "时候开始……\x02\x03",

            "#1001F到现在已经有十几年了呢。  \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x103,
        "#526F嗯，是呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x105,
        (
            "#048F听说雪拉小姐你以前是位\x01",
            "周游各地的艺人吧？\x02\x03",

            "那后来是怎么和艾丝蒂尔\x01",
            "认识的呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E59")

    label("loc_3580")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36C4")

    ChrTalk(    #91
        0x106,
        (
            "#051F看起来……雪拉扎德。\x02\x03",

            "你好像对这里的事情\x01",
            "很了解啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x103,
        (
            "#524F嗯，是啊。\x02\x03",

            "我和这个家可是\x01",
            "有着很深厚的感情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1015F#5P从我妈妈还活着的\x01",
            "时候开始……\x02\x03",

            "#1001F到现在已经有十几年了呢。  \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x103,
        "#526F嗯，是呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x108,
        (
            "#070F你以前好像是位\x01",
            "周游各地的艺人吧？\x02\x03",

            "后来是怎么和艾丝蒂尔\x01",
            "认识的呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E59")

    label("loc_36C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3804")

    ChrTalk(    #96
        0x104,
        (
            "#030F话说回来，雪拉。\x02\x03",

            "你对这里的事情\x01",
            "还真是熟悉啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x103,
        (
            "#524F嗯，是啊。\x02\x03",

            "我和这个家可是\x01",
            "有着很深厚的感情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#1015F#5P从我妈妈还活着的\x01",
            "时候开始……\x02\x03",

            "#1001F到现在已经有十几年了呢。  \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x103,
        "#526F嗯，是呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x107,
        (
            "#560F听说雪拉姐以前\x01",
            "是四处旅行的艺人呢。\x02\x03",

            "那后来是怎么和姐姐\x01",
            "认识的呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E59")

    label("loc_3804")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3944")

    ChrTalk(    #101
        0x107,
        (
            "#560F雪拉姐好像对姐姐的家\x01",
            "很熟悉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x103,
        (
            "#524F呵呵，这个嘛。\x02\x03",

            "我和这个家可是\x01",
            "有着很深厚的感情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        (
            "#1015F#5P从我妈妈还活着的\x01",
            "时候开始……\x02\x03",

            "#1001F到现在已经有十几年了呢。  \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x103,
        "#526F嗯，是呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x105,
        (
            "#048F听说雪拉扎德你以前是位\x01",
            "四处旅行的艺人呢。  \x02\x03",

            "那后来是怎么和艾丝蒂尔\x01",
            "认识的呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E59")

    label("loc_3944")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A7A")

    ChrTalk(    #106
        0x107,
        (
            "#560F雪拉姐好像对姐姐的家\x01",
            "很熟悉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x103,
        (
            "#524F呵呵，这个嘛。\x02\x03",

            "我和这个家可是\x01",
            "有着很深厚的感情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#1015F#5P从我妈妈还活着的\x01",
            "时候开始……\x02\x03",

            "#1001F到现在已经有十几年了呢。  \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x103,
        "#526F嗯，是呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x108,
        (
            "#070F你以前好像是位\x01",
            "四处旅行的艺人呢。  \x02\x03",

            "后来是怎么和艾丝蒂尔\x01",
            "认识的呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E59")

    label("loc_3A7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BC6")

    ChrTalk(    #111
        0x104,
        (
            "#030F话说回来，雪拉。\x02\x03",

            "你对这里的事情\x01",
            "还真是熟悉啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x103,
        (
            "#524F嗯，是啊。\x02\x03",

            "我和这个家可是\x01",
            "有着很深厚的感情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1015F#5P从我妈妈还活着的\x01",
            "时候开始……\x02\x03",

            "#1001F到现在已经有十几年了呢。  \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x103,
        "#526F嗯，是呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x105,
        (
            "#048F听说雪拉扎德你以前是位\x01",
            "四处旅行的艺人呢。  \x02\x03",

            "那后来是怎么和艾丝蒂尔\x01",
            "认识的呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E59")

    label("loc_3BC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D08")

    ChrTalk(    #116
        0x104,
        (
            "#030F话说回来，雪拉。\x02\x03",

            "你对这里的事情\x01",
            "还真是熟悉啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        (
            "#524F嗯，是啊。\x02\x03",

            "我和这个家可是\x01",
            "有着很深厚的感情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1015F#5P从我妈妈还活着的\x01",
            "时候开始……\x02\x03",

            "#1001F到现在已经有十几年了呢。  \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x103,
        "#526F嗯，是呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x108,
        (
            "#070F你以前好像是位\x01",
            "四处旅行的艺人呢。  \x02\x03",

            "后来是怎么和艾丝蒂尔\x01",
            "认识的呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E59")

    label("loc_3D08")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E59")

    ChrTalk(    #121
        0x108,
        (
            "#070F对了，雪拉扎德。\x02\x03",

            "你对这里的事情\x01",
            "好像很熟悉的样子啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x103,
        (
            "#524F呵呵，这个嘛。\x02\x03",

            "我和这个家可是\x01",
            "有着很深厚的感情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        (
            "#1015F#5P从我妈妈还活着的\x01",
            "时候开始……\x02\x03",

            "#1001F到现在已经有十几年了呢。  \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x103,
        "#526F嗯，是呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x105,
        (
            "#040F雪拉小姐以前好像是个\x01",
            "是四处旅行的艺人呢。\x02\x03",

            "那后来是怎么和艾丝蒂尔\x01",
            "认识的呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E59")


    ChrTalk(    #126
        0x103,
        "#021F呵呵，这个嘛……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    Sleep(300)
    OP_62(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)

    ChrTalk(    #127
        0x101,
        "#1004F#1P等、等一下啦，雪拉姐。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0)
    Sleep(75)
    SetChrSubChip(0x103, 2)

    ChrTalk(    #128
        0x103,
        "#027F说说也没关系啦，反正是那么久之前的事了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0)
    OP_63(0x101)
    Sleep(500)

    ChrTalk(    #129
        0x103,
        (
            "#026F那是１２年前的事了……\x02\x03",

            "我们的戏团来洛连特\x01",
            "进行演出。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(90, 330, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #130
        (
            "\x07\x00#027F那个时候的艾丝蒂尔\x01",
            "好奇心只怕是比现在还要旺盛，\x02\x03",

            "在演出结束后总是一个人跑进\x01",
            "我们的帐篷里玩。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x24007D, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(90, 330, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #131
        (
            "#524F……身为旅行艺人，\x01",
            "说白了只不过是一群『流浪者』而已，\x02\x03",

            "一般来说，当地的市民是\x01",
            "不会主动来接近我们的。\x01",
            "所以一开始大家都有点不知所措……\x02\x03",

            "#021F呵呵，总之就是个天不怕地不怕的孩子。\x02\x03",

            "之后她每天都跑来玩，没多久便和\x01",
            "大家都混熟了。\x02\x03",

            "#526F当然也包括我在内。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x24007E, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(90, 330, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #132
        (
            "#026F有一天，日暮时分\x01",
            "玩到天黑才要回家……\x02\x03",

            "没办法，只能由我送她\x01",
            "回家去。\x02\x03",

            "#027F我和卡西乌斯老师，\x01",
            "还有艾丝蒂尔的妈妈莱娜，\x01",
            "就是在那个时候认识的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x103, 0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4214")

    ChrTalk(    #133
        0x107,
        (
            "#061F哇……\x01",
            "原来是那样的啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E1")

    label("loc_4214")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4246")

    ChrTalk(    #134
        0x106,
        (
            "#051F唉……\x01",
            "竟然是这样的啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E1")

    label("loc_4246")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_427C")

    ChrTalk(    #135
        0x104,
        (
            "#031F呼……\x01",
            "原来发生过那样的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E1")

    label("loc_427C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42B0")

    ChrTalk(    #136
        0x105,
        (
            "#048F呼呼……\x01",
            "原来是那样的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42E1")

    label("loc_42B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42E1")

    ChrTalk(    #137
        0x108,
        (
            "#071F哈哈……\x01",
            "竟然是这样的啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_431F")

    ChrTalk(    #138
        0x107,
        (
            "#061F嘿嘿，姐姐果然\x01",
            "从小时候就是这样呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4444")

    label("loc_431F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_436B")

    ChrTalk(    #139
        0x106,
        (
            "#051F呵～这天不怕地不怕的性格，\x01",
            "原来从小时候就有了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4444")

    label("loc_436B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43B5")

    ChrTalk(    #140
        0x104,
        (
            "#031F呼～从小时候开始就是\x01",
            "这种天不怕地不怕的性格啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4444")

    label("loc_43B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43FD")

    ChrTalk(    #141
        0x105,
        (
            "#048F呵呵，天不怕地不怕的性格\x01",
            "从小时候就开始了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4444")

    label("loc_43FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4444")

    ChrTalk(    #142
        0x108,
        (
            "#071F哈哈，天不怕地不怕的性格\x01",
            "原来从小时候就有了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4444")


    ChrTalk(    #143
        0x101,
        (
            "#1016F#5P啊、啊哈哈……\x02\x03",

            "那时我才只有４岁嘛～\x01",
            "都已经记不太清楚了……\x02\x03",

            "#1017F不过，从那以后，\x01",
            "雪拉姐每次再来洛连特演出时\x01",
            "都会来我家玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x103,
        "#021F呵呵，是啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45F9")

    ChrTalk(    #145
        0x106,
        (
            "#050F不过，雪拉扎德，\x02\x03",

            "身为旅行艺人的你，\x01",
            "为什么会在利贝尔\x01",
            "当起了游击士了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x103,
        (
            "#524F……中间发生了好多事情。\x02\x03",

            "８年前，在我决定成为游击士的时候，\x01",
            "所拜托的人就是卡西乌斯老师。\x02\x03",

            "自那以后我就一直留在利贝尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x106,
        (
            "#053F是这样啊……\x01",
            "你也是因为那个大叔…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48F7")

    label("loc_45F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46F1")

    ChrTalk(    #148
        0x104,
        (
            "#030F不过，雪拉……\x02\x03",

            "身为旅行艺人的你，\x01",
            "为什么会在利贝尔当起了游击士？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x103,
        (
            "#524F……中间发生了好多事情。\x02\x03",

            "８年前，在我决定成为游击士的时候，\x01",
            "所拜托的人就是卡西乌斯老师。\x02\x03",

            "自那以后我就一直留在利贝尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x104,
        "#035F嗯，是这样啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_48F7")

    label("loc_46F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47F1")

    ChrTalk(    #151
        0x108,
        (
            "#073F不过，雪拉扎德，\x02\x03",

            "身为旅行艺人的你，\x01",
            "为什么会在利贝尔当起了游击士？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x103,
        (
            "#524F……中间发生了好多事情。\x02\x03",

            "８年前，在我决定成为游击士的时候，\x01",
            "所拜托的人就是卡西乌斯老师。\x02\x03",

            "自那以后我就一直留在利贝尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x108,
        "#070F原来如此，是这样啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_48F7")

    label("loc_47F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48F7")

    ChrTalk(    #154
        0x107,
        (
            "#064F那个，所谓的旅行艺人，\x01",
            "是要在各国巡回演出的吧？\x02\x03",

            "为什么最后会留在利贝尔\x01",
            "当游击士呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x103,
        (
            "#524F……中间发生了好多事情。\x02\x03",

            "８年前，在我决定成为游击士的时候，\x01",
            "所拜托的人就是卡西乌斯老师。\x02\x03",

            "自那以后我就一直留在利贝尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x107,
        "#560F是这样啊……\x02",
    )

    CloseMessageWindow()

    label("loc_48F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_494F")

    ChrTalk(    #157
        0x105,
        (
            "#044F啊，说起来的话……\x02\x03",

            "#542F那个时候，约修亚\x01",
            "已经来到你家了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A5C")

    label("loc_494F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49AD")

    ChrTalk(    #158
        0x107,
        (
            "#064F啊，说起来的话……\x02\x03",

            "#560F啊，那个时候，\x01",
            "约修亚哥哥也在姐姐家了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A5C")

    label("loc_49AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A05")

    ChrTalk(    #159
        0x108,
        (
            "#074F嗯，说起来的话……\x02\x03",

            "#070F约修亚那小子当时\x01",
            "已经住在你家了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A5C")

    label("loc_4A05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A5C")

    ChrTalk(    #160
        0x104,
        (
            "#035F嗯，说起来的话……\x02\x03",

            "#030F在那个时候，\x01",
            "约修亚已经来到你家了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A5C")


    ChrTalk(    #161
        0x101,
        (
            "#1025F#5P啊，还没有……\x02\x03",

            "老爸收养约修亚\x01",
            "是３年之后的事情了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #162
        0x101,
        (
            "#1011F#5P就在雪拉姐为了成为正游击士\x01",
            "而周游全国的时候，没错吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x103,
        (
            "#027F嗯嗯，确实是的。\x02\x03",

            "#021F旅行归来的时候，\x01",
            "忽然就介绍一个陌生的男孩给我认识，\x02\x03",

            "当时还真是吃了一惊呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #164
        (
            "\x07\x05之后，艾丝蒂尔一行人\x01",
            "继续谈天说地……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #165
        (
            "\x07\x05最后以茶代酒，约定\x01",
            "以后再来此聚会。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_82(0x81, 0x0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x0, -1160, 0, -2760, 171)
    SetChrPos(0x1, -1160, 0, -2760, 171)
    SetChrPos(0x2, -1160, 0, -2760, 171)
    SetChrPos(0x3, -1160, 0, -2760, 171)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x103, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0xF8, 0x4)
    ClearChrFlags(0xF9, 0x4)
    OP_6D(-1160, 0, -2760, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_A2(0x180D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CC9")
    OP_28(0x8F, 0x1, 0x2000)
    OP_28(0x8F, 0x1, 0x4000)
    Jump("loc_4CCF")

    label("loc_4CC9")

    OP_28(0x8F, 0x1, 0x100)

    label("loc_4CCF")

    EventEnd(0x0)
    Return()

    # Function_8_2F45 end

    def Function_9_4CD2(): pass

    label("Function_9_4CD2")

    EventBegin(0x0)
    SetChrChipByIndex(0x11, 25)
    SetChrSubChip(0x11, 1)
    SetChrPos(0x11, -600, 200, 2900, 0)
    SetChrPos(0xD, -9600, 800, 1100, 0)
    SetChrPos(0x14, -9950, 800, 1250, 0)
    SetChrPos(0xE, -8100, 800, 1100, 0)
    SetChrPos(0x13, -8500, 800, 1250, 0)
    SetChrPos(0xF, -8600, 800, 100, 0)
    SetChrPos(0x15, -8100, 800, 290, 0)
    SetChrPos(0x16, -9450, 800, 600, 0)
    SetChrPos(0xC, -640, 600, 4330, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    LoadEffect(0x1, "map\\\\mp068_00.eff")
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -8290, 200, -480, 0)
    SetChrChipByIndex(0x101, 12)
    SetChrPos(0x8, -9790, 200, 2290, 180)
    SetChrChipByIndex(0x8, 13)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x12, -1570, 0, 2810, 90)
    SetChrChipByIndex(0x12, 14)
    ClearChrFlags(0x12, 0x80)
    OP_6D(-1610, 200, 3420, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(338, 0)
    PlayEffect(0x0, 0x0, 0xFF, -630, 750, 2940, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0xFF, -630, 0, 2940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_82(0x0, 0x0)
    Sleep(1000)
    OP_8E(0x12, 0xFFFFFA1A, 0x0, 0x1040, 0x3E8, 0x0)
    OP_8C(0x12, 90, 400)
    Sleep(300)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
    SetChrChipByIndex(0x12, 15)
    SetChrSubChip(0x12, 3)
    Sleep(300)
    OP_8C(0x12, 0, 300)
    OP_8C(0x12, 270, 300)

    def lambda_4F27():
        OP_6D(-8470, 200, 1050, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F27)

    def lambda_4F3F():
        OP_6E(270, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F3F)
    OP_8F(0x12, 0xFFFFE4A8, 0xC8, 0x366, 0x7D0, 0x0)
    Sleep(500)
    SetChrPos(0xC, -7750, 800, 800, 0)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
    SetChrChipByIndex(0x12, 14)
    Sleep(500)
    OP_62(0x101, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x8, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_8E(0x12, 0xFFFFE4A8, 0xC8, 0x834, 0x3E8, 0x0)
    OP_8E(0x12, 0xFFFFE340, 0xC8, 0x834, 0x3E8, 0x0)
    Fade(500)
    SetChrPos(0x12, -8240, 200, 2200, 180)
    SetChrChipByIndex(0x12, 16)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #166
        "\x07\x05一家三人围在餐桌上的早晨……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T0300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_4CD2 end

    def Function_10_5062(): pass

    label("Function_10_5062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5071")
    Call(0, 11)
    Jump("loc_5075")

    label("loc_5071")

    Call(0, 15)

    label("loc_5075")

    Return()

    # Function_10_5062 end

    def Function_11_5076(): pass

    label("Function_11_5076")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51B9")
    Fade(1000)
    OP_6D(73010, 0, -730, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 73010, 0, -730, 0)
    OP_0D()
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #167
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #168
        0x101,
        (
            "#293F#6P啊……\x02\x03",

            "这个房间\x01",
            "是做什么的呢？\x02\x03",

            "#296F嗯……～？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)
    Sleep(300)

    ChrTalk(    #169
        0x101,
        (
            "#291F#6P……不知道呢。\x02\x03",

            "#290F去找爸爸和妈妈\x01",
            "问问看吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1835)
    Jump("loc_5223")

    label("loc_51B9")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #170
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #171
        0x101,
        (
            "#290F去找爸爸和妈妈\x01",
            "问问看吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5223")

    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_11_5076 end

    def Function_12_522B(): pass

    label("Function_12_522B")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_52BB")
    Jump("loc_52FD")

    label("loc_52BB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52D7")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_52FD")

    label("loc_52D7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52F3")
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_52FD")

    label("loc_52F3")

    OP_51(0x8, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_52FD")

    OP_51(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5537")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5499")

    ChrTalk(    #172
        0x8,
        (
            "#080F怎么了，艾丝蒂尔？\x02\x03",

            "果然还是想和爸爸\x01",
            "一起玩吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        "#291F嘿嘿～才不是呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x8,
        "#083F唉，是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        (
            "#290F爸爸你在看\x01",
            "什么书呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x8,
        (
            "#084F这本吗？\x02\x03",

            "#080F是『各国的游击士协会』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        "#293F油鸡石～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x8,
        (
            "#080F这种书对你而言\x01",
            "还有些难懂呢。\x02\x03",

            "#081F对了，爸爸也像妈妈那样\x01",
            "读小人书给你听怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        "#291F嘿～今天不要啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x8,
        "#083F是、是吗……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_5534")

    label("loc_5499")


    ChrTalk(    #181
        0x8,
        (
            "#085F利贝尔的游击士协会\x01",
            "只有格兰赛尔一处。\x02\x03",

            "如果能在各地都建立支部的话\x01",
            "就可以分担军队的压力了……\x02\x03",

            "#082F嗯，等休假结束以后\x01",
            "去找摩尔根将军商量一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5534")

    Jump("loc_5B7B")

    label("loc_5537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5801")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57BA")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(3860, 0, 71420, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 4250, 0, 71160, 285)
    SetChrSubChip(0x8, 1)
    OP_0D()
    Sleep(200)

    ChrTalk(    #182
        0x101,
        (
            "#290F#2P喂～爸爸～\x02\x03",

            "２楼最里面的那个房间\x01",
            "里面有什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x8,
        (
            "#080F#6P啊啊，那里\x01",
            "只是储物用的房间而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x101,
        "#293F#2P储物？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x8,
        (
            "#080F#6P就是把平时不经常用的东西\x01",
            "堆在里面存放的意思。\x02\x03",

            "最近一直都没有进去过，\x01",
            "里面也许都结出蜘蛛网了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#296F#2P呼……\x02\x03",

            "#290F那门的钥匙\x01",
            "放在哪里了啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x8,
        (
            "#080F#6P啊，那个啊……\x02\x03",

            "#084F……等一下。\x01",
            "你到那里要做什么啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        (
            "#291F#2P嗯…………\x01",
            "人家想去探险呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x8,
        (
            "#083F#6P那……就随你高兴吧。\x02\x03",

            "#080F钥匙应该被你妈妈\x01",
            "收到什么地方去了，\x02\x03",

            "去问她好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        "#291F#2P嗯！知道啦！\x02",
    )

    CloseMessageWindow()
    OP_82(0x1, 0x0)
    OP_A2(0x1836)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Jump("loc_57FE")

    label("loc_57BA")


    ChrTalk(    #191
        0x8,
        (
            "#080F储物室的钥匙应该被你妈妈\x01",
            "收到什么地方去了，\x02\x03",

            "去问她好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57FE")

    Jump("loc_5B7B")

    label("loc_5801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5903")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58A2")

    ChrTalk(    #192
        0x8,
        (
            "#080F哦，找到钥匙了吗？\x02\x03",

            "里面大概已经堆积了很多灰尘了，\x01",
            "玩耍时不要把衣服弄得太脏啊。\x02\x03",

            "不然妈妈可是会发火的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x101,
        "#291F嗯，我知道啦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_5900")

    label("loc_58A2")


    ChrTalk(    #194
        0x8,
        (
            "#080F里面大概已经堆积了很多灰尘了，\x01",
            "玩耍时不要把衣服弄得太脏啊。\x02\x03",

            "不然妈妈可是会发火的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5900")

    Jump("loc_5B7B")

    label("loc_5903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B2B")

    ChrTalk(    #195
        0x8,
        (
            "#084F啊，怎么？\x02\x03",

            "很漂亮的\x01",
            "口琴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        (
            "#290F这个是在储物室里找到的。\x02\x03",

            "不是\x01",
            "爸爸的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x8,
        (
            "#080F啊，不是……\x02\x03",

            "而且好像也不是莱娜的东西，\x01",
            "究竟是哪里来的呢？\x02\x03",

            "#084F嗯……拿给我看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        "#293F嗯，给。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #199
        "\x07\x05艾丝蒂尔把口琴交给卡西乌斯。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #200
        0x8,
        (
            "#084F利威尔特社……\x01",
            "这个东西不是帝国制造的吗？\x02\x03",

            "#083F实在想不出来\x01",
            "会是谁的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x101,
        "#293F？？？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #202
        "\x07\x05卡西乌斯把口琴还给了艾丝蒂尔。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #203
        0x8,
        (
            "#080F算了，既然被你发现了，\x01",
            "就说明你和它有种缘分，\x02\x03",

            "有兴趣的话学着吹吹吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        "#290F嗯……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_5B7B")

    label("loc_5B2B")


    ChrTalk(    #205
        0x8,
        (
            "#080F算了，既然被你发现了，\x01",
            "就说明你和它有种缘分，\x02\x03",

            "有兴趣的话学着吹吹吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B7B")

    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Return()

    # Function_12_522B end

    def Function_13_5B84(): pass

    label("Function_13_5B84")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C98")

    ChrTalk(    #206
        0x12,
        (
            "#860F对了，昨天咱们吃的\x01",
            "是砂锅……\x02\x03",

            "#861F那…今天晚上\x01",
            "就吃煎蛋卷吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        (
            "#293F真的吗！？\x02\x03",

            "#291F哇———太好了！\x01",
            "我最喜欢吃妈妈做的\x01",
            "煎蛋卷了～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x12,
        (
            "#864F哎呀～\x01",
            "竟然那么高兴吗？\x02\x03",

            "#866F呵呵，妈妈和爸爸\x01",
            "也都很喜欢那个，\x01",
            "真是一家子煎蛋卷爱好者啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_5CF8")

    label("loc_5C98")


    ChrTalk(    #209
        0x12,
        (
            "#865F今天的晚饭是\x01",
            "你最爱吃的鸡肉煎蛋卷。\x02\x03",

            "配菜是\x01",
            "洋葱奶汁烤菜\x01",
            "和野菜沙拉。\x02\x03",

            "要多吃一点哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CF8")

    Jump("loc_5FB5")

    label("loc_5CFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D48")

    ChrTalk(    #210
        0x12,
        (
            "#860F对不起哦，艾丝蒂尔。\x02\x03",

            "妈妈现在要生火了，\x01",
            "退后一点好吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FB5")

    label("loc_5D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E0B")

    ChrTalk(    #211
        0x12,
        (
            "#861F呵呵呵，把钥匙\x01",
            "找到了啊，真了不起。\x02\x03",

            "#860F在里面不要挪动重物，\x01",
            "也别摸看起来很锋利的东西哦，\x01",
            "那样可是会受伤的。\x02\x03",

            "还有～探险回来以后\x01",
            "别忘了洗手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        "#291F嗯！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_5E7B")

    label("loc_5E0B")


    ChrTalk(    #213
        0x12,
        (
            "#860F在里面不要挪动重物，\x01",
            "也别摸看起来很锋利的东西哦，\x01",
            "那样可是会受伤的。\x02\x03",

            "还有～探险回来以后\x01",
            "别忘了洗手。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E7B")

    Jump("loc_5FB5")

    label("loc_5E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 3)), scpexpr(EXPR_END)), "loc_5FB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F61")

    ChrTalk(    #214
        0x12,
        (
            "#864F哎呀……\x01",
            "好漂亮的口琴。\x02\x03",

            "#865F难道是在\x01",
            "储物室发现的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x101,
        (
            "#291F嘿嘿……\x02\x03",

            "#290F这个是\x01",
            "妈妈的东西吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x12,
        (
            "#860F不是啊，\x01",
            "那个不是妈妈的东西。\x02\x03",

            "爸爸也是从来\x01",
            "不吹口琴的……\x02\x03",

            "到底是谁用过的东西呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_5FB5")

    label("loc_5F61")


    ChrTalk(    #217
        0x12,
        (
            "#861F呵呵呵～看来你的大冒险\x01",
            "成功完成了呀。\x02\x03",

            "#866F马上就要开饭啦，\x01",
            "快去洗手吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FB5")

    TalkEnd(0x12)
    Return()

    # Function_13_5B84 end

    def Function_14_5FB9(): pass

    label("Function_14_5FB9")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(8940, 0, 68850, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 8950, 0, 68820, 90)
    OP_0D()
    Sleep(200)

    ChrTalk(    #218
        0x101,
        (
            "#296F#6P嗯嗯……\x01",
            "最上面的抽屉是吧… \x02\x03",

            "#292F翻啊翻……\x02\x03",

            "#291F啊……找到啦！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #219
        "\x07\x00得到了\x1F\xF8\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3F8, 1)
    OP_64(0x1, 0x1)
    OP_A2(0x1838)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_14_5FB9 end

    def Function_15_60B9(): pass

    label("Function_15_60B9")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(73010, 0, -730, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 73010, 0, -730, 0)
    OP_0D()
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #220
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用储物室钥匙】\x01",      # 0
            "【放弃】\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61C3")
    OP_22(0x73, 0x0, 0x64)
    OP_71(0x4, 0x10)
    OP_64(0x0, 0x1)
    OP_A2(0x1839)

    label("loc_61C3")

    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_15_60B9 end

    def Function_16_61CB(): pass

    label("Function_16_61CB")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    OP_6D(71060, 0, 149350, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(31000, 0)
    OP_6E(237, 0)
    FadeToBright(1000, 0)
    Sleep(500)

    def lambda_6223():
        OP_6D(70550, 0, 144740, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6223)

    def lambda_623B():
        OP_6E(280, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_623B)

    def lambda_624B():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_624B)
    Sleep(1000)
    SetChrPos(0x101, 70970, 0, 139960, 0)
    ClearChrFlags(0x101, 0x80)
    OP_8E(0x101, 0x11396, 0x0, 0x23564, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #221
        0x101,
        (
            "#291F哇……\x01",
            "堆放着好多东西啊！\x02\x03",

            "#293F啊……可是……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8C(0x101, 90, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    Sleep(500)
    OP_62(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #222
        0x101,
        (
            "#295F真奇怪啊……\x02\x03",

            "为什么胸口会有这种\x01",
            "异样的感觉呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x183A)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_16_61CB end

    def Function_17_6349(): pass

    label("Function_17_6349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64C4")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(70730, 0, 149460, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(28000, 0)
    OP_6E(233, 0)
    SetChrPos(0x101, 70540, 0, 147820, 0)
    OP_0D()
    Sleep(1000)
    OP_6F(0x8, 0)
    OP_70(0x8, 0xF)
    OP_22(0x2B, 0x0, 0x64)
    OP_73(0x8)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #223
        "\x07\x00得到了\x1F\xF9\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3F9, 1)

    ChrTalk(    #224
        0x101,
        (
            "#291F哇！真漂亮……\x02\x03",

            "#290F这个……\x01",
            "是吹奏的乐器啊。\x02\x03",

            "要不要试着\x01",
            "吹一下呢？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    SetChrPos(0x101, 70340, 0, 147390, 0)
    OP_6D(70340, 0, 147390, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    OP_64(0x2, 0x1)
    OP_A2(0x183B)
    EventEnd(0x0)
    SetMapFlags(0x2000000)

    label("loc_64C4")

    Return()

    # Function_17_6349 end

    def Function_18_64C5(): pass

    label("Function_18_64C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x3F9), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_64DB")
    Return()

    label("loc_64DB")

    SetMapFlags(0x80)
    OP_C2()
    OP_48()
    EventBegin(0x0)
    Fade(500)
    SetChrChipByIndex(0x101, 19)
    SetChrSubChip(0x101, 0)
    OP_0D()
    OP_20(0x5DC)
    OP_21()
    OP_22(0x11B, 0x0, 0x64)

    def lambda_6505():

        label("loc_6505")

        OP_99(0x101, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_6505")

    QueueWorkItem2(0x101, 2, lambda_6505)
    Sleep(15000)
    OP_44(0x101, 0x2)
    OP_1D(0x75)
    Fade(500)
    SetChrSubChip(0x101, 8)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65BB")

    ChrTalk(    #225
        0x101,
        (
            "#290F声音很好听呢，不过……\x01",
            "似乎有些难吹啊。\x02\x03",

            "#296F可是，真奇怪啊……\x02\x03",

            "这个声音……\x01",
            "总觉得以前在哪里听过。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    OP_A2(0x6)
    Jump("loc_660D")

    label("loc_65BB")


    ChrTalk(    #226
        0x101,
        (
            "#296F这声音……\x01",
            "以前在哪里听到过呢？\x02\x03",

            "就去那个地方吹吹看吧。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()

    label("loc_660D")

    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_18_64C5 end

    def Function_19_6615(): pass

    label("Function_19_6615")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6692"),
        (1, "loc_6698"),
        (SWITCH_DEFAULT, "loc_669E"),
    )


    label("loc_6692")

    OP_A2(0x1200)
    Jump("loc_669E")

    label("loc_6698")

    OP_A2(0x1201)
    Jump("loc_669E")

    label("loc_669E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_66AC")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_66B0")

    label("loc_66AC")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_66B0")

    Return()

    # Function_19_6615 end

    def Function_20_66B1(): pass

    label("Function_20_66B1")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_20_66B1 end

    def Function_21_6703(): pass

    label("Function_21_6703")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "休息\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_679F")
    OP_20(0xBB8)
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
    Sleep(3500)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_679F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_67B9")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_67B9")

    Return()

    # Function_21_6703 end

    SaveToFile()

Try(main)
