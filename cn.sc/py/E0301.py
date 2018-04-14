from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0301   ._SN',
        MapName             = 'Event',
        Location            = 'E0301.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60116",
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
        '提妲',                                 # 9
        '科洛丝',                               # 10
        '阿加特',                               # 11
        '雪拉扎德',                             # 12
        '金',                                   # 13
        '凯文',                                 # 14
        '拉赛尔博士',                           # 15
        '尤莉亚上尉',                           # 16
        '奈尔',                                 # 17
        '朵洛希',                               # 18
        '库莱泽',                               # 19
        '安东尼',                               # 20
        'lift',                                 # 21
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
        'ED6_DT07/CH00060 ._CH',             # 00
        'ED6_DT07/CH00040 ._CH',             # 01
        'ED6_DT07/CH00050 ._CH',             # 02
        'ED6_DT07/CH00020 ._CH',             # 03
        'ED6_DT07/CH00070 ._CH',             # 04
        'ED6_DT27/CH03080 ._CH',             # 05
        'ED6_DT07/CH02020 ._CH',             # 06
        'ED6_DT27/CH03580 ._CH',             # 07
        'ED6_DT07/CH02060 ._CH',             # 08
        'ED6_DT06/CH20063 ._CH',             # 09
        'ED6_DT06/CH20064 ._CH',             # 0A
        'ED6_DT07/CH01450 ._CH',             # 0B
        'ED6_DT07/CH01700 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH00060P._CP',             # 00
        'ED6_DT07/CH00040P._CP',             # 01
        'ED6_DT07/CH00050P._CP',             # 02
        'ED6_DT07/CH00020P._CP',             # 03
        'ED6_DT07/CH00070P._CP',             # 04
        'ED6_DT27/CH03080P._CP',             # 05
        'ED6_DT07/CH02020P._CP',             # 06
        'ED6_DT27/CH03580P._CP',             # 07
        'ED6_DT07/CH02060P._CP',             # 08
        'ED6_DT06/CH20063P._CP',             # 09
        'ED6_DT06/CH20064P._CP',             # 0A
        'ED6_DT07/CH01450P._CP',             # 0B
        'ED6_DT07/CH01700P._CP',             # 0C
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1540,
        Z                   = 3000,
        Y                   = 17550,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -20,
        Z                   = 2500,
        Y                   = 15640,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -2430,
        Z                   = 2500,
        Y                   = 12850,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -1830,
        Z                   = 1500,
        Y                   = -7470,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_2B2",          # 00, 0
        "Function_1_458",          # 01, 1
        "Function_2_519",          # 02, 2
        "Function_3_74E",          # 03, 3
        "Function_4_772",          # 04, 4
        "Function_5_FCB",          # 05, 5
        "Function_6_1313",         # 06, 6
        "Function_7_1CCD",         # 07, 7
        "Function_8_219B",         # 08, 8
        "Function_9_254C",         # 09, 9
        "Function_10_290C",        # 0A, 10
        "Function_11_2A2E",        # 0B, 11
        "Function_12_2D6E",        # 0C, 12
        "Function_13_2F3C",        # 0D, 13
        "Function_14_2F5D",        # 0E, 14
        "Function_15_2F70",        # 0F, 15
        "Function_16_2F83",        # 10, 16
        "Function_17_2F96",        # 11, 17
        "Function_18_340D",        # 12, 18
        "Function_19_3484",        # 13, 19
        "Function_20_34B4",        # 14, 20
        "Function_21_34E4",        # 15, 21
        "Function_22_3514",        # 16, 22
        "Function_23_354B",        # 17, 23
        "Function_24_357B",        # 18, 24
        "Function_25_35B2",        # 19, 25
        "Function_26_35E2",        # 1A, 26
        "Function_27_3612",        # 1B, 27
        "Function_28_3642",        # 1C, 28
        "Function_29_3807",        # 1D, 29
    )


    def Function_0_2B2(): pass

    label("Function_0_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_2E6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E3")
    SetChrPos(0xA, -60, 3000, 19860, 0)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x6, 0x2)

    label("loc_2E3")

    Jump("loc_3D6")

    label("loc_2E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_2FA")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_3D6")

    label("loc_2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_32E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_32B")
    SetChrPos(0x8, 3490, 1500, -6210, 90)
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x6, 0x2)

    label("loc_32B")

    Jump("loc_3D6")

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_399")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_35F")
    SetChrPos(0xB, -1920, 1500, -9370, 270)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x0, 0x6, 0x2)

    label("loc_35F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_396")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_379")
    SetChrFlags(0x9, 0x10)

    label("loc_379")

    SetChrPos(0x9, 2300, 2500, 14260, 90)
    ClearChrFlags(0x9, 0x80)
    OP_43(0x9, 0x0, 0x6, 0x2)

    label("loc_396")

    Jump("loc_3D6")

    label("loc_399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D6")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 10)
    SetChrSubChip(0x11, 0)
    SetChrPos(0xB, 3490, 1500, -6210, 90)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x0, 0x6, 0x2)

    label("loc_3D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_3EC")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 13)
    Jump("loc_457")

    label("loc_3EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_402")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 14)
    Jump("loc_457")

    label("loc_402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_418")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 15)
    Jump("loc_457")

    label("loc_418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_42E")
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 16)
    Jump("loc_457")

    label("loc_42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_444")
    OP_A3(0x10F4)
    SetMapFlags(0x10000000)
    Event(0, 17)
    Jump("loc_457")

    label("loc_444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_457")
    OP_A3(0x10F5)
    SetMapFlags(0x10000000)
    Event(0, 29)

    label("loc_457")

    Return()

    # Function_0_2B2 end

    def Function_1_458(): pass

    label("Function_1_458")

    OP_22(0x1C3, 0x0, 0x64)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_471")
    OP_22(0x75, 0x1, 0x5A)
    Jump("loc_482")

    label("loc_471")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_482")
    OP_22(0x125, 0x1, 0x50)

    label("loc_482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49C")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_49C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 4)), scpexpr(EXPR_END)), "loc_4AF")
    OP_B1("E0301_1")
    Jump("loc_518")

    label("loc_4AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_4C2")
    OP_B1("E0301_3")
    Jump("loc_518")

    label("loc_4C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_4D5")
    OP_B1("E0301_4")
    Jump("loc_518")

    label("loc_4D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_4E8")
    OP_B1("E0301_5")
    Jump("loc_518")

    label("loc_4E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_4FB")
    OP_B1("E0301_2")
    Jump("loc_518")

    label("loc_4FB")

    OP_B1("E0301_1")
    LoadEffect(0x0, "map\\\\mp032_00.eff")

    label("loc_518")

    Return()

    # Function_1_458 end

    def Function_2_519(): pass

    label("Function_2_519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74D")

    label("loc_531")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74D")
    OP_8F(0x11, 0xFFFFFFEC, 0x9C4, 0x3764, 0x7D0, 0x0)
    Sleep(500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_8F(0x11, 0x73A, 0x9C4, 0x3764, 0x7D0, 0x0)
    Sleep(500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_8F(0x11, 0x73A, 0x9C4, 0x3A5C, 0x7D0, 0x0)
    Sleep(500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_8F(0x11, 0xFFFFF8F8, 0x9C4, 0x3A5C, 0x7D0, 0x0)
    Sleep(500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_8F(0x11, 0xFFFFF8F8, 0x9C4, 0x3CDC, 0x7D0, 0x0)
    Sleep(500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_8F(0x11, 0xFFFFFFEC, 0x9C4, 0x3D18, 0x7D0, 0x0)
    Sleep(500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_531")

    label("loc_74D")

    Return()

    # Function_2_519 end

    def Function_3_74E(): pass

    label("Function_3_74E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_771")
    OP_8D(0xFE, -2580, -8230, -860, -6510, 1000)
    Jump("Function_3_74E")

    label("loc_771")

    Return()

    # Function_3_74E end

    def Function_4_772(): pass

    label("Function_4_772")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_FC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B27")

    ChrTalk(    #0
        0x10,
        (
            "#141F哟，这不是艾丝蒂尔吗。\x02\x03",

            "在龙出现之前\x01",
            "在这里闲逛？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1011F嗯，算是吧。\x01",
            "奈尔你们这么快就来采访了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "#140F不，一样是在\x01",
            "等待主角登场呢。\x02\x03",

            "暂时先照几张\x01",
            "『埃尔赛尤』吧。\x02\x03",

            "#147F……嘿嘿，话说回来\x01",
            "这次真是幸运啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1000F的确……\x01",
            "对通讯社来说可是一次很难得的机会呢。\x02\x03",

            "除了引起轰动的巨龙骚动事件之外，\x01",
            "同时还能采访到到新锐军舰的情报呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#141F光是龙和飞行舰队的对决\x01",
            "就已经是不得了的大新闻了。\x02\x03",

            "这次的随行采访，\x01",
            "几乎全部的通讯社\x01",
            "都挤破头了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1015F嗯～果然是这样啊。\x02\x03",

            "不过，居然会选中你们啊。\x01",
            "难不成是抽签抽中的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#142F笨蛋……那怎么可能。\x02\x03",

            "#145F我们会被指名采访，\x01",
            "似乎是因为过去的报道大受好评。\x02\x03",

            "在那次政变事件当中的实绩，\x01",
            "在这里发挥了很大的作用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#1004F哦～很厉害嘛。\x02\x03",

            "王国军的人们也\x01",
            "对你们评价很高嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "#141F只要写出好报道，\x01",
            "总有一天会得到认可的。\x02\x03",

            "嗯，就因为这样，\x01",
            "这次也麻烦你们提供情报啦。\x02\x03",

            "要是有什么轶闻插曲之类的，\x01",
            "刊登在版面上可是增色不少啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1001F啊哈哈……\x01",
            "嗯，明白了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A6F)
    Jump("loc_FC7")

    label("loc_B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D48")

    ChrTalk(    #10
        0x10,
        (
            "#140F对了，艾丝蒂尔。\x01",
            "你和那个尤莉亚上尉熟吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1015F虽然还不能说是\x01",
            "非常亲近……\x02\x03",

            "不过也还算是\x01",
            "有颇深的交往啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#141F那么你能不能\x01",
            "帮我介绍一下？\x02\x03",

            "制作那位女队长的特辑，\x01",
            "可是读者们的强烈要求哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#1004F尤、尤莉亚队长\x01",
            "那么有人气啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "#140F嗯嗯，和科洛蒂娅殿下\x01",
            "感觉上有得一拼哦。\x02\x03",

            "听说也有出版社\x01",
            "正在计划出写真集呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x101,
        "#1020F写、写真集～～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "#145F不过，这纯粹\x01",
            "是我们业界的传闻啦。\x02\x03",

            "那种企划就算制订出来\x01",
            "也得不到采访许可的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1013F……啊，那也是。\x01",
            "（不过还真想看看。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A70)
    Jump("loc_FC7")

    label("loc_D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F87")

    ChrTalk(    #18
        0x10,
        (
            "#141F尤莉亚上尉的采访请求……\x01",
            "到时候就麻烦你啦。\x02\x03",

            "毕竟亲卫队对平民来说\x01",
            "是个很有距离的组织嘛。\x02\x03",

            "我想透过对上尉的采访\x01",
            "报导出真实的情况来。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 6)), scpexpr(EXPR_END)), "loc_F84")

    ChrTalk(    #19
        0x101,
        (
            "#1007F嗯，关于这个……\x02\x03",

            "其实立刻\x01",
            "就被拒绝了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #20
        0x10,
        (
            "#143F啊？\x02\x03",

            "拒、拒绝了……这么快？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1016F啊哈哈～抱歉。\x02\x03",

            "好像有很多\x01",
            "不方便的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "#145F唉……是、是吗……\x02\x03",

            "可恶……\x01",
            "防卫心比想象中更坚固啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1007F呼，对不起。\x01",
            "完全没能帮上忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "#142F哪里，这也是没办法的。\x01",
            "对方也有自己的立场。\x02\x03",

            "不过，既然这样的话\x01",
            "就得考虑一下别的招数了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#1019F（嗯～还没死心啊。）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A2(0x1A74)

    label("loc_F84")

    Jump("loc_FC7")

    label("loc_F87")


    ChrTalk(    #26
        0x10,
        (
            "#145F透过熟人也不行吗……\x02\x03",

            "还以为会是个\x01",
            "对人情没辙的人……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FC7")

    TalkEnd(0xFE)
    Return()

    # Function_4_772 end

    def Function_5_FCB(): pass

    label("Function_5_FCB")

    TalkBegin(0xFE)
    SetChrChipByIndex(0x11, 9)
    SetChrSubChip(0x11, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_1305")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12AD")

    ChrTalk(    #27
        0x11,
        "#150F呀嗬～艾丝蒂尔！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1001F嗨～朵洛希。\x01",
            "自从王都之后都没见过呢。\x02\x03",

            "拍摄的情况如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x11,
        (
            "#150F哈哈哈，完全没问题哦！\x02\x03",

            "这孩子真是太可爱了，\x01",
            "从哪个角度拍都ＯＫ呢㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1011F这孩子……\x01",
            "啊，是说『埃尔赛尤』吗。\x02\x03",

            "#1016F真是的，朵洛希\x01",
            "还是那么我行我素啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x11,
        (
            "#151F嘿嘿，艾丝蒂尔才是。\x02\x03",

            "和平常一样有精神，\x01",
            "真是太好了㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#1008F啊哈哈……\x01",
            "不用客气。\x02\x03",

            "#1017F咦，莫非……\x02\x03",

            "朵洛希也在担心我吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x11,
        (
            "#150F嗯～那当然了。\x02\x03",

            "#156F那张约修亚的照片\x01",
            "可是我拍的哦！\x02\x03",

            "要是因为这个害小艾\x01",
            "心情沮丧，我会很难过的～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1003F是，是吗……\x01",
            "抱歉哦，朵洛希。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x11,
        (
            "#151F哪里，别在意。\x02\x03",

            "我是姐姐嘛，\x01",
            "鼓励小艾是应该的。\x02\x03",

            "如果还有什么其它的烦恼，\x01",
            "随时都可以来找我商量哦⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1016F啊、啊哈哈……\x01",
            "谢谢，我会记住的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A71)
    Jump("loc_1305")

    label("loc_12AD")


    ChrTalk(    #37
        0x11,
        (
            "#150F在龙出来之前\x01",
            "先来拍这孩子的表情～\x02\x03",

            "#151F然后假装拍摄舰内，\x01",
            "趁机来偷拍女队长。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1305")

    SetChrChipByIndex(0x11, 10)
    SetChrSubChip(0x11, 0)
    TalkEnd(0xFE)
    Return()

    # Function_5_FCB end

    def Function_6_1313(): pass

    label("Function_6_1313")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_1845")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "队伍编成\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_137B"),
        (1, "loc_1817"),
        (2, "loc_183F"),
        (SWITCH_DEFAULT, "loc_1842"),
    )


    label("loc_137B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_1814")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17BD")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B4")

    ChrTalk(    #38
        0xFE,
        "#020F哎呀，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13CD")

    label("loc_13B4")


    ChrTalk(    #39
        0xFE,
        "#020F哎呀，是你们。\x02",
    )

    CloseMessageWindow()

    label("loc_13CD")


    ChrTalk(    #40
        0x101,
        (
            "#1011F啊，雪拉姐。\x01",
            "你在这里啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        "#1040F在想什么呢？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #42
        0xFE,
        (
            "#524F嗯嗯，这个啊……\x02\x03",

            "看着翡翠之塔，\x01",
            "就会想起很多事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1008F听你这么一说……\x01",
            "确实是一言难尽呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#1041F哈哈，是啊……\x02\x03",

            "不管怎么说\x01",
            "这里是我们首次执行任务的地方嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14F1")

    ChrTalk(    #45
        0x107,
        "#560F哇……是这样啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1564")

    label("loc_14F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1515")

    ChrTalk(    #46
        0x105,
        "#040F哎呀……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1564")

    label("loc_1515")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1545")

    ChrTalk(    #47
        0x106,
        "#051F这可是头一回听说啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1564")

    label("loc_1545")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1564")

    ChrTalk(    #48
        0x108,
        "#070F哦……\x02",
    )

    CloseMessageWindow()

    label("loc_1564")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #49
        0xFE,
        (
            "#021F呵呵，是刚刚成为\x01",
            "准游击士的时候吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#1015F嗯，附近的孩子\x01",
            "闯进塔里迷了路……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x102,
        (
            "#1035F所以我们就\x01",
            "前来救援了。\x02\x03",

            "#1048F不过，最后的风头\x01",
            "倒是都被父亲抢走了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_165E")

    ChrTalk(    #52
        0x108,
        (
            "#071F哈哈，果然是这样吗。\x02\x03",

            "完全像是大人的做法呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_173C")

    label("loc_165E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16A4")

    ChrTalk(    #53
        0x106,
        (
            "#051F哈哈，果然是这样吗。\x02\x03",

            "大叔也真像个小孩子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_173C")

    label("loc_16A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16F7")

    ChrTalk(    #54
        0x105,
        (
            "#045F啊，果然是这样吗。\x02\x03",

            "嘻嘻……\x01",
            "很像是卡西乌斯叔叔的风格。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_173C")

    label("loc_16F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_173C")

    ChrTalk(    #55
        0x107,
        (
            "#067F啊，果然是这样啊。\x02\x03",

            "嘿嘿，很像是叔叔的风格。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_173C")


    ChrTalk(    #56
        0xFE,
        (
            "#020F嗯，比起那时候，\x01",
            "你们两人确实都成长了不少。\x02\x03",

            "这次要好好靠自己的力量\x01",
            "坚持到最后哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#1006F嗯！　包在我身上。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1E27)
    Jump("loc_1814")

    label("loc_17BD")


    ChrTalk(    #58
        0xFE,
        (
            "#020F没想到会以这样的形式\x01",
            "回到翡翠之塔呢。\x02\x03",

            "我也会做好准备的。\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1814")

    Jump("loc_1842")

    label("loc_1817")


    ChrTalk(    #59
        0xB,
        "#020F哎呀？要更换成员了吗？\x02",
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_1842")

    label("loc_183F")

    Jump("loc_1842")

    label("loc_1842")

    Jump("loc_1CC9")

    label("loc_1845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_1CC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C47")

    ChrTalk(    #60
        0x101,
        (
            "#1011F啊，雪拉姐。\x01",
            "你在这里啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xB,
        "#020F哎呀，艾丝蒂尔在散步？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1000F嗯，差不多吧。\x02\x03",

            "你是出来吹吹风的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xB,
        (
            "#021F嗯嗯，天气正好，\x01",
            "我也顺便放松一下。\x02\x03",

            "休养生息以备随时出动，\x01",
            "也是我们游击士的工作哦。\x02\x03",

            "特别是像这次一样的\x01",
            "空闲时间就更不能白白浪费了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1002F嗯，我明白的，\x01",
            "不过……\x02\x03",

            "雪拉姐觉得此次的作战\x01",
            "会失败吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xB,
        (
            "#020F这个嘛，该怎么说呢……\x02\x03",

            "嗯，从常识上考虑的话，\x01",
            "成功的可能性比较高。\x02\x03",

            "毕竟昂贵的警备艇\x01",
            "也出动了１２艘之多嘛。\x02\x03",

            "任凭古代龙多么厉害，\x01",
            "我想也难以逃脱才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1015F嗯……是啊。\x02\x03",

            "这次摩尔根将军也\x01",
            "胜券在握的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xB,
        (
            "#027F不过，这单纯\x01",
            "只是表面上的样子。\x02\x03",

            "对于让游击士同行这件事，\x01",
            "原本会有不少反对的声音。\x02\x03",

            "但将军却抛开这些意见\x01",
            "而允许我们一起同行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#1002F……代表摩尔根将军\x01",
            "心中也有所不安吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xB,
        (
            "#020F会这么想也很合理吧。\x02\x03",

            "#525F嗯，正因为这样，\x01",
            "现在才要放松一下嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1007F呼，原来如此。\x02\x03",

            "那我也\x01",
            "继续散步吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xB,
        (
            "#021F呵呵，就这么办吧。\x02\x03",

            "毕竟搭乘王家飞船的机会\x01",
            "可是很难得的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#1006F嗯……说得也是。\x02\x03",

            "那我走了，雪拉姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xB,
        "#020F嗯嗯，待会儿见。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A1F)
    Jump("loc_1CC9")

    label("loc_1C47")


    ChrTalk(    #74
        0xB,
        (
            "#020F既然让我们同行，\x01",
            "说明将军也有所不安哦。\x02\x03",

            "为了随时随地可以出动，\x01",
            "必须事先做好准备才行。\x02\x03",

            "不过，在那之前\x01",
            "就先尽情放松吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC9")

    TalkEnd(0xFE)
    Return()

    # Function_6_1313 end

    def Function_7_1CCD(): pass

    label("Function_7_1CCD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_2197")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "队伍编成\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D35"),
        (1, "loc_2174"),
        (2, "loc_2194"),
        (SWITCH_DEFAULT, "loc_2197"),
    )


    label("loc_1D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_2171")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F5")
    OP_4A(0xA, 255)

    ChrTalk(    #75
        0xA,
        (
            "#552F下一个执行者是那个小鬼吗。\x02\x03",

            "是在王都让我们\x01",
            "吃尽苦头的对手啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#1002F嗯……\x02\x03",

            "那个巨大的人形兵器……\x01",
            "这次也会出来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x102,
        (
            "#1043F要看他们的战术而定，\x01",
            "目前来说很难判断……\x02\x03",

            "#1043F但即使对手只有玲一个人\x01",
            "必定也将会是一场严峻的战斗。\x02\x03",

            "#1035F如果是面对面作战的话，\x01",
            "她的实力应该在我之上。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_1E8D():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1E8D)
    Sleep(120)

    def lambda_1EA0():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1EA0)
    TurnDirection(0x101, 0x102, 400)
    Sleep(600)

    ChrTalk(    #78
        0x101,
        (
            "#1020F约、约修亚之上……！？\x02\x03",

            "别，别开玩笑啦。\x01",
            "再加上那样的人形兵器的话…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x102,
        (
            "#1035F和以隐密行动为主的我不同，\x01",
            "玲可以说是万能型的执行者。\x02\x03",

            "当然也拥有着能够\x01",
            "独力排除敌人的战斗力。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FAB")

    ChrTalk(    #80
        0x108,
        "#072F唔，看来下一个也不能大意啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2031")

    label("loc_1FAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FD9")

    ChrTalk(    #81
        0x103,
        "#022F原来如此，说得对。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2031")

    label("loc_1FD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_200A")

    ChrTalk(    #82
        0x109,
        "#1064F呵～不愧是执行者啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2031")

    label("loc_200A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2031")

    ChrTalk(    #83
        0x107,
        "#065F怎、怎么会……\x02",
    )

    CloseMessageWindow()

    label("loc_2031")


    ChrTalk(    #84
        0xA,
        (
            "#051F哼，求之不得啊。\x02\x03",

            "我可要好好地\x01",
            "教导一下那个小鬼来作为回礼。\x02\x03",

            "我随时都可以帮忙……\x01",
            "需要的话就说一声吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #85
        0x101,
        (
            "#1006F嗯，谢谢。\x01",
            "那就拜托了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x102,
        (
            "#1040F到时\x01",
            "就请多多关照了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E46)
    Jump("loc_2171")

    label("loc_20F5")


    ChrTalk(    #87
        0xA,
        (
            "#053F下一个对手是那个小鬼吗……\x02\x03",

            "#051F我可要好好地\x01",
            "教导一下那个小鬼来作为回礼。\x02\x03",

            "需要我的力量的话，\x01",
            "随时来找我就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2171")

    Jump("loc_2197")

    label("loc_2174")


    ChrTalk(    #88
        0xA,
        "#050F要更换成员了？\x02",
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_2197")

    label("loc_2194")

    Jump("loc_2197")

    label("loc_2197")

    TalkEnd(0xFE)
    Return()

    # Function_7_1CCD end

    def Function_8_219B(): pass

    label("Function_8_219B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_2548")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_246E")
    OP_4A(0x9, 255)

    ChrTalk(    #89
        0x9,
        "#047F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        "#1026F科洛丝……怎么了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2240")

    ChrTalk(    #91
        0x9,
        (
            "#043F啊，艾丝蒂尔……\x02\x03",

            "#047F没什么，在想些事情……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2274")

    label("loc_2240")


    ChrTalk(    #92
        0x9,
        (
            "#043F啊，大家……\x02\x03",

            "#047F没什么，在想些事情……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2274")


    ChrTalk(    #93
        0x101,
        (
            "#1003F……是吗。\x02\x03",

            "嗯……\x01",
            "果然还是会烦恼呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #94
        0x9,
        "#043F……对不起，在这种时候。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#1000F哪里的话，你不用介意啦。\x02\x03",

            "而且之前还是我\x01",
            "害得大家一直在担心呢。\x02\x03",

            "#1007F不过，我倒觉得一切\x01",
            "都是某人的错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x102,
        "#1048F……是是，我会反省。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x9,
        "#048F呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#1008F所以，科洛丝\x01",
            "完全没必要在意这些。\x02\x03",

            "困难的时候要互相帮助嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x9,
        (
            "#040F谢谢你，艾丝蒂尔。\x02\x03",

            "不过，如果需要我的话\x01",
            "请马上跟我说哦。\x02\x03",

            "虽然力量微薄，\x01",
            "但也请让我帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#1006F嗯，当然。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x102,
        "#1040F到时要麻烦你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        "#041F好！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    OP_A2(0x1E26)
    Jump("loc_2548")

    label("loc_246E")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "队伍编成\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_24CC"),
        (1, "loc_251A"),
        (2, "loc_2545"),
        (SWITCH_DEFAULT, "loc_2548"),
    )


    label("loc_24CC")


    ChrTalk(    #103
        0x9,
        (
            "#040F需要我的力量的话，\x01",
            "请随时跟我说哦。\x02\x03",

            "那么，请各位\x01",
            "一定要小心……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2548")

    label("loc_251A")


    ChrTalk(    #104
        0x9,
        (
            "#040F明白了。\x01",
            "要更换成员是吧。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_2548")

    label("loc_2545")

    Jump("loc_2548")

    label("loc_2548")

    TalkEnd(0xFE)
    Return()

    # Function_8_219B end

    def Function_9_254C(): pass

    label("Function_9_254C")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "队伍编成\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_25AD"),
        (1, "loc_28E5"),
        (2, "loc_2905"),
        (SWITCH_DEFAULT, "loc_2908"),
    )


    label("loc_25AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2897")

    ChrTalk(    #105
        0x8,
        "#060F啊，姐姐，是你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        (
            "#1011F咦，提妲……\x01",
            "你怎么在甲板上？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #107
        0x8,
        (
            "#063F嗯、嗯，我听说\x01",
            "蔡斯被袭击了……\x02\x03",

            "不知道在城里的人们……\x01",
            "是否平安呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#1003F是、是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        (
            "#1040F没问题，别担心啦。\x02\x03",

            "蔡斯离雷斯顿要塞很近，\x01",
            "守备队的战力也很充足。\x02\x03",

            "而且协会里\x01",
            "也有雾香在。\x02\x03",

            "万一有事\x01",
            "她应该会想办法的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#1015F嗯，的确……\x02\x03",

            "一想到有雾香小姐在\x01",
            "感觉就安心许多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "#560F嘿嘿，是吧……\x02\x03",

            "#067F嗯，一下子\x01",
            "就感觉放松多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        (
            "#1040F我们如果能压制住塔\x01",
            "城里的敌人应该也会撤退的。\x02\x03",

            "毕竟城镇里发生的那些异变，\x01",
            "应该都是配合塔的佯攻才对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1002F这么说来，可不能\x01",
            "再磨磨蹭蹭了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x108,
        (
            "#070F嗯，就是这样。\x01",
            "马上过去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x102,
        (
            "#1040F嗯嗯，是啊……\x02\x03",

            "那么，提妲，我们先走了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        (
            "#060F啊，嗯……\x02\x03",

            "哥哥你们也\x01",
            "要多加小心。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E42)
    Jump("loc_28E2")

    label("loc_2897")


    ChrTalk(    #117
        0x8,
        (
            "#060F我就待在这里，\x01",
            "有需要帮忙的话尽管说。\x02\x03",

            "那么……\x01",
            "大家都要当心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28E2")

    Jump("loc_2908")

    label("loc_28E5")


    ChrTalk(    #118
        0x8,
        "#060F要更换成员吗？\x02",
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_2908")

    label("loc_2905")

    Jump("loc_2908")

    label("loc_2908")

    TalkEnd(0xFE)
    Return()

    # Function_9_254C end

    def Function_10_290C(): pass

    label("Function_10_290C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29CA")

    ChrTalk(    #119
        0xFE,
        "啊，是各位游击士啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "我研究上遇到一些困难。\x01",
            "试着来转换一下心情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "话说那个塔的异样情况\x01",
            "到底是怎么回事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "真担心在卢安的弟弟。\x01",
            "城镇能平安无事就好了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2A2A")

    label("loc_29CA")


    ChrTalk(    #123
        0xFE,
        (
            "话说那个塔的异样情况\x01",
            "到底是怎么回事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "真担心在卢安的弟弟。\x01",
            "城镇能平安无事就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A2A")

    TalkEnd(0xFE)
    Return()

    # Function_10_290C end

    def Function_11_2A2E(): pass

    label("Function_11_2A2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 6)), scpexpr(EXPR_END)), "loc_2A8A")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #125
        0xFE,
        "呼啊～～喵呼。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A87")

    ChrTalk(    #126
        0x105,
        (
            "#040F看来好像在这里\x01",
            "晒太阳的样子。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A87")

    Jump("loc_2D6A")

    label("loc_2A8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD3")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #127
        0xFE,
        "喵～～～\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #128
        0x101,
        "#1004F啊，安东尼！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B31")

    ChrTalk(    #129
        0x107,
        (
            "#067F嘿嘿嘿……\x01",
            "很吃惊吧？\x02\x03",

            "不管怎么看\x01",
            "都像是雷伊哥哥带来的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B5A")

    label("loc_2B31")


    ChrTalk(    #130
        0x102,
        (
            "#1044F是中央工房的人\x01",
            "带来的吗……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B5A")

    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #131
        0xFE,
        "喵噢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1011F嗯～为什么会在\x01",
            "这种紧张的场合下再次见面呢。\x02\x03",

            "#1000F嗯，不管怎么说\x01",
            "这阵子还请多关照了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E4C)
    Jump("loc_2BF8")

    label("loc_2BD3")


    ChrTalk(    #133
        0x101,
        (
            "#1001F安东尼，\x01",
            "你在这里做什么？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BF8")

    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #134
        0xFE,
        "喵噢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "喵呜喵呜喵呜喵呜咪！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x102,
        (
            "#1041F哈哈，好像\x01",
            "在说什么似的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D49")

    ChrTalk(    #137
        0x105,
        (
            "#044F……看起来好像\x01",
            "想交给我们什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "喵嗄！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x105,
        (
            "#041F啊……\x01",
            "这本书要给我吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #140
        "\x07\x00得到了\x1F\x43\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x243, 1)
    OP_A2(0x10BE)

    ChrTalk(    #141
        0x105,
        "#048F呵呵，谢谢你了。\x02",
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #142
        0xFE,
        "咕喵～咕。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        "#1016F真、真不简单……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D6A")

    label("loc_2D49")


    ChrTalk(    #144
        0x101,
        (
            "#1016F有人懂\x01",
            "动物的语言吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D6A")

    TalkEnd(0xFE)
    Return()

    # Function_11_2A2E end

    def Function_12_2D6E(): pass

    label("Function_12_2D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_2DBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_2D9C")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    Jump("loc_2DB7")

    label("loc_2D9C")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)

    label("loc_2DB7")

    Jump("loc_2E38")

    label("loc_2DBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_2DDD")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    Jump("loc_2E38")

    label("loc_2DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_2DFE")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0x2, 0xFF, 0x5, 0x6, 0x4, 0x8, 0x7, 0xFFFF)
    Jump("loc_2E38")

    label("loc_2DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_2E1F")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0x7, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x8, 0xFFFF)
    Jump("loc_2E38")

    label("loc_2E1F")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)

    label("loc_2E38")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_2E6E")
    Jump("loc_2F3B")

    label("loc_2E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_2EA2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E9F")
    SetChrPos(0xA, -60, 3000, 19860, 0)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x6, 0x2)

    label("loc_2E9F")

    Jump("loc_2F3B")

    label("loc_2EA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_2EAC")
    Jump("loc_2F3B")

    label("loc_2EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_2EE0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2EDD")
    SetChrPos(0x8, 3490, 1500, -6210, 90)
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x6, 0x2)

    label("loc_2EDD")

    Jump("loc_2F3B")

    label("loc_2EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_2F3B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F11")
    SetChrPos(0xB, -1920, 1500, -9370, 270)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x0, 0x6, 0x2)

    label("loc_2F11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2F3B")
    SetChrPos(0x9, 2300, 2500, 14260, 90)
    ClearChrFlags(0x9, 0x80)
    OP_43(0x9, 0x0, 0x6, 0x2)

    label("loc_2F3B")

    Return()

    # Function_12_2D6E end

    def Function_13_2F3C(): pass

    label("Function_13_2F3C")

    EventBegin(0x0)
    Call(0, 28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F50")
    OP_A2(0x10F0)
    Jump("loc_2F53")

    label("loc_2F50")

    OP_A2(0x10F1)

    label("loc_2F53")

    NewScene("ED6_DT21/R0303   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_2F3C end

    def Function_14_2F5D(): pass

    label("Function_14_2F5D")

    EventBegin(0x0)
    Call(0, 28)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R3104   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2F5D end

    def Function_15_2F70(): pass

    label("Function_15_2F70")

    EventBegin(0x0)
    Call(0, 28)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R2401   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_2F70 end

    def Function_16_2F83(): pass

    label("Function_16_2F83")

    EventBegin(0x0)
    Call(0, 28)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R1402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_2F83 end

    def Function_17_2F96(): pass

    label("Function_17_2F96")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(70, 2500, 10950, 0)
    OP_67(0, 8380, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(414, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    OP_73(0x1)
    Sleep(500)

    def lambda_300F():
        OP_6D(600, 2500, 15570, 6500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_300F)

    def lambda_3027():
        OP_67(0, 6000, -10000, 6500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3027)

    def lambda_303F():
        OP_6E(262, 6500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_303F)
    OP_43(0x101, 0x1, 0x0, 0x12)
    OP_43(0x102, 0x1, 0x0, 0x13)
    OP_43(0xB, 0x1, 0x0, 0x14)
    OP_43(0xA, 0x1, 0x0, 0x15)
    OP_43(0x8, 0x1, 0x0, 0x16)
    OP_43(0xC, 0x1, 0x0, 0x17)
    OP_43(0xD, 0x1, 0x0, 0x18)
    OP_43(0x9, 0x1, 0x0, 0x19)
    OP_43(0xF, 0x1, 0x0, 0x1A)
    OP_43(0xE, 0x1, 0x0, 0x1B)
    WaitChrThread(0x102, 0x2)

    ChrTalk(    #145
        0x101,
        "#1000F哪、哪里……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x102,
        (
            "#1030F从前方甲板\x01",
            "看得最清楚的方向……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_8C(0xD, 270, 400)
    Sleep(500)

    ChrTalk(    #147
        0xD,
        "#1060F……就是那个！\x02",
    )

    CloseMessageWindow()

    def lambda_3123():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3123)

    def lambda_3131():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3131)
    Sleep(50)

    def lambda_3144():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3144)

    def lambda_3152():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3152)
    Sleep(40)

    def lambda_3165():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3165)

    def lambda_3173():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3173)
    Sleep(50)

    def lambda_3186():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3186)

    def lambda_3194():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3194)
    Sleep(40)

    def lambda_31A7():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_31A7)

    def lambda_31B5():
        OP_6D(-1820, 2500, 15470, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_31B5)

    def lambda_31CD():
        OP_6C(340000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_31CD)
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x2)
    OP_44(0x101, 0x3)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #148
        "\x07\x00◆浮游都市出现的过场动画\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_77(0xFF, 0xFF, 0x80, 0x0, 0x0)
    OP_6D(600, 2500, 15570, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6E(262, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #149
        0x101,
        "#1000F什、什、什……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x9,
        (
            "#040F难不成那就是……\x01",
            "……那座巨大的都市是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x102,
        "#1030F嗯……不会错的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xD,
        (
            "#1060F『辉之环』……\x01",
            "是辉之环啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xE,
        "#100F──糟糕。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 400)
    Sleep(600)

    ChrTalk(    #154
        0xE,
        (
            "#100F尤莉亚上尉！\x01",
            "赶快让军舰降落！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xF,
        "#170F……咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xE,
        (
            "#100F卡西乌斯不是下达过\x01",
            "紧急指令吗！\x02\x03",

            "再不快点的话就来不及了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xF,
        "#170F！！！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #158
        "\x07\x00◆浮游都市波浪扩散导力停止的过场动画\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/C5408   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_2F96 end

    def Function_18_340D(): pass

    label("Function_18_340D")

    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFFDDA, 0xBB8, 0x4588, 0xFA0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_18_340D end

    def Function_19_3484(): pass

    label("Function_19_3484")

    Sleep(500)
    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x23A, 0xBB8, 0x4394, 0xFA0, 0x0)
    Return()

    # Function_19_3484 end

    def Function_20_34B4(): pass

    label("Function_20_34B4")

    Sleep(1000)
    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x3C0, 0xBB8, 0x401A, 0xFA0, 0x0)
    Return()

    # Function_20_34B4 end

    def Function_21_34E4(): pass

    label("Function_21_34E4")

    Sleep(1500)
    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFF8D0, 0xBB8, 0x4114, 0xFA0, 0x0)
    Return()

    # Function_21_34E4 end

    def Function_22_3514(): pass

    label("Function_22_3514")

    Sleep(2000)
    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4EC, 0x9C4, 0x39F8, 0xFA0, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_22_3514 end

    def Function_23_354B(): pass

    label("Function_23_354B")

    Sleep(2500)
    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFFEA2, 0x9C4, 0x3C3C, 0xFA0, 0x0)
    Return()

    # Function_23_354B end

    def Function_24_357B(): pass

    label("Function_24_357B")

    Sleep(3000)
    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFF830, 0x9C4, 0x384A, 0xFA0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_24_357B end

    def Function_25_35B2(): pass

    label("Function_25_35B2")

    Sleep(3500)
    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFFBB4, 0x9C4, 0x3462, 0xFA0, 0x0)
    Return()

    # Function_25_35B2 end

    def Function_26_35E2(): pass

    label("Function_26_35E2")

    Sleep(4000)
    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x3A2, 0x9C4, 0x2F8A, 0xFA0, 0x0)
    Return()

    # Function_26_35E2 end

    def Function_27_3612(): pass

    label("Function_27_3612")

    Sleep(4500)
    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFFF74, 0x9C4, 0x30D4, 0xFA0, 0x0)
    Return()

    # Function_27_3612 end

    def Function_28_3642(): pass

    label("Function_28_3642")

    OP_6D(-1900, -9600, -11180, 0)
    OP_67(0, 3300, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_6D(-550, -9330, -8150, 0)
    OP_67(0, 3370, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(48000, 0)
    OP_6E(262, 0)
    OP_72(0x4, 0x4)
    OP_A1(0x14, 0x4)
    SetChrPos(0x14, 0, -7600, -7600, 0)
    SetChrPos(0x101, -550, -7600, -8150, 270)
    SetChrPos(0x102, 550, -7600, -8150, 270)
    SetChrPos(0xF8, -550, -7600, -7050, 270)
    SetChrPos(0xF9, 550, -7600, -7050, 270)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0xF8, 0x20)
    SetChrFlags(0xF9, 0x20)

    def lambda_3749():
        OP_67(0, 4700, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3749)

    def lambda_3761():
        OP_91(0xFE, 0x0, 0xFFFFB1E0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3761)

    def lambda_377C():
        OP_91(0xFE, 0x0, 0xFFFFB1E0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_377C)

    def lambda_3797():
        OP_91(0xFE, 0x0, 0xFFFFB1E0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3797)

    def lambda_37B2():
        OP_91(0xFE, 0x0, 0xFFFFB1E0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_37B2)

    def lambda_37CD():
        OP_91(0xFE, 0x0, 0xFFFFB1E0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_37CD)
    ClearMapFlags(0x100000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    Return()

    # Function_28_3642 end

    def Function_29_3807(): pass

    label("Function_29_3807")

    EventBegin(0x0)
    OP_67(0, 4700, -10000, 0)
    OP_6D(-550, -9330, -8150, 0)
    OP_67(0, 3370, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(48000, 0)
    OP_6E(262, 0)
    OP_72(0x4, 0x4)
    OP_A1(0x14, 0x4)
    SetChrPos(0x14, 0, -17600, -7600, 0)
    SetChrPos(0x101, -550, -17600, -8150, 270)
    SetChrPos(0x102, 550, -17600, -8150, 270)
    SetChrPos(0xF8, -550, -17600, -7050, 270)
    SetChrPos(0xF9, 550, -17600, -7050, 270)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0xF8, 0x20)
    SetChrFlags(0xF9, 0x20)

    def lambda_38E4():
        OP_6D(-550, -9330, -8150, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_38E4)

    def lambda_38FC():
        OP_91(0xFE, 0x0, 0x4E20, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_38FC)

    def lambda_3917():
        OP_91(0xFE, 0x0, 0x4E20, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3917)

    def lambda_3932():
        OP_91(0xFE, 0x0, 0x4E20, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3932)

    def lambda_394D():
        OP_91(0xFE, 0x0, 0x4E20, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_394D)

    def lambda_3968():
        OP_91(0xFE, 0x0, 0x4E20, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3968)
    SetMapFlags(0x100000)
    OP_22(0x68, 0x0, 0x64)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    OP_23(0x1C3)
    OP_23(0x75)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0313   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_3807 end

    SaveToFile()

Try(main)
