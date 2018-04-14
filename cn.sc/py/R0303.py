from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R0303   ._SN',
        MapName             = 'Rolent',
        Location            = 'R0303.x',
        MapIndex            = 21,
        MapDefaultBGM       = "ed60022",
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
        '雷震狂鱼',                             # 9
        '士兵海恩茨',                           # 10
        '矿工兰古',                             # 11
        '阿加特',                               # 12
        '目标用照相机',                         # 13
        '玛鲁加山道方向',                       # 14
        '玛鲁加山道方向',                       # 15
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01500 ._CH',             # 01
        'ED6_DT06/CH20053 ._CH',             # 02
        'ED6_DT09/CH10900 ._CH',             # 03
        'ED6_DT09/CH10901 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01500P._CP',             # 01
        'ED6_DT06/CH20053P._CP',             # 02
        'ED6_DT09/CH10900P._CP',             # 03
        'ED6_DT09/CH10901P._CP',             # 04
    )

    DeclNpc(
        X                   = -420,
        Z                   = -20,
        Y                   = -34790,
        Direction           = 180,
        Unknown2            = 3,
        Unknown3            = 196608,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -166100,
        Z                   = 100,
        Y                   = 127500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -166100,
        Z                   = 100,
        Y                   = 127500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
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
        X                   = -167010,
        Z                   = -70,
        Y                   = 78790,
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

    DeclNpc(
        X                   = -2070,
        Z                   = -120,
        Y                   = -72730,
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


    DeclEvent(
        X                   = -4700,
        Y                   = -2000,
        Z                   = -62600,
        Range               = 1200,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFF0E98,
        Unknown_18          = 0x0,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = -15720,
        Y                   = -2000,
        Z                   = -24750,
        Range               = 13360,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFFB08C,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = -2500,
        Y                   = -6100,
        Z                   = -8670,
        Range               = 2500,
        Unknown_10          = 0x2710,
        Unknown_14          = 0xFFFFF254,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )

    DeclEvent(
        X                   = -168250,
        Y                   = -1000,
        Z                   = 128800,
        Range               = -164500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x1F2E8,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = -420,
        Y                   = -1000,
        Z                   = -34790,
        Range               = 2000,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 7,
    )


    DeclActor(
        TriggerX            = -13840,
        TriggerZ            = -130,
        TriggerY            = -13720,
        TriggerRange        = 1000,
        ActorX              = -13620,
        ActorZ              = -140,
        ActorY              = -12960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_276",          # 00, 0
        "Function_1_3C6",          # 01, 1
        "Function_2_59D",          # 02, 2
        "Function_3_5B3",          # 03, 3
        "Function_4_5BE",          # 04, 4
        "Function_5_A14",          # 05, 5
        "Function_6_A1F",          # 06, 6
        "Function_7_B35",          # 07, 7
        "Function_8_CF0",          # 08, 8
        "Function_9_E07",          # 09, 9
        "Function_10_143B",        # 0A, 10
        "Function_11_150A",        # 0B, 11
        "Function_12_159F",        # 0C, 12
        "Function_13_1B3E",        # 0D, 13
        "Function_14_1C29",        # 0E, 14
        "Function_15_1CB0",        # 0F, 15
        "Function_16_1D3F",        # 10, 16
        "Function_17_1E22",        # 11, 17
        "Function_18_1EA7",        # 12, 18
        "Function_19_1F2C",        # 13, 19
        "Function_20_1FB1",        # 14, 20
        "Function_21_2036",        # 15, 21
        "Function_22_21C2",        # 16, 22
        "Function_23_2228",        # 17, 23
        "Function_24_228E",        # 18, 24
        "Function_25_22F4",        # 19, 25
    )


    def Function_0_276(): pass

    label("Function_0_276")

    OP_A3(0x1970)
    OP_A3(0x1971)
    OP_A3(0x1972)
    OP_A3(0x1973)
    OP_A3(0x1974)
    OP_A3(0x1975)
    OP_A3(0x1976)
    OP_A3(0x1977)
    OP_A3(0x1978)
    OP_A3(0x1979)
    OP_A3(0x197A)
    OP_A3(0x197B)
    OP_A3(0x197C)
    OP_A3(0x1FC0)
    OP_A3(0x1FC1)
    OP_A3(0x1FC2)
    OP_A3(0x1FC3)
    OP_A3(0x1FC4)
    OP_A3(0x1FC5)
    OP_A3(0x1FC6)
    OP_A3(0x1FC7)
    OP_A3(0x1FC8)
    OP_A3(0x1FC9)
    OP_A3(0x1FCA)
    OP_A3(0x1FCB)
    OP_A3(0x1FCC)
    OP_A3(0x1FCD)
    OP_A3(0x1FCE)
    OP_A3(0x1FCF)
    OP_A3(0x1FD0)
    OP_A3(0x1FD1)
    OP_A3(0x1FD2)
    OP_A3(0x1FD3)
    OP_A3(0x1FD4)
    OP_A3(0x1FD5)
    OP_A3(0x1FD6)
    OP_A3(0x1FD7)
    OP_A3(0x1FD8)
    OP_A3(0x1FD9)
    OP_A3(0x1FDA)
    OP_A3(0x1FDB)
    OP_A3(0x1FDC)
    OP_A3(0x1FDD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_319")
    SetChrPos(0x9, -2440, 30, -23500, 180)
    ClearChrFlags(0x9, 0x80)

    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_349")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_330")
    SetChrFlags(0xA, 0x80)
    Jump("loc_346")

    label("loc_330")

    SetChrPos(0xA, -168160, -10, 126410, 90)
    ClearChrFlags(0xA, 0x80)

    label("loc_346")

    Jump("loc_389")

    label("loc_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_353")
    Jump("loc_389")

    label("loc_353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_362")
    SetChrFlags(0xA, 0x80)
    Jump("loc_389")

    label("loc_362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_END)), "loc_382")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, -163860, 40, 125420, 315)
    Jump("loc_389")

    label("loc_382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_389")

    label("loc_389")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_39F")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 9)
    Jump("loc_3C5")

    label("loc_39F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_3B5")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 11)
    Jump("loc_3C5")

    label("loc_3B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C5")
    Event(0, 21)

    label("loc_3C5")

    Return()

    # Function_0_276 end

    def Function_1_3C6(): pass

    label("Function_1_3C6")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3E6"),
        (101, "loc_3E6"),
        (105, "loc_3E6"),
        (102, "loc_412"),
        (103, "loc_412"),
        (104, "loc_412"),
        (SWITCH_DEFAULT, "loc_43E"),
    )


    label("loc_3E6")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFD7790, 0x230011)
    ClearChrFlags(0xD, 0x4)
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x2F8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43E")

    label("loc_412")

    OP_16(0x2, 0xFA0, 0xFFFB8390, 0xFFFFBD98, 0x23006A)
    ClearChrFlags(0xE, 0x4)
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x31A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x81), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43E")

    label("loc_43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_458")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_END)), "loc_468")
    OP_10(0x3, 0x0)
    OP_10(0x4, 0x1)
    Jump("loc_46E")

    label("loc_468")

    OP_10(0x3, 0x1)
    OP_10(0x4, 0x0)

    label("loc_46E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_48C")
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x4, 0x80)
    Jump("loc_49E")

    label("loc_48C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49E")
    ClearChrFlags(0x8, 0x80)
    OP_B2(0x1, 0x4, 0x80)

    label("loc_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x326, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B0")
    OP_6F(0x0, 0)
    Jump("loc_4B7")

    label("loc_4B0")

    OP_6F(0x0, 60)

    label("loc_4B7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_512")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_4E8")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    OP_C4(0x0, 0x4)
    Jump("loc_512")

    label("loc_4E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_512")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)

    label("loc_512")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_521")
    Jump("loc_571")

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_571")
    LoadEffect(0x0, "map\\\\mp086_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 6000, -8130, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_57D")
    OP_B2(0x0, 0x3, 0x80)

    label("loc_57D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_596")
    OP_10(0x1, 0x0)
    OP_10(0x5, 0x1)
    Jump("loc_59C")

    label("loc_596")

    OP_10(0x1, 0x1)
    OP_10(0x5, 0x0)

    label("loc_59C")

    Return()

    # Function_1_3C6 end

    def Function_2_59D(): pass

    label("Function_2_59D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5B2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_59D")

    label("loc_5B2")

    Return()

    # Function_2_59D end

    def Function_3_5B3(): pass

    label("Function_3_5B3")

    TalkBegin(0xA)
    Call(0, 4)
    TalkEnd(0xA)
    Return()

    # Function_3_5B3 end

    def Function_4_5BE(): pass

    label("Function_4_5BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_68C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_648")

    ChrTalk(    #0
        0xA,
        (
            "哦！是小姐你们。\x01",
            "事故的时候真是多谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xA,
        (
            "其他矿工们\x01",
            "也已经在里面开始工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xA,
        (
            "不介意的话\x01",
            "去见见他们吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_689")

    label("loc_648")


    ChrTalk(    #3
        0xA,
        "事故的时候真是多谢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        (
            "不介意的话\x01",
            "也去见见其他矿工吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_689")

    Jump("loc_A13")

    label("loc_68C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_887")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x77, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_753")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6DA")

    ChrTalk(    #5
        0xA,
        (
            "抱歉，里面不能进去。\x01",
            "因为今天开始重新开工了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_750")

    label("loc_6DA")


    ChrTalk(    #6
        0xA,
        "哟，游击士们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xA,
        (
            "加通老大\x01",
            "终于来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xA,
        (
            "我们也终于\x01",
            "重新开工了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xA,
        (
            "因此，这里又要禁止\x01",
            "无关人士入内了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_750")

    Jump("loc_884")

    label("loc_753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7A9")

    ChrTalk(    #10
        0xA,
        (
            "今天开始我们也\x01",
            "打算重新开工了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xA,
        (
            "不好意思，这里禁止\x01",
            "无关人士入内。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_884")

    label("loc_7A9")


    ChrTalk(    #12
        0xA,
        (
            "哟，游击士们啊\x01",
            "先前承蒙关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xA,
        (
            "我们今天也打算来\x01",
            "重新开工的……\x01",
            "不巧老大还没来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xA,
        (
            "矿工们只好做些准备工作，\x01",
            "现在正在待命中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xA,
        (
            "好像是老大家里\x01",
            "出了麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xA,
        (
            "虽然不太清楚状况\x01",
            "但希望他早点来矿山啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_884")

    Jump("loc_A13")

    label("loc_887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_END)), "loc_966")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8F2")

    ChrTalk(    #17
        0xA,
        (
            "现在你们的游击士同伴\x01",
            "正在里面进行避难引导。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xA,
        (
            "真是帮大忙了。\x01",
            "这下就可以回城里了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_963")

    label("loc_8F2")


    ChrTalk(    #19
        0xA,
        "哟，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xA,
        (
            "现在你们的游击士同伴\x01",
            "正在里面进行避难引导。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xA,
        (
            "真是帮大忙了。\x01",
            "这下就可以回城里了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_963")

    Jump("loc_A13")

    label("loc_966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_A13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9AC")

    ChrTalk(    #22
        0xA,
        (
            "如你们所知，这里是禁止进入的。\x01",
            "无关人士请回吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A13")

    label("loc_9AC")


    ChrTalk(    #23
        0xA,
        (
            "哟，你们是\x01",
            "那次的游击士吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xA,
        (
            "如你们所知，矿山是\x01",
            "禁止无关人士入内的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xA,
        "不好意思请回吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A13")

    Return()

    # Function_4_5BE end

    def Function_5_A14(): pass

    label("Function_5_A14")

    TalkBegin(0xB)
    Call(0, 6)
    TalkEnd(0xB)
    Return()

    # Function_5_A14 end

    def Function_6_A1F(): pass

    label("Function_6_A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_END)), "loc_B34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A71")

    ChrTalk(    #26
        0xB,
        (
            "#050F现在奥利维尔和金\x01",
            "去叫矿工了。\x02\x03",

            "你们就\x01",
            "赶紧前往农场吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B34")

    label("loc_A71")


    ChrTalk(    #27
        0xB,
        (
            "#052F喂喂，你们……\x02\x03",

            "怎么到这边来了。\x01",
            "不是要去农场吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1008F啊，不……\x01",
            "我们现在正要去。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #29
        0xB,
        (
            "#057F……你们以为\x01",
            "为什么要兵分两路啊。\x02\x03",

            "赶快去农场吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1007F明，明白了……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_B34")

    Return()

    # Function_6_A1F end

    def Function_7_B35(): pass

    label("Function_7_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31F, 6)), scpexpr(EXPR_END)), "loc_B3D")
    Return()

    label("loc_B3D")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(    #31
        "\x07\x05大型魔兽正在四处游荡中。\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_C22"),
        (SWITCH_DEFAULT, "loc_C45"),
    )


    label("loc_C22")

    Fade(500)
    OP_89(0x0, -580, -40, -40880, 357)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_C45")

    Battle(0xEEC, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, -580, -40, -40880, 357)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_C7E"),
        (1, "loc_C81"),
        (SWITCH_DEFAULT, "loc_C84"),
    )


    label("loc_C7E")

    EventEnd(0x0)
    Return()

    label("loc_C81")

    OP_B4(0x0)
    Return()

    label("loc_C84")

    EventBegin(0x1)
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x4, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #32
        "\x07\x05消灭了通缉魔兽！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x18FE)
    OP_28(0xB0, 0x4, 0x10)
    OP_28(0xB0, 0x4, 0x2)
    OP_28(0xB0, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_7_B35 end

    def Function_8_CF0(): pass

    label("Function_8_CF0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x326, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_D5F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #33
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1933)
    Jump("loc_DC5")

    label("loc_D5F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #34
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_DC5")

    Jump("loc_DF9")

    label("loc_DC8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_DF9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_CF0 end

    def Function_9_E07(): pass

    label("Function_9_E07")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E1E")
    Call(0, 14)
    Call(0, 15)

    label("loc_E1E")

    OP_6D(-1710, -30, -25410, 0)
    OP_67(0, 10030, -10000, 0)
    OP_6B(3010, 0)
    OP_6C(315000, 0)
    OP_6E(393, 0)
    SetChrPos(0x101, 1330, -30, -53480, 0)
    SetChrPos(0x102, 140, -20, -53920, 0)
    SetChrPos(0xF8, 1340, -40, -55460, 0)
    SetChrPos(0xF9, -110, -30, -55920, 0)

    def lambda_EA5():
        OP_8E(0xFE, 0x532, 0xFFFFFFE2, 0xFFFF54FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EA5)

    def lambda_EC0():
        OP_8E(0xFE, 0x8C, 0xFFFFFFEC, 0xFFFF5538, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EC0)

    def lambda_EDB():
        OP_8E(0xFE, 0x53C, 0xFFFFFFD8, 0xFFFF4FFC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_EDB)

    def lambda_EF6():
        OP_8E(0xFE, 0xFFFFFF92, 0xFFFFFFE2, 0xFFFF5024, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_EF6)

    def lambda_F11():
        OP_6D(120, -40, -43020, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F11)
    OP_C8(0x200, 0x46, "C_PLAC19._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Fade(1000)
    OP_6D(250, -20, -43960, 0)
    OP_67(0, 9530, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #36
        0x101,
        (
            "#1002F#6P好了……\x01",
            "终于要开始调查了。\x02\x03",

            "总之必须赶快\x01",
            "到塔顶上去才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        (
            "#1043F#6P嗯……\x01",
            "不过情况很奇怪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#1004F#6P咦？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x9, 850, -30, -32460, 180)
    ClearChrFlags(0x9, 0x80)
    OP_4A(0x9, 255)

    NpcTalk(    #39
        0x9,
        "男人的声音",
        "#3P你，你们是……！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109F")
    OP_62(0xF8, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_10D3")

    label("loc_109F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C1")
    OP_62(0xF8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_10D3")

    label("loc_10C1")

    OP_62(0xF8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_10D3")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10FA")
    OP_62(0xF9, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_112E")

    label("loc_10FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_111C")
    OP_62(0xF9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Jump("loc_112E")

    label("loc_111C")

    OP_62(0xF9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_112E")

    Sleep(1000)

    def lambda_1139():
        OP_6D(120, -40, -42500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1139)

    def lambda_1151():
        OP_67(0, 9040, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1151)
    OP_8E(0x9, 0x1F4, 0xFFFFFFC4, 0xFFFF5D12, 0xFA0, 0x0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #40
        0x9,
        (
            "#2P难，难道是\x01",
            "联络中提到的游击士？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#1006F#6P嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        "#1042F#6P你是侦察部队的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        "#2P啊、啊啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        (
            "#2P为了向你们说明\x01",
            "塔的状况才留下来的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1261")

    ChrTalk(    #45
        0x106,
        (
            "#555F#6P记得你们是被\x01",
            "戴面具的家伙袭击了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1363")

    label("loc_1261")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12A3")

    ChrTalk(    #46
        0x103,
        (
            "#022F#6P记得你们是被\x01",
            "戴面具的男子袭击了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1363")

    label("loc_12A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12E3")

    ChrTalk(    #47
        0x108,
        (
            "#072F#6P听说有个有\x01",
            "戴面具的男子出现了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1363")

    label("loc_12E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1326")

    ChrTalk(    #48
        0x109,
        (
            "#1063F#6P听说你们是被\x01",
            "戴面具的男子袭击了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1363")

    label("loc_1326")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1363")

    ChrTalk(    #49
        0x105,
        (
            "#043F#6P听说有个有\x01",
            "戴面具的男子出现了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1363")


    ChrTalk(    #50
        0x9,
        (
            "#2P是，是没错\x01",
            "但不仅仅是这个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "#2P怎么说呢……\x01",
            "实在是很奇怪啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1015F#6P奇怪……什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        "#2P看，看了就知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        "#2P总之先到入口来吧。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 500)
    OP_90(0x9, 0x0, 0x0, 0x3A98, 0xFA0, 0x0)
    SetChrPos(0x9, -2440, 30, -23500, 180)
    OP_4B(0x9, 255)
    OP_A2(0x1E03)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_9_E07 end

    def Function_10_143B(): pass

    label("Function_10_143B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_144D")
    Return()

    label("loc_144D")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(    #55
        "\x07\x05要回『埃尔赛尤』吗？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【回船上】\x01",      # 0
            "【不回去】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E9")
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1509")

    label("loc_14E9")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_1509")

    Return()

    # Function_10_143B end

    def Function_11_150A(): pass

    label("Function_11_150A")

    EventBegin(0x0)
    OP_6D(-1900, -90, -56520, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1900, -90, -56520, 0)
    SetChrPos(0x102, -1900, -90, -56520, 0)
    SetChrPos(0xF8, -1900, -90, -56520, 0)
    SetChrPos(0xF9, -1900, -90, -56520, 0)
    OP_48()
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_11_150A end

    def Function_12_159F(): pass

    label("Function_12_159F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15AC")
    Return()

    label("loc_15AC")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15D1")
    Call(0, 14)
    Call(0, 15)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_15D1")

    Fade(1000)
    OP_6D(-540, 100, -23090, 0)
    OP_67(0, 8100, -10000, 0)
    OP_6B(3060, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 800, 40, -22800, 0)
    SetChrPos(0x102, -400, 90, -22800, 0)
    SetChrPos(0xF8, 800, 70, -24200, 0)
    SetChrPos(0xF9, -400, 10, -24200, 0)
    OP_8C(0x9, 0, 0)
    OP_4A(0x9, 255)
    OP_0D()
    Sleep(300)

    ChrTalk(    #56
        0x101,
        "#1004F#6P哎……！？\x02",
    )

    CloseMessageWindow()

    def lambda_1687():
        OP_6D(-930, 2000, -16490, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1687)

    def lambda_169F():
        OP_67(0, 3110, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_169F)

    def lambda_16B7():
        OP_6B(2730, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_16B7)

    def lambda_16C7():
        OP_6C(349000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_16C7)

    def lambda_16D7():
        OP_6E(567, 5000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_16D7)
    WaitChrThread(0x101, 0x3)
    Fade(1000)
    OP_6D(0, 4890, -15580, 0)
    OP_67(0, 1310, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(0, 0)
    OP_6E(412, 0)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #57
        "\x07\x00#1020F那，那是……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_179F")
    SetMessageWindowPos(240, 320, -1, -1)
    SetChrName("提妲")

    AnonymousTalk(    #58
        "\x07\x00#065F#5P能，能量障壁……！？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_18AF")

    label("loc_179F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17E5")
    SetMessageWindowPos(240, 320, -1, -1)
    SetChrName("科洛丝")

    AnonymousTalk(    #59
        "\x07\x00#042F#5P是什么结界吗……！？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_18AF")

    label("loc_17E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_182E")
    SetMessageWindowPos(240, 320, -1, -1)
    SetChrName("凯文神父")

    AnonymousTalk(    #60
        "\x07\x00#1069F#5P难道是……结界吗！？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_18AF")

    label("loc_182E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_186A")
    SetMessageWindowPos(240, 320, -1, -1)
    SetChrName("金")

    AnonymousTalk(    #61
        "\x07\x00#072F#5P唔……结界吗？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_18AF")

    label("loc_186A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18AF")
    SetMessageWindowPos(240, 320, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #62
        "\x07\x00#022F#5P是什么结界呢……！？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_18AF")

    Sleep(100)
    Fade(1000)
    TurnDirection(0x9, 0x102, 0)
    OP_6D(-1450, 90, -22590, 0)
    OP_67(0, 7770, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(315000, 0)
    OP_6E(283, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #63
        0x9,
        (
            "#5P我们到达的时候\x01",
            "已经是这样了……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1931():

        label("loc_1931")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1931")

    QueueWorkItem2(0x101, 1, lambda_1931)
    Sleep(50)

    def lambda_1947():

        label("loc_1947")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1947")

    QueueWorkItem2(0x102, 1, lambda_1947)
    Sleep(50)

    def lambda_195D():

        label("loc_195D")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_195D")

    QueueWorkItem2(0xF8, 1, lambda_195D)
    Sleep(50)

    def lambda_1973():

        label("loc_1973")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_1973")

    QueueWorkItem2(0xF9, 1, lambda_1973)

    ChrTalk(    #64
        0x9,
        (
            "#5P然后，正要调查的时候\x01",
            "那个戴面具的男子就出现了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        (
            "#1043F#6P…………………………\x02\x03",

            "#1042F没有办法\x01",
            "进去吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        (
            "#5P戴面具的男子\x01",
            "就这样直接进去了，\x01",
            "我想应该没问题……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        (
            "#5P我们当时也想追上去，\x01",
            "但是同伴都被打倒了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#1007F#4P是吗……\x02\x03",

            "#1002F这里就交给我们\x01",
            "你先返回部队吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x9,
        (
            "#5P明，明白了……\x01",
            "愿女神保佑各位！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 500)

    def lambda_1AD6():
        OP_6D(-690, 20, -27800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1AD6)
    OP_8E(0x9, 0xFFFFFF42, 0xFFFFFFF6, 0xFFFF6348, 0x1388, 0x0)
    SetChrFlags(0x9, 0x80)
    WaitChrThread(0x101, 0x0)

    def lambda_1B0C():
        OP_6D(-1450, 90, -22590, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B0C)
    WaitChrThread(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_A2(0x1E04)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_12_159F end

    def Function_13_1B3E(): pass

    label("Function_13_1B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B4B")
    Return()

    label("loc_1B4B")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BD0")
    TurnDirection(0xB, 0x0, 400)
    TurnDirection(0x0, 0xB, 0)
    TurnDirection(0x1, 0xB, 0)
    TurnDirection(0x2, 0xB, 0)
    TurnDirection(0x3, 0xB, 0)
    OP_4A(0xB, 255)
    SetChrFlags(0xB, 0x40)
    Call(0, 6)
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x1EC30), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_92(0x0, 0xC, 0x0, 0xBB8, 0x0)
    OP_8C(0xB, 0, 0)
    Sleep(50)
    EventEnd(0x4)
    OP_4B(0xB, 255)
    ClearChrFlags(0xB, 0x40)
    Jump("loc_1C28")

    label("loc_1BD0")

    TurnDirection(0xA, 0x0, 400)
    OP_4A(0xA, 255)
    SetChrFlags(0xA, 0x40)
    Call(0, 4)
    OP_51(0xC, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x3, (scpexpr(EXPR_PUSH_LONG, 0x1EC30), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_92(0x0, 0xC, 0x0, 0xBB8, 0x0)
    OP_8C(0xA, 180, 0)
    Sleep(50)
    EventEnd(0x4)
    OP_4B(0xA, 255)
    ClearChrFlags(0xA, 0x40)

    label("loc_1C28")

    Return()

    # Function_13_1B3E end

    def Function_14_1C29(): pass

    label("Function_14_1C29")

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
        (0, "loc_1CA3"),
        (1, "loc_1CA9"),
        (SWITCH_DEFAULT, "loc_1CAF"),
    )


    label("loc_1CA3")

    OP_A2(0x1200)
    Jump("loc_1CAF")

    label("loc_1CA9")

    OP_A2(0x1201)
    Jump("loc_1CAF")

    label("loc_1CAF")

    Return()

    # Function_14_1C29 end

    def Function_15_1CB0(): pass

    label("Function_15_1CB0")

    FadeToDark(0, 0, -1)
    OP_6D(55450, 4000, 13070, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_15_1CB0 end

    def Function_16_1D3F(): pass

    label("Function_16_1D3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E21")
    EventBegin(0x0)
    Fade(500)
    ClearMapFlags(0x1)
    OP_6D(-40, 4000, -8710, 0)
    OP_67(0, 4950, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(351000, 0)
    OP_6E(412, 0)
    SetChrPos(0x101, 850, 4000, -10070, 0)
    SetChrPos(0x102, -360, 4000, -10110, 0)
    SetChrPos(0xF8, 820, 3600, -11500, 0)
    SetChrPos(0xF9, -450, 3600, -11500, 0)
    OP_43(0x101, 0x0, 0x0, 0x11)
    Sleep(300)
    OP_43(0x102, 0x0, 0x0, 0x12)
    Sleep(300)
    OP_43(0xF8, 0x0, 0x0, 0x13)
    Sleep(300)
    OP_43(0xF9, 0x0, 0x0, 0x14)
    WaitChrThread(0x3, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/C0700   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1E21")

    Return()

    # Function_16_1D3F end

    def Function_17_1E22(): pass

    label("Function_17_1E22")

    OP_91(0xFE, 0x0, 0x0, 0x708, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_1E67():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E67)

    def lambda_1E81():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E81)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_17_1E22 end

    def Function_18_1EA7(): pass

    label("Function_18_1EA7")

    OP_91(0xFE, 0x0, 0x0, 0x708, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_1EEC():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1EEC)

    def lambda_1F06():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1F06)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_18_1EA7 end

    def Function_19_1F2C(): pass

    label("Function_19_1F2C")

    OP_91(0xFE, 0x0, 0x0, 0xAF0, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_1F71():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F71)

    def lambda_1F8B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1F8B)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_19_1F2C end

    def Function_20_1FB1(): pass

    label("Function_20_1FB1")

    OP_91(0xFE, 0x0, 0x0, 0xAF0, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_1FF6():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1FF6)

    def lambda_2010():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2010)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_20_1FB1 end

    def Function_21_2036(): pass

    label("Function_21_2036")

    EventBegin(0x0)
    OP_6D(-40, 4000, -8710, 0)
    OP_67(0, 4950, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(351000, 0)
    OP_6E(412, 0)
    SetChrPos(0x101, 500, 4400, -7000, 180)
    SetChrPos(0x102, -500, 4400, -7000, 180)
    SetChrPos(0xF8, 500, 4400, -7000, 180)
    SetChrPos(0xF9, -500, 4400, -7000, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xF9, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x101, 0x0, 0x0, 0x16)
    Sleep(800)
    OP_43(0x102, 0x0, 0x0, 0x17)
    Sleep(800)
    OP_43(0xF8, 0x0, 0x0, 0x18)
    Sleep(800)
    OP_43(0xF9, 0x0, 0x0, 0x19)
    WaitChrThread(0xF9, 0x0)
    Fade(500)
    OP_6D(100, 4000, -10180, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 100, 4000, -10180, 180)
    SetChrPos(0x1, 100, 4000, -10180, 180)
    SetChrPos(0x2, 100, 4000, -10180, 180)
    SetChrPos(0x3, 100, 4000, -10180, 180)
    OP_0D()
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_21_2036 end

    def Function_22_21C2(): pass

    label("Function_22_21C2")

    OP_22(0x99, 0x0, 0x64)

    def lambda_21CD():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_21CD)

    def lambda_21E7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21E7)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_2208():
        OP_8F(0xFE, 0x1F4, 0xFA0, 0xFFFFD2CE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2208)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_22_21C2 end

    def Function_23_2228(): pass

    label("Function_23_2228")

    OP_22(0x99, 0x0, 0x64)

    def lambda_2233():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2233)

    def lambda_224D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_224D)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_226E():
        OP_8F(0xFE, 0xFFFFFE0C, 0xFA0, 0xFFFFD2CE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_226E)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_23_2228 end

    def Function_24_228E(): pass

    label("Function_24_228E")

    OP_22(0x99, 0x0, 0x64)

    def lambda_2299():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2299)

    def lambda_22B3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_22B3)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_22D4():
        OP_8F(0xFE, 0x1F4, 0xE10, 0xFFFFD698, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_22D4)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_24_228E end

    def Function_25_22F4(): pass

    label("Function_25_22F4")

    OP_22(0x99, 0x0, 0x64)

    def lambda_22FF():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_22FF)

    def lambda_2319():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2319)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_233A():
        OP_8F(0xFE, 0xFFFFFE0C, 0xE10, 0xFFFFD698, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_233A)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_25_22F4 end

    SaveToFile()

Try(main)
