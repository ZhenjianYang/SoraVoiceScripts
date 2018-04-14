from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3100   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C3100_1 ._SN',
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
        '凯诺娜',                               # 9
        '士兵塞缪尔',                           # 10
        '卡西乌斯',                             # 11
        '希德中校',                             # 12
        '测量仪',                               # 13
        '贝尔克副队长',                         # 14
        '士兵',                                 # 15
        '士兵',                                 # 16
        '士兵',                                 # 17
        '士兵',                                 # 18
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
        'ED6_DT27/CH03125 ._CH',             # 00
        'ED6_DT27/CH03120 ._CH',             # 01
        'ED6_DT07/CH01640 ._CH',             # 02
        'ED6_DT27/CH03670 ._CH',             # 03
        'ED6_DT27/CH03590 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
        'ED6_DT07/CH00065 ._CH',             # 06
        'ED6_DT07/CH01310 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT27/CH03125P._CP',             # 00
        'ED6_DT27/CH03120P._CP',             # 01
        'ED6_DT07/CH01640P._CP',             # 02
        'ED6_DT27/CH03670P._CP',             # 03
        'ED6_DT27/CH03590P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
        'ED6_DT07/CH00065P._CP',             # 06
        'ED6_DT07/CH01310P._CP',             # 07
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
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -3230,
        Direction           = 174,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -4990,
        Y                   = 0,
        Z                   = -35710,
        Range               = 5060,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF7D1A,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = 5460,
        TriggerZ            = -60,
        TriggerY            = -46490,
        TriggerRange        = 2000,
        ActorX              = 5460,
        ActorZ              = -60,
        ActorY              = -46490,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6000,
        TriggerZ            = 0,
        TriggerY            = -45540,
        TriggerRange        = 1500,
        ActorX              = 6000,
        ActorZ              = 1500,
        ActorY              = -45540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 31750,
        TriggerZ            = -30,
        TriggerY            = -32759,
        TriggerRange        = 1000,
        ActorX              = 32009,
        ActorZ              = -1030,
        ActorY              = -29320,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2B6",          # 00, 0
        "Function_1_32E",          # 01, 1
        "Function_2_386",          # 02, 2
        "Function_3_42D",          # 03, 3
        "Function_4_F1D",          # 04, 4
        "Function_5_14CA",         # 05, 5
        "Function_6_1813",         # 06, 6
        "Function_7_1D40",         # 07, 7
        "Function_8_1EDB",         # 08, 8
        "Function_9_4356",         # 09, 9
        "Function_10_4372",        # 0A, 10
        "Function_11_438E",        # 0B, 11
        "Function_12_43AA",        # 0C, 12
        "Function_13_43C6",        # 0D, 13
        "Function_14_45E6",        # 0E, 14
        "Function_15_4675",        # 0F, 15
        "Function_16_4CA7",        # 10, 16
        "Function_17_4E6D",        # 11, 17
        "Function_18_53F3",        # 12, 18
        "Function_19_548C",        # 13, 19
        "Function_20_54F2",        # 14, 20
        "Function_21_554B",        # 15, 21
        "Function_22_55A7",        # 16, 22
    )


    def Function_0_2B6(): pass

    label("Function_0_2B6")

    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2DA")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 13)
    Jump("loc_32D")

    label("loc_2DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FB")
    SetMapFlags(0x10000000)
    Event(0, 4)
    Jump("loc_32D")

    label("loc_2FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_311")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(1, 3)
    Jump("loc_32D")

    label("loc_311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_32D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_32D")

    Return()

    # Function_0_2B6 end

    def Function_1_32E(): pass

    label("Function_1_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_33C")
    OP_6F(0x0, 110)

    label("loc_33C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34F")
    OP_65(0x0, 0x1)
    Jump("loc_353")

    label("loc_34F")

    OP_64(0x0, 0x1)

    label("loc_353")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_380")
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_22(0x9E, 0x1, 0x64)
    OP_24(0x9E, 0x4B)

    label("loc_380")

    OP_22(0x1CD, 0x1, 0x5A)
    Return()

    # Function_1_32E end

    def Function_2_386(): pass

    label("Function_2_386")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_3B7"),
        (1, "loc_3C3"),
        (2, "loc_3CF"),
        (3, "loc_3DB"),
        (4, "loc_3E7"),
        (5, "loc_3F3"),
        (6, "loc_3FF"),
        (SWITCH_DEFAULT, "loc_40B"),
    )


    label("loc_3B7")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_417")

    label("loc_3C3")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_417")

    label("loc_3CF")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_417")

    label("loc_3DB")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_417")

    label("loc_3E7")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_417")

    label("loc_3F3")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_417")

    label("loc_3FF")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_417")

    label("loc_40B")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_417")

    label("loc_417")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_417")

    label("loc_42C")

    Return()

    # Function_2_386 end

    def Function_3_42D(): pass

    label("Function_3_42D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_448")
    Call(0, 15)
    Jump("loc_80B")

    label("loc_448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_57E")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51A")

    ChrTalk(    #0
        0xFE,
        (
            "与各关所之间的通讯恢复了，\x01",
            "王国军也做好了作战准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "虽然维持治安也是件十分重要的事情，\x01",
            "不过，如何解决目前的导力停止问题\x01",
            "才是当务之急。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "就连卡西乌斯准将\x01",
            "也感到很伤脑筋吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_578")

    label("loc_51A")


    ChrTalk(    #3
        0xFE,
        (
            "不过，如何解决目前的导力停止问题\x01",
            "才是当务之急。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "就连卡西乌斯准将\x01",
            "也感到很伤脑筋吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_578")

    TalkEnd(0x9)
    Jump("loc_80B")

    label("loc_57E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_END)), "loc_79D")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_END)), "loc_70D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BA")

    ChrTalk(    #5
        0xFE,
        (
            "哟，你们……\x01",
            "找到内燃机了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1000F嗯，已经顺利取得了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#1040F警备艇的各位\x01",
            "也好像没有受伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "是吗？这可是好消息。\x01",
            "赶快去报告吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "救援部队很快\x01",
            "就会来收容他们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "那么，也请你们\x01",
            "努力地修理温泉吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#1000F感谢你们帮了那么多忙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        "#1040F那就先失礼了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_70A")

    label("loc_6BA")


    ChrTalk(    #13
        0xFE,
        (
            "去向司令部报告\x01",
            "有关警备艇的情况吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "那么，也请你们\x01",
            "努力地修理温泉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70A")

    Jump("loc_797")

    label("loc_70D")


    ChrTalk(    #15
        0xFE,
        (
            "卡西乌斯准将\x01",
            "为了重整混乱的王国军\x01",
            "正向各地发出指示。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "虽然说是紧急情况，\x01",
            "但是他那不眠不休地进行指挥的身影，\x01",
            "真可说是全军的楷模。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_797")

    TalkEnd(0x9)
    Jump("loc_80B")

    label("loc_79D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_END)), "loc_807")
    TalkBegin(0x9)

    ChrTalk(    #17
        0xFE,
        (
            "警备艇应该是停在\x01",
            "托兰特平原的某个地方了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "有关内燃机的事情，\x01",
            "请你们去问他们吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Jump("loc_80B")

    label("loc_807")

    Call(0, 16)

    label("loc_80B")

    Return()

    label("loc_80F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_820")
    Call(0, 5)
    Return()

    label("loc_820")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_852")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84D")
    Call(1, 0)
    Return()

    label("loc_84D")

    Call(1, 1)
    Return()

    label("loc_852")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_96C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8E6")

    ChrTalk(    #19
        0x9,
        (
            "可以预料，担任实际警戒任务的\x01",
            "也将以驻留要塞的部队为主。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        (
            "由我们来守护王国军的中枢\x01",
            "承担这中流砥柱的职责也是理所当然的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_969")

    label("loc_8E6")


    ChrTalk(    #21
        0x9,
        (
            "不久希德中校\x01",
            "就要出发去王都了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x9,
        "当然是为了签字仪式的警戒工作。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        (
            "虽然是国家性的仪式，\x01",
            "不过中校去的话就让人放心了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_969")

    Jump("loc_F19")

    label("loc_96C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_A56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9CD")

    ChrTalk(    #24
        0x9,
        (
            "多亏收到了待命的命令，\x01",
            "因此几乎没有受到损害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x9,
        (
            "这个命令来得\x01",
            "真是时候。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A53")

    label("loc_9CD")


    ChrTalk(    #26
        0x9,
        (
            "现在在要塞内部\x01",
            "正在确认受损情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x9,
        (
            "虽然震度不弱，\x01",
            "不过并没有受到损害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "这都是因为事先接到了\x01",
            "准备防范地震的待机命令。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A53")

    Jump("loc_F19")

    label("loc_A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_END)), "loc_B45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AA2")

    ChrTalk(    #29
        0x9,
        (
            "你、你们和准将\x01",
            "谈了些什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x9,
        "可恶，真令人羡慕……\x02",
    )

    CloseMessageWindow()
    Jump("loc_B42")

    label("loc_AA2")


    ChrTalk(    #31
        0x9,
        (
            "刚、刚才是作战本部的\x01",
            "卡西乌斯准将吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "你、你们……\x01",
            "谈了些什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x9,
        (
            "就连我这个已经服役十几年的老兵\x01",
            "也没跟他说过话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        "可恶，真令人羡慕……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B42")

    Jump("loc_F19")

    label("loc_B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 5)), scpexpr(EXPR_END)), "loc_BE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B8B")

    ChrTalk(    #35
        0x9,
        (
            "请避开铺装路面。\x01",
            "否则车辆通过的时候会有麻烦的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BE6")

    label("loc_B8B")


    ChrTalk(    #36
        0x9,
        (
            "请避开铺装路面。\x01",
            "否则车辆通过的时候会有麻烦的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        (
            "其他的地方你们\x01",
            "可以随意设置。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_BE6")

    Jump("loc_F19")

    label("loc_BE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_END)), "loc_E10")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x0, 0x40)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x0, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C81")

    ChrTalk(    #38
        0x9,
        (
            "蔡斯各地好像\x01",
            "都在发生地震。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "要塞的留驻部队也处于警戒状态\x01",
            "以防万一出现的紧急情况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD2")

    label("loc_C81")


    ChrTalk(    #40
        0x9,
        (
            "最近蔡斯各地好像\x01",
            "都在发生地震。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "我们要塞留驻部队也\x01",
            "也正在加强警戒。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_CD2")

    Jump("loc_D27")

    label("loc_CD5")


    ChrTalk(    #42
        0xFE,
        (
            "很遗憾，训练\x01",
            "已经结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "现在正进行抗震准备的工作，\x01",
            "已经顾不上训练了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D27")

    Jump("loc_E0D")

    label("loc_D2A")


    ChrTalk(    #44
        0xFE,
        (
            "哎呀，你们\x01",
            "来得太迟了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "训练早就\x01",
            "已经结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1000F啊，果然是这样……\x02\x03",

            "上面的确写着要尽快过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "嗯，而且现在正在进行抗震准备的工作，\x01",
            "似乎不是训练的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "军队的高官已经\x01",
            "聚集在一起开始讨论了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6D, 0x1, 0x8000)
    OP_A2(0x2)

    label("loc_E0D")

    Jump("loc_F19")

    label("loc_E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_F19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E54")

    ChrTalk(    #49
        0x9,
        "哟，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "今天的训练\x01",
            "看来相当严格呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F19")

    label("loc_E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_EBC")

    ChrTalk(    #51
        0x9,
        (
            "因为是重要的军事设施，\x01",
            "所以是禁止摄影的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "就算再怎么样也不能以\x01",
            "要塞为背景进行摄影。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F19")

    label("loc_EBC")


    ChrTalk(    #53
        0x9,
        (
            "这是王国军的根据地\x01",
            "雷斯顿水上要塞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "民间人士\x01",
            "请勿进入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        "能不能请你们回去？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_F19")

    TalkEnd(0x9)
    Return()

    # Function_3_42D end

    def Function_4_F1D(): pass

    label("Function_4_F1D")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F34")
    Call(0, 18)
    Call(0, 19)

    label("loc_F34")

    SetChrPos(0x101, -1130, 0, -60200, 0)
    SetChrPos(0x107, -120, 0, -61110, 0)
    SetChrPos(0xF7, -1370, 0, -61940, 0)
    SetChrPos(0xF9, -500, 0, -62650, 0)
    ClearMapFlags(0x10)
    OP_6D(560, 0, -4680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(5110, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_FC0():
        OP_6D(680, -140, -49070, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FC0)

    def lambda_FD8():
        OP_67(0, 9500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_FD8)
    OP_C8(0x200, 0x46, "C_PLAC10._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_1014():
        OP_8E(0xFE, 0xFFFFFE98, 0xFFFFFFB0, 0xFFFF4098, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1014)
    Sleep(100)

    def lambda_1034():
        OP_8E(0xFE, 0x30C, 0xFFFFFF88, 0xFFFF3F94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1034)
    Sleep(100)

    def lambda_1054():
        OP_8E(0xFE, 0xFFFFFD12, 0xFFFFFFBA, 0xFFFF3A62, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_1054)
    Sleep(100)

    def lambda_1074():
        OP_8E(0xFE, 0x208, 0xFFFFFF92, 0xFFFF39AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_1074)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    Fade(1000)
    StopSound(0x9470, 0x1FBD0, 0x0)
    OP_6D(190, -40, -49730, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0xF9, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1132")

    ChrTalk(    #56
        0x101,
        (
            "#1011F#5P雷斯顿要塞……\x01",
            "总觉得好怀念。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1170")

    label("loc_1132")


    ChrTalk(    #57
        0x101,
        (
            "#1011F#5P雷斯顿要塞……\x02\x03",

            "来参加训练的时候\x01",
            "总觉得好怀念。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1170")


    ChrTalk(    #58
        0x107,
        (
            "#067F#2P嘿嘿嘿……\x01",
            "我也有那种心情。\x02\x03",

            "#560F因为上次是在晚上和姐姐你们分开的，\x01",
            "所以和印象中有点不同……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1229")

    ChrTalk(    #59
        0x106,
        (
            "#051F嗯，因为上次是\x01",
            "冒险潜入进来的啊。\x02\x03",

            "因此也就变得更加怀念。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1279")

    label("loc_1229")


    ChrTalk(    #60
        0x103,
        (
            "#027F说起来，你们似乎为了\x01",
            "营救博士而潜入过这里吧？\x02\x03",

            "真是的，老是这么乱来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1279")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1330")

    ChrTalk(    #61
        0x104,
        (
            "#032F唔，这么有趣的事情\x01",
            "居然没找我一起去。\x02\x03",

            "你们几个太无情了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    OP_8C(0x107, 225, 400)

    ChrTalk(    #62
        0x101,
        (
            "#1007F#5P为什么非要\x01",
            "特地去叫你啊……\x02\x03",

            "#1006F别说这个了，还是\x01",
            "赶快设置测量仪吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13E1")

    label("loc_1330")


    ChrTalk(    #63
        0x105,
        (
            "#542F原来还发生过那种事啊……\x02\x03",

            "你们竟然能够潜入\x01",
            "这座铜墙铁壁的要塞呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    OP_8C(0x107, 225, 400)

    ChrTalk(    #64
        0x101,
        (
            "#1016F#5P嘿嘿……\x01",
            "稍微用了一点小把戏。\x02\x03",

            "#1006F别说这个了，还是\x01",
            "赶快设置测量仪吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1448")

    ChrTalk(    #65
        0x106,
        (
            "#051F不，先去向门卫\x01",
            "取得设置许可比较好吧。\x02\x03",

            "雾香应该已经联系过了，\x01",
            "大概马上就会同意吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A5")

    label("loc_1448")


    ChrTalk(    #66
        0x103,
        (
            "#020F先去向门卫\x01",
            "取得设置许可比较好吧。\x02\x03",

            "雾香小姐应该已经联系过了，\x01",
            "大概马上就会同意吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A5")


    ChrTalk(    #67
        0x101,
        "#1006F#5P嗯，ＯＫ！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x141C)
    OP_28(0x87, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_4_F1D end

    def Function_5_14CA(): pass

    label("Function_5_14CA")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14EA")
    Call(0, 18)
    Call(0, 19)
    FadeToBright(0, 0)

    label("loc_14EA")

    OP_4A(0x9, 255)
    Fade(1000)
    SetChrPos(0x101, -500, 0, -4790, 0)
    SetChrPos(0xF7, 900, 0, -4790, 0)
    SetChrPos(0x107, -540, 160, -6150, 0)
    SetChrPos(0xF9, 480, 160, -6270, 0)
    OP_6D(320, 0, -3840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #68
        0x9,
        (
            "#5P这里是王国军的根据地\x01",
            "雷斯顿水上要塞。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x9,
        (
            "#5P民间人士\x01",
            "请勿进入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        "#5P能不能请你们回去？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1015F#6P那个，我们是\x01",
            "游击士协会的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #72
        0x9,
        "#5P哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "#5P我听司令部说过了。\x01",
            "好像要设置什么装置吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_16C2")

    ChrTalk(    #74
        0x106,
        (
            "#051F#2P尽量长话短说吧。\x02\x03",

            "我们想早点进行设置，\x01",
            "能不能让我们自由行动呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1713")

    label("loc_16C2")


    ChrTalk(    #75
        0x103,
        (
            "#020F#2P还是尽量长话短说吧。\x02\x03",

            "我们想早点进行设置，\x01",
            "能不能让我们自由行动呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1713")


    ChrTalk(    #76
        0x9,
        (
            "#5P嗯，既然已经有许可了，\x01",
            "就请你们随意设置吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        (
            "#5P不过，请不要设置\x01",
            "在铺装路面上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x9,
        "#5P否则车辆通过的时候会有麻烦的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1006F#6P嗯，明白了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    OP_8C(0xF7, 225, 400)

    ChrTalk(    #80
        0x101,
        (
            "#1006F#5P那么\x01",
            "我们就找个合适的地点吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x107,
        "#061F#6P嗯，是啊。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x9, 255)
    OP_A2(0x141D)
    OP_28(0x87, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_5_14CA end

    def Function_6_1813(): pass

    label("Function_6_1813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1820")
    Return()

    label("loc_1820")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1840")
    Call(0, 18)
    Call(0, 19)
    FadeToBright(0, 0)

    label("loc_1840")

    OP_A2(0x141E)
    Fade(1000)
    SetChrPos(0x101, -910, 250, -36040, 180)
    SetChrPos(0x107, 140, 250, -36150, 180)
    SetChrPos(0xF7, 70, 250, -35070, 180)
    SetChrPos(0xF9, -910, 250, -34770, 180)
    OP_6D(-200, -230, -46450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_18D0():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18D0)
    Sleep(150)

    def lambda_18F0():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_18F0)
    Sleep(100)

    def lambda_1910():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD634, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1910)
    Sleep(200)

    def lambda_1930():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD698, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1930)
    WaitChrThread(0xF9, 0x1)
    OP_8C(0x101, 90, 400)
    OP_8C(0x107, 270, 400)

    ChrTalk(    #82
        0x101,
        (
            "#1006F#6P那么，提妲。\x01",
            "设置在哪儿比较好？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x107,
        "#560F#2P嗯，稍微等一等。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 180, 400)

    def lambda_19B1():
        OP_6B(3270, 3000)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_19B1)

    def lambda_19C1():

        label("loc_19C1")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_19C1")

    QueueWorkItem2(0x101, 1, lambda_19C1)

    def lambda_19D2():

        label("loc_19D2")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_19D2")

    QueueWorkItem2(0xF7, 1, lambda_19D2)

    def lambda_19E3():

        label("loc_19E3")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_19E3")

    QueueWorkItem2(0xF9, 1, lambda_19E3)
    OP_8E(0x107, 0x2EE, 0xFFFFFF42, 0xFFFF41EC, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0x107, 270, 400)
    Sleep(500)
    OP_8C(0x107, 90, 400)
    Sleep(500)
    OP_8C(0x107, 180, 400)
    WaitChrThread(0x1, 0x0)

    ChrTalk(    #84
        0x107,
        (
            "#064F#5P嗯，除了铺装路面\x01",
            "以外能放的地方嘛……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 45, 400)

    def lambda_1A6B():
        OP_6D(2690, -160, -46040, 2500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1A6B)
    Sleep(500)
    OP_8E(0x107, 0x1284, 0xFFFFFFD8, 0xFFFF46BA, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0x107, 0, 400)
    Sleep(500)
    OP_8C(0x107, 180, 400)
    Sleep(500)

    ChrTalk(    #85
        0x107,
        (
            "#060F#5P……虽然旁边有照明设备，\x01",
            "不过这样的距离应该是没有问题。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 225, 400)
    Sleep(500)

    ChrTalk(    #86
        0x107,
        (
            "#060F#5P蔡斯在那边……\x01",
            "嗯，方向也没有问题。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)
    Sleep(500)

    ChrTalk(    #87
        0x107,
        (
            "#061F#2P虽然就在牌子前面，\x01",
            "我想在这里就可以了。\x02\x03",

            "现在就开始设置测量仪吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF9, 0x1)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【设置测量仪】\x01",      # 0
            "【先不设置】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C33")

    ChrTalk(    #88
        0x107,
        (
            "#560F#2P那么\x01",
            "开始进行设置作业啰。\x02\x03",

            "请稍等一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D3B")

    label("loc_1C33")


    ChrTalk(    #89
        0x107,
        (
            "#064F#2P哎……不设置吗？\x02\x03",

            "#060F那就等准备好以后\x01",
            "再来这个地方调查吧。\x02\x03",

            "到时再进行设置工作。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-910, -140, -47040, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -910, -140, -47040, 90)
    SetChrPos(0x1, -910, -140, -47040, 90)
    SetChrPos(0x2, -910, -140, -47040, 90)
    SetChrPos(0x3, -910, -140, -47040, 90)
    OP_69(0x0, 0x0)
    OP_65(0x0, 0x1)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    label("loc_1D3B")

    Call(0, 8)
    Return()

    # Function_6_1813 end

    def Function_7_1D40(): pass

    label("Function_7_1D40")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 3460, -40, -46290, 90)
    SetChrPos(0x107, 4450, -20, -46910, 90)
    SetChrPos(0xF7, 3170, -40, -47550, 90)
    SetChrPos(0xF9, 4100, 70, -48420, 0)
    OP_6D(4450, -20, -46910, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【设置测量仪】\x01",      # 0
            "【先不设置】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E67")
    OP_8C(0x107, 270, 400)

    ChrTalk(    #90
        0x107,
        (
            "#061F#2P那么\x01",
            "开始进行设置作业啰。\x02\x03",

            "请稍等一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED6")

    label("loc_1E67")

    OP_8C(0x107, 270, 400)

    ChrTalk(    #91
        0x107,
        (
            "#064F#2P哎……不设置吗？\x02\x03",

            "#060F那就等准备好以后\x01",
            "再来这个地方调查吧。\x02\x03",

            "到时再进行设置工作。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    EventEnd(0x0)
    Return()

    label("loc_1ED6")

    Call(0, 8)
    Return()

    # Function_7_1D40 end

    def Function_8_1EDB(): pass

    label("Function_8_1EDB")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 3460, -40, -46290, 90)
    SetChrPos(0x107, 4450, -20, -46910, 90)
    SetChrPos(0xF7, 3170, -40, -47550, 90)
    SetChrPos(0xF9, 4100, 70, -48420, 0)
    OP_6D(4450, -20, -46910, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #92
        0x107,
        "#061F嗯，设置完成！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20BD")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇第一次设置测量仪】\x01",                                # 0
            "【◇已经在托兰特平原设置了测量仪】\x01",                    # 1
            "【◇已经在卡鲁迪亚隧道设置了测量仪】\x01",                  # 2
            "【◇已经在卡鲁迪亚隧道和托兰特平原设置了测量仪】\x01",      # 3
            "【◇不变更】\x01",                                          # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_208D"),
        (1, "loc_2099"),
        (2, "loc_20A5"),
        (3, "loc_20B1"),
        (SWITCH_DEFAULT, "loc_20BD"),
    )


    label("loc_208D")

    OP_A3(0x1419)
    OP_A3(0x141B)
    OP_A3(0x141F)
    Jump("loc_20BD")

    label("loc_2099")

    OP_A2(0x1419)
    OP_A3(0x141B)
    OP_A3(0x141F)
    Jump("loc_20BD")

    label("loc_20A5")

    OP_A3(0x1419)
    OP_A2(0x141B)
    OP_A3(0x141F)
    Jump("loc_20BD")

    label("loc_20B1")

    OP_A2(0x1419)
    OP_A2(0x141B)
    OP_A3(0x141F)
    Jump("loc_20BD")

    label("loc_20BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_250B")

    ChrTalk(    #93
        0x101,
        (
            "#1004F#3P哟，组装起来以后\x01",
            "原来是这个样子的啊。\x02\x03",

            "#1015F不过……\x01",
            "这个像盘子一样的东西是什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)

    ChrTalk(    #94
        0x107,
        (
            "#060F#2P这叫碟型天线，\x01",
            "是个可以集中导力波的天线。\x02\x03",

            "通过它可以把强力的导力波\x01",
            "传送到很远的地方……\x02\x03",

            "即使在卡鲁迪亚隧道那种地方\x01",
            "也都一样可以传送到呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22FD")

    ChrTalk(    #95
        0x104,
        (
            "#033F哦……\x01",
            "那可是很厉害的东西啊。\x02\x03",

            "#030F那么…\x01",
            "有打算在市面上销售吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 180, 400)

    ChrTalk(    #96
        0x107,
        (
            "#560F啊，我也不是\x01",
            "很清楚呢，\x02\x03",

            "不过，爷爷的发明一般在问世\x01",
            "半年后就会在市面上销售了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x104,
        "#031F呵，这真是令人期待啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_22FA")

    ChrTalk(    #98
        0x103,
        "#027F哎呀……和你的『本职工作』有关吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x104,
        "#035F我听不懂你在说什么呢。\x02",
    )

    CloseMessageWindow()

    label("loc_22FA")

    Jump("loc_2457")

    label("loc_22FD")


    ChrTalk(    #100
        0x105,
        (
            "#044F那个，提妲。\x02\x03",

            "我以前听说过，导力波遇到障碍物\x01",
            "就会减弱，不过……\x02\x03",

            "即使在卡鲁迪亚隧道那种地方\x01",
            "那种地方也可以传送呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 180, 400)

    ChrTalk(    #101
        0x107,
        (
            "#560F嗯，这种天线\x01",
            "会赋予导力波指向性，\x01",
            "所以可以顺利进行传送。\x02\x03",

            "即使是像洞窟那种地方，\x01",
            "导力波似乎也能藉由墙壁反射\x01",
            "持续传送到出口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x105,
        (
            "#040F原来如此……\x02\x03",

            "#041F不愧是拉赛尔博士啊，\x01",
            "天才的称号果然不是浪得虚名。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2457")


    ChrTalk(    #103
        0x101,
        (
            "#1007F#3P唔，虽然现在还\x01",
            "无法亲身体会其厉害之处……\x02\x03",

            "#1006F不过这样一来就可以\x01",
            "把地震情报传送出去了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)

    ChrTalk(    #104
        0x107,
        (
            "#560F#2P啊，不是。\x01",
            "还没有启动呢……\x02\x03",

            "现在就打开开关了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_255A")

    label("loc_250B")


    ChrTalk(    #105
        0x101,
        (
            "#1006F#3P那么只剩下\x01",
            "打开开关了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 270, 400)

    ChrTalk(    #106
        0x107,
        "#560F#2P嗯，我马上就打开。\x02",
    )

    CloseMessageWindow()

    label("loc_255A")

    OP_8C(0x107, 90, 400)
    OP_8C(0xF9, 0, 400)
    Sleep(500)
    Fade(500)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 6)
    OP_0D()
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_22(0x9E, 0x1, 0x64)
    OP_24(0x9E, 0x4B)
    Sleep(2000)
    Fade(500)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 65535)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26F3")
    OP_8C(0x107, 270, 400)

    ChrTalk(    #107
        0x107,
        (
            "#061F#2P嗯⊙\x01",
            "这样启动就完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#1006F#3P辛苦呢了，提妲。\x02\x03",

            "天线虽然看起来很容易坏掉，\x01",
            "不过放在这里的话就不用担心会有魔兽了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x107,
        (
            "#560F#2P嗯，而且这个装置\x01",
            "有类似街灯一样\x01",
            "驱赶魔兽的功能。\x02\x03",

            "所以就算设置在其它地方，\x01",
            "我想也不必担心会有什么事情发生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        "#1011F#3P是吗，那我就放心了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_275F")

    label("loc_26F3")

    OP_8C(0x107, 270, 400)

    ChrTalk(    #111
        0x107,
        (
            "#061F#2P嗯⊙\x01",
            "这样启动就完成了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2743")

    ChrTalk(    #112
        0x106,
        "#051F#6P哦，辛苦了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_275F")

    label("loc_2743")


    ChrTalk(    #113
        0x103,
        "#021F#6P呵呵，辛苦了。\x02",
    )

    CloseMessageWindow()

    label("loc_275F")

    SetChrPos(0xA, 1460, 250, -34530, 180)
    ClearChrFlags(0xA, 0x80)

    NpcTalk(    #114
        0xA,
        "男性的声音",
        "#4P哟，你们在工作啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        "#1004F#3P咦……\x02",
    )

    CloseMessageWindow()

    def lambda_27B6():
        OP_6D(2480, -90, -43470, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_27B6)

    def lambda_27CE():
        OP_67(0, 8500, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_27CE)

    def lambda_27E6():
        OP_8E(0xA, 0x5B4, 0xB4, 0xFFFF6636, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_27E6)
    OP_8C(0x101, 0, 400)
    OP_8C(0x107, 0, 400)
    OP_8C(0xF7, 0, 400)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0xA, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #116
        0x101,
        "#1004F#2P#3S老爸！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_28C1")

    ChrTalk(    #117
        0x106,
        "#052F#6P大叔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D9")

    label("loc_28C1")


    ChrTalk(    #118
        0x103,
        "#023F#6P老师……！\x02",
    )

    CloseMessageWindow()

    label("loc_28D9")


    def lambda_28DF():
        OP_6D(1780, 0, -41760, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_28DF)
    OP_43(0x101, 0x0, 0x0, 0x9)
    Sleep(200)

    def lambda_2903():
        OP_8E(0xFE, 0x618, 0x0, 0xFFFF6064, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2903)
    OP_43(0xF7, 0x0, 0x0, 0xB)
    Sleep(300)
    OP_43(0x107, 0x0, 0x0, 0xA)
    Sleep(200)
    OP_43(0xF9, 0x0, 0x0, 0xC)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0xA, 0x1)
    Sleep(500)

    ChrTalk(    #119
        0xA,
        (
            "#1120F#5P好久不见了，艾丝蒂尔。\x02\x03",

            "虽然说得有些晚，\x01",
            "不过强化训练，真是辛苦你了。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0xF9, 0x0)

    ChrTalk(    #120
        0x101,
        (
            "#1008F#4P真是的～！\x01",
            "不是辛苦不辛苦的问题！\x02\x03",

            "什么啊，老爸。\x01",
            "你怎么在这里？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xA,
        (
            "#1120F#5P哈哈，别忘了我可是个军人。\x02\x03",

            "这里是作战总部的据点，\x01",
            "所以大多数时间都会在这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        "#1017F#4P这样啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2AAC")

    ChrTalk(    #123
        0x106,
        (
            "#051F#6P听说你当上\x01",
            "作战总部长了是吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD7")

    label("loc_2AAC")


    ChrTalk(    #124
        0x103,
        (
            "#020F#6P听说你当上\x01",
            "作战总部长了是吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AD7")


    ChrTalk(    #125
        0xA,
        (
            "#1123F#5P嗯，摩尔根将军\x01",
            "三番五次地劝说我……\x02\x03",

            "最后实在拗不过他。\x02\x03",

            "所以现在搞得天天连点休息的时间也都没有了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2C07")

    ChrTalk(    #126
        0x106,
        (
            "#051F#6P嘿嘿，这叫平日\x01",
            "『积德』所致。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#1016F#4P哈哈，您就不要抱怨了吧。\x02\x03",

            "#1006F不过，老爸穿军服的样子\x01",
            "乍一看，还真感觉有点不协调，不过……\x02\x03",

            "但仔细看看也挺\x01",
            "有板有眼的嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CB5")

    label("loc_2C07")


    ChrTalk(    #128
        0x103,
        "#021F#6P呵呵，您辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1016F#4P不过老爸\x01",
            "说不定算是自作自受呢。\x02\x03",

            "#1006F不过，老爸穿军服的样子\x01",
            "乍一看，还真感觉有点不协调，不过……\x02\x03",

            "但仔细看看也挺\x01",
            "有板有眼的嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CB5")


    ChrTalk(    #130
        0xA,
        (
            "#1121F#5P哼哼，那是当然的。\x02\x03",

            "我以前可是号称\x01",
            "王国军第一美男子呢。\x02\x03",

            "理查德算得了什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        (
            "#1007F#4P真是的，马上就得意忘形了。\x02\x03",

            "#1017F嘿嘿……不过太好了。\x02\x03",

            "听说你那么忙\x01",
            "我还有点担心呢，\x01",
            "不过看上去您比我想象中还要有精神。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xA,
        (
            "#1125F#5P嗯，现在还算好吧。\x02\x03",

            "#1122F话说回来……\x01",
            "我已经看过来自协会的报告书。\x02\x03",

            "他们似乎已经在卢安开始行动了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        (
            "#1003F#4P啊……嗯。\x02\x03",

            "#1002F『噬身之蛇』的党羽。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2EA6")

    ChrTalk(    #134
        0x106,
        (
            "#050F#6P和报告书上写的一样，\x01",
            "那些家伙比预料中的还要厉害。\x02\x03",

            "军方不准备拟定相应的对策吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F07")

    label("loc_2EA6")


    ChrTalk(    #135
        0x103,
        (
            "#022F#6P和报告书上写的一样，\x01",
            "看来那些家伙比预料中的还要危险。\x02\x03",

            "军方不准备拟定相应的对策吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F07")


    ChrTalk(    #136
        0xA,
        (
            "#1125F#5P嗯，要是能尽快建立起一个\x01",
            "可以代替情报部的机构就好了……\x02\x03",

            "正规军和国境师团的改组\x01",
            "总算是刚结束。\x02\x03",

            "#1120F目前，有关调查的事情\x01",
            "只能暂时拜托协会了。\x02\x03",

            "关于这次的怪异地震\x01",
            "也指望着你们能调查出一些眉目出来。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3013")

    ChrTalk(    #137
        0x106,
        (
            "#551F#6P真是的……\x01",
            "我就知道是这个样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_302F")

    label("loc_3013")


    ChrTalk(    #138
        0x103,
        "#027F#6P呵呵，明白了。\x02",
    )

    CloseMessageWindow()

    label("loc_302F")


    ChrTalk(    #139
        0x101,
        (
            "#1006F#4P反正老爸平时也\x01",
            "很少拜托我做什么事情。\x02\x03",

            "这次，就当是我孝敬您吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xA,
        (
            "#1120F#5P噢，什么时候开始变得会那么说话了呢。\x02\x03",

            "你的新衣服也挺合适的，\x01",
            "似乎多了一点女人味了。\x02\x03",

            "如果约修亚看到你现在这个样子，一定会感到很吃惊的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1025F#4P啊……\x02\x03",

            "#1016F嘿嘿，真是那样的话就好了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xB, 690, 250, -31680, 180)
    ClearChrFlags(0xB, 0x80)

    NpcTalk(    #142
        0xB,
        "男性的声音",
        "#4P卡西乌斯准将！\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    def lambda_319F():
        OP_6D(1780, 0, -39760, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_319F)

    def lambda_31B7():
        TurnDirection(0xA, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_31B7)
    OP_8E(0xB, 0x1FE, 0xFA, 0xFFFF6898, 0x9C4, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3227")

    ChrTalk(    #143
        0x101,
        "#1004F#4P啊……希德少校！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3224")

    ChrTalk(    #144
        0x106,
        "#052F#6P还真是好久不见。\x02",
    )

    CloseMessageWindow()

    label("loc_3224")

    Jump("loc_326B")

    label("loc_3227")


    ChrTalk(    #145
        0x101,
        "#1011F#4P啊……希德中校！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_326B")

    ChrTalk(    #146
        0x106,
        "#051F#6P哟，又见面了。\x02",
    )

    CloseMessageWindow()

    label("loc_326B")


    def lambda_3271():
        OP_6D(1780, 0, -41760, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3271)

    def lambda_3289():
        OP_8E(0xB, 0x1FE, 0x0, 0xFFFF60C8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3289)
    Sleep(1000)
    TurnDirection(0xA, 0xF9, 400)
    WaitChrThread(0xB, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6D, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35CA")

    NpcTalk(    #147
        0xB,
        "希德",
        (
            "#701F哈哈，好久不见。\x02\x03",

            "拉赛尔博士绑架事件时\x01",
            "给你们添了不少麻烦。\x02\x03",

            "我一直打算有机会的话\x01",
            "要好好地向你们道歉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        (
            "#1016F#4P哈哈，没关系啦。\x01",
            "你不是也放我们逃跑了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x107,
        (
            "#560F那个那个……\x01",
            "真是非常感谢您的帮忙。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #150
        0xB,
        "希德",
        (
            "#703F是吗……\x01",
            "你们能这么想我真是松了一口气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xA,
        (
            "#1120F#5P顺便说一下\x01",
            "由于在镇压政变时的活跃表现，\x01",
            "希德最近已经升任为中校了。\x02\x03",

            "今后你们就叫他希德中校吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(    #152
        0xB,
        "#702F#6P准、准将……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        (
            "#1011F#4P哟～是这样啊。\x02\x03",

            "#1001F恭喜你，希德中校！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x107,
        "#061F恭喜恭喜。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_34F9")

    ChrTalk(    #155
        0x106,
        (
            "#051F#6P哈哈，这不是好事吗。\x02\x03",

            "像你这样的人\x01",
            "就应该得到相当高的评价。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34F9")

    TurnDirection(0xB, 0xF7, 400)

    ChrTalk(    #156
        0xB,
        (
            "#701F那个……谢谢。\x02\x03",

            "我只是做了我应该做的事，\x01",
            "真有点不太好意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        (
            "#1006F#4P又来了～\x01",
            "你真是个谦虚的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xA,
        (
            "#1125F#5P嗯，希德你也应该再\x01",
            "多担负起一些责任来。\x02\x03",

            "不然，我到什么时候\x01",
            "才能引退啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36D1")

    label("loc_35CA")


    ChrTalk(    #159
        0xA,
        (
            "#1124F#5P哟……\x02\x03",

            "你们已经打过招呼了啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xB,
        (
            "#701F是，在那次特别训练中……\x02\x03",

            "托你们的福，\x01",
            "训练也获得了很好的成果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xA,
        (
            "#1125F#5P是吗，看来我不在的时候\x01",
            "你干得不错啊。\x02\x03",

            "既然晋升中校了，那就期待希德你\x01",
            "今后能表现的更加活跃一些。\x02\x03",

            "不然，我到什么时候\x01",
            "才能引退啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36D1")

    OP_8C(0xB, 90, 400)

    ChrTalk(    #162
        0xB,
        (
            "#702F#6P过奖了，不过，要是您轻易引退的话，\x01",
            "我们会感到很为难的。\x02\x03",

            "至少也请等到\x01",
            "摩尔根将军退役之后吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xA,
        "#1123F#5P啊，那要等到何年何月啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 400)

    ChrTalk(    #164
        0xA,
        (
            "#1124F#5P对了，希德。\x01",
            "你不是有事找我吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xB,
        (
            "#700F#6P是的，摩尔根将军说\x01",
            "会比预定的时间提早到达。\x02\x03",

            "再过一会儿\x01",
            "就会到达起降场了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xA,
        (
            "#1125F#5P没办法……\x01",
            "那位大人也真性急。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)
    OP_8C(0xB, 180, 400)

    ChrTalk(    #167
        0xA,
        (
            "#1120F#5P……好了\x01",
            "我要去参加军事会议了。\x02\x03",

            "真抱歉，艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        (
            "#1017F#4P没关系，别介意。\x01",
            "能跟你说上几句话，我就已经很开心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xA,
        "#1120F#5P嗯，我也一样。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xF7, 400)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3976")

    ChrTalk(    #170
        0xA,
        (
            "#1120F#5P阿加特。\x01",
            "不好意思，艾丝蒂尔就拜托你了。\x02\x03",

            "虽然她已经是一名正游击士了，\x01",
            "但是，肯定经验还尚浅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x106,
        "#051F#6P嗯，放心交给我吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A03")

    label("loc_3976")


    ChrTalk(    #172
        0xA,
        (
            "#1120F#5P雪拉扎德。\x01",
            "不好意思，艾丝蒂尔就拜托你了。\x02\x03",

            "虽然她已经是一名正游击士了，\x01",
            "但是，肯定经验还尚浅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x103,
        "#027F#6P嗯，放心交给我吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3A03")

    TurnDirection(0xA, 0x101, 400)
    Sleep(400)

    ChrTalk(    #174
        0xA,
        (
            "#1121F#5P提妲你也\x01",
            "很努力嘛。\x02\x03",

            "虽然你姐姐不成器，\x01",
            "不过还是请多帮助她。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x107,
        (
            "#067F嘿嘿，我知道。\x02\x03",

            "#560F另外，关于\x01",
            "『福音』的解析……\x02\x03",

            "爷爷兴奋地说他\x01",
            "找到了意想不到的关键点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xA,
        (
            "#1120F#5P是吗……\x01",
            "这可真令人期待。\x02\x03",

            "替我向博士问好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x107,
        "#061F是的。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C3A")

    ChrTalk(    #178
        0xA,
        (
            "#1120F#5P听说奥利维尔\x01",
            "也在帮我那个不成器的女儿。\x02\x03",

            "抛开那件事不说，我还是要谢谢你的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x104,
        (
            "#035F#6P呵呵，您客气了。\x02\x03",

            "#030F难得一看的歌剧第二幕。\x01",
            "我没理由不参加呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xA,
        (
            "#1125F#5P呵呵……也好。\x02\x03",

            "#1120F不过也别忘了\x01",
            "你自己的目的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x104,
        "#031F#6P嗯，我会谨记在心的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        "#1015F#2P？？？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DCB")

    label("loc_3C3A")


    ChrTalk(    #183
        0xA,
        (
            "#1125F#5P公主殿下，也感谢您\x01",
            "帮助我这个不成器的女儿。\x02\x03",

            "#1120F不过，有机会的话也请您\x01",
            "能把自己的想法说给周围人听吧。\x02\x03",

            "不论陛下是怎么想的，\x01",
            "尤莉亚上尉和摩尔根将军他们\x01",
            "看上去似乎都有些焦虑不安。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x105,
        (
            "#047F#4P……嗯。\x02\x03",

            "#040F我会找机会好好跟他们说明\x01",
            "并寻求他们的理解的。\x02\x03",

            "我需要进行一次\x01",
            "找寻自我的旅程……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xA,
        (
            "#1120F#5P哈呵呵，殿下您\x01",
            "一定能成功的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x105,
        (
            "#048F#4P谢谢……\x01",
            "能听到你说这句话，我就安心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DCB")


    ChrTalk(    #187
        0xA,
        (
            "#1125F#5P……那么我就先走了。\x02\x03",

            "#1120F虽然无法直接帮助你们，\x01",
            "不过，如果有协会应付不了的事情\x01",
            "就随时联系我好了。\x02\x03",

            "我会尽力协助你们的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        (
            "#1006F#4P嗯……\x01",
            "我会记住的。\x02\x03",

            "#1018F老爸你也要努力工作啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xA,
        (
            "#1121F#5P哈哈，我自然知道会怎么做\x01",
            "而不至于被摩尔根将军所骂。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 400)

    ChrTalk(    #190
        0xA,
        "#1120F#2P希德，我们走吧。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 90, 400)

    ChrTalk(    #191
        0xB,
        "#701F#6P是！\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 0, 400)

    def lambda_3F22():
        OP_90(0xFE, 0x0, 0x0, 0x36B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3F22)
    Sleep(600)
    OP_8C(0xB, 0, 400)

    def lambda_3F49():
        OP_90(0xFE, 0x0, 0x0, 0x36B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3F49)

    def lambda_3F64():
        OP_6D(1780, 250, -37820, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3F64)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    def lambda_3F8B():
        OP_6D(1780, 0, -41540, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F8B)

    def lambda_3FA3():
        OP_67(0, 9500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3FA3)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)

    ChrTalk(    #192
        0x101,
        (
            "#1017F#5P唔～老爸他们比我\x01",
            "想象中的还要忙。\x02\x03",

            "既然如此，作为游击士协会\x01",
            "理所当然也不能输给他们。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4071")

    ChrTalk(    #193
        0x106,
        (
            "#051F#6P嗯，是啊。\x02\x03",

            "好好做出成果来\x01",
            "让大叔刮目相看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40B3")

    label("loc_4071")


    ChrTalk(    #194
        0x103,
        (
            "#021F#6P呵呵，是啊。\x02\x03",

            "#020F好好做出成果来\x01",
            "让老师也吃一惊吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40B3")

    OP_8C(0xF7, 90, 400)
    OP_8C(0x101, 270, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_418E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4129")

    ChrTalk(    #195
        0x106,
        (
            "#051F#6P好，这个地方就ＯＫ了。\x02\x03",

            "保持这种步调，\x01",
            "将剩下的测量仪也设置完毕吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4176")

    label("loc_4129")


    ChrTalk(    #196
        0x103,
        (
            "#027F#6P好，这个地方就搞定了。\x02\x03",

            "保持这种步调，\x01",
            "继续设置剩下的测量仪吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4176")


    ChrTalk(    #197
        0x101,
        "#1006F#2P明白！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4346")

    label("loc_418E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_422F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_41DD")

    ChrTalk(    #198
        0x106,
        (
            "#051F#6P好，这是第二个了。\x02\x03",

            "去把最后一个也搞定吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4217")

    label("loc_41DD")


    ChrTalk(    #199
        0x103,
        (
            "#526F#6P那么，这是第二个了。\x02\x03",

            "马上去设置最后一个吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4217")


    ChrTalk(    #200
        0x101,
        "#1000F#2PＯＫ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4346")

    label("loc_422F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_429F")

    ChrTalk(    #201
        0x106,
        (
            "#051F#6P好，这样一来所有的\x01",
            "测量仪都设置完毕了。\x02\x03",

            "老爷子还在等着我们，\x01",
            "赶快去中央工房的演算室吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4314")

    label("loc_429F")


    ChrTalk(    #202
        0x103,
        (
            "#026F#6P那么，这样一来所有的\x01",
            "测量仪都设置完毕了呢。\x02\x03",

            "#020F拉赛尔博士还在等着我们，\x01",
            "现在就回中央工房的演算室吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4314")


    ChrTalk(    #203
        0x101,
        (
            "#1006F#2PＯＫ。\x01",
            "就在中央工房的５楼吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x87, 0x1, 0x200)

    label("loc_4346")

    OP_64(0x0, 0x1)
    OP_A2(0x141F)
    OP_28(0x87, 0x1, 0x100)
    EventEnd(0x0)
    Return()

    # Function_8_1EDB end

    def Function_9_4356(): pass

    label("Function_9_4356")

    OP_8E(0x101, 0x74E, 0x0, 0xFFFF5B78, 0x9C4, 0x0)
    OP_8C(0x101, 0, 400)
    Return()

    # Function_9_4356 end

    def Function_10_4372(): pass

    label("Function_10_4372")

    OP_8E(0x107, 0x7BC, 0xFFFFFFBA, 0xFFFF5696, 0x7D0, 0x0)
    OP_8C(0x107, 0, 400)
    Return()

    # Function_10_4372 end

    def Function_11_438E(): pass

    label("Function_11_438E")

    OP_8E(0xF7, 0x30C, 0x0, 0xFFFF5B00, 0x9C4, 0x0)
    OP_8C(0xF7, 0, 400)
    Return()

    # Function_11_438E end

    def Function_12_43AA(): pass

    label("Function_12_43AA")

    OP_8E(0xF9, 0x3CA, 0xFFFFFFCE, 0xFFFF566E, 0x7D0, 0x0)
    OP_8C(0xF9, 0, 400)
    Return()

    # Function_12_43AA end

    def Function_13_43C6(): pass

    label("Function_13_43C6")

    EventBegin(0x0)
    OP_6D(7290, 8370, -11590, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(310000, 0)
    OP_6E(326, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 41020, 8200, -35260, 270)

    def lambda_443A():
        OP_6D(38570, 8950, -35140, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_443A)

    def lambda_4452():
        OP_67(0, 3000, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4452)

    def lambda_446A():
        OP_6C(315000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_446A)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #204
        0x8,
        (
            "#1182F#6P监视塔上有导力感应器……\x02\x03",

            "水中设置鱼雷群……\x02\x03",

            "防守果然是滴水不漏……\x02\x03",

            "#1322F呼，没办法……\x02\x03",

            "还是像他们说的一样，\x01",
            "只能使用那个东西了……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_8C(0x8, 90, 400)
    Sleep(500)

    ChrTalk(    #205
        0x8,
        (
            "#1181F#5P阁下……很快就好了。\x02\x03",

            "请再等一等。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_24(0x1CD, 0x5A)
    Sleep(200)
    OP_24(0x1CD, 0x50)
    Sleep(200)
    OP_24(0x1CD, 0x46)
    Sleep(200)
    OP_24(0x1CD, 0x3C)
    Sleep(200)
    OP_24(0x1CD, 0x32)
    Sleep(200)
    OP_24(0x1CD, 0x28)
    Sleep(200)
    OP_24(0x1CD, 0x1E)
    Sleep(200)
    OP_23(0x1CD)
    OP_0D()
    OP_AD(0x2400A6, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A2(0x10F0)
    OP_A2(0x1600)
    NewScene("ED6_DT21/T3100   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_13_43C6 end

    def Function_14_45E6(): pass

    label("Function_14_45E6")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(40, 3450, -7970, 0)
    OP_67(0, 3180, -10000, 0)
    OP_6B(4019, 0)
    OP_6C(330000, 0)
    OP_6E(496, 0)
    OP_C8(0x200, 0x46, "C_PLAC10._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C3110   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_14_45E6 end

    def Function_15_4675(): pass

    label("Function_15_4675")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4695")
    Call(0, 18)
    Call(0, 20)
    FadeToBright(0, 0)

    label("loc_4695")

    OP_4A(0x9, 255)
    Fade(1000)
    SetChrPos(0x101, -440, 0, -4750, 0)
    SetChrPos(0x102, 590, 0, -4750, 0)
    SetChrPos(0xF8, -840, 150, -6050, 0)
    SetChrPos(0xF9, 480, 100, -6050, 0)
    OP_8C(0x9, 180, 0)
    OP_6D(800, 0, -3520, 0)
    OP_67(0, 7630, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(45000, 0)
    OP_6E(291, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #206
        0x9,
        (
            "#5P你们……\x01",
            "我记得你们是游击士吧。\x02\x03",

            "雷斯顿要塞现在\x01",
            "已经处于紧急警戒状态了。\x02\x03",

            "没有紧要事情的话\x01",
            "就请你们回去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        (
            "#1015F#6P嗯……\x02\x03",

            "卡西乌斯准将\x01",
            "现在在要塞里吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x9,
        (
            "#5P当然在……\x01",
            "因为通讯障碍和导力兵器的停止\x01",
            "王国军正陷入大混乱之中。\x02\x03",

            "为了重整指挥系统\x01",
            "准将大人日夜不停地在\x01",
            "向各地做出指示。\x02\x03",

            "就算是游击士\x01",
            "也没办法让你们见他……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        "#1025F是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x102,
        (
            "#1035F#4P请问……\x01",
            "能不能通融一下呢？\x02\x03",

            "#1043F其实她是准将的女儿。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #211
        0x9,
        (
            "#5P是、是吗！？\x02\x03",

            "倒是听说过他有个\x01",
            "当游击士的女儿……\x02\x03",

            "要是这样的话就另当别论了！\x01",
            "我现在马上去报告！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        (
            "#1004F#6P啊，不用了。\x01",
            "还是算了吧。\x02\x03",

            "#1008F我也不想在他这么忙的时候\x01",
            "打扰他的工作。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #213
        0x102,
        "#1044F#2P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A1E")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #214
        0x103,
        (
            "#524F#6P只是一小会儿的话\x01",
            "应该无所谓吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_4AB9")

    label("loc_4A1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A6A")
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #215
        0x106,
        (
            "#555F#6P只是一小会儿的话\x01",
            "应该无所谓吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Jump("loc_4AB9")

    label("loc_4A6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AB9")
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(    #216
        0x108,
        (
            "#072F#6P只是一小会儿的话\x01",
            "我想应该无所谓吧……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    label("loc_4AB9")


    ChrTalk(    #217
        0x101,
        (
            "#1011F#5P我和老爸都有\x01",
            "自己该走的路。\x02\x03",

            "#1012F老爸那边在努力的话，\x01",
            "我们的工作也会变得更加轻松些……\x02\x03",

            "而我们多努力一点的话，\x01",
            "我想，老爸的工作也会稍微轻松一些。\x02\x03",

            "#1006F所以现在还是不要去打扰他了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BAA")
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #218
        0x107,
        "#560F#4P姐姐……\x02",
    )

    CloseMessageWindow()

    label("loc_4BAA")


    ChrTalk(    #219
        0x102,
        "#1053F#2P这样啊……明白了。\x02",
    )

    CloseMessageWindow()

    def lambda_4BD1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4BD1)
    Sleep(100)

    def lambda_4BE4():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4BE4)
    Sleep(100)

    def lambda_4BF7():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BF7)
    Sleep(100)
    OP_8C(0xF8, 0, 400)
    Sleep(200)

    ChrTalk(    #220
        0x102,
        (
            "#1040F#4P那么我们就告辞了。\x02\x03",

            "有机会的话\x01",
            "替我们向准将问好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x9,
        (
            "#5P嗯……当然。\x02\x03",

            "我会在他吃饭的时候\x01",
            "报告的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x101,
        "#1017F#6P嗯，拜托了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x200D)
    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    # Function_15_4675 end

    def Function_16_4CA7(): pass

    label("Function_16_4CA7")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D03")

    Menu(
        0,
        10,
        100,
        0,
        (
            "【说话】\x01",                    # 0
            "【询问关于内燃机的事】\x01",      # 1
            "【离开】\x01",                    # 2
        )
    )

    Jump("loc_4D1E")

    label("loc_4D03")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【说话】\x01",      # 0
            "【离开】\x01",      # 1
        )
    )


    label("loc_4D1E")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DD2")

    ChrTalk(    #223
        0x9,
        (
            "卡西乌斯准将\x01",
            "为了重整混乱的王国军\x01",
            "正向各地发出指示。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x9,
        (
            "虽然说是紧急情况，\x01",
            "但是他那不眠不休地进行指挥的身影，\x01",
            "真可说是全军的楷模。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E69")

    label("loc_4DD2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DF4")
    Call(0, 17)
    Jump("loc_4E69")

    label("loc_4DF4")


    ChrTalk(    #225
        0x9,
        (
            "根据亲卫队传来的消息，\x01",
            "雷斯顿要塞的通讯功能\x01",
            "正在逐步恢复。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x9,
        (
            "今后如果有紧急的事情\x01",
            "就直接从协会支部联络好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E69")

    TalkEnd(0x9)
    Return()

    # Function_16_4CA7 end

    def Function_17_4E6D(): pass

    label("Function_17_4E6D")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E8D")
    Call(0, 18)
    Call(0, 20)
    FadeToBright(0, 0)

    label("loc_4E8D")

    Fade(1000)
    SetChrPos(0x101, -440, 0, -4750, 0)
    SetChrPos(0x102, 590, 0, -4750, 0)
    SetChrPos(0xF8, -840, 150, -6050, 0)
    SetChrPos(0xF9, 480, 100, -6050, 0)
    SetChrPos(0x9, 500, 0, -3240, 0)
    OP_8C(0x9, 180, 0)
    SetChrSubChip(0x9, 0)
    OP_6D(800, 0, -3520, 0)
    OP_67(0, 7630, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(45000, 0)
    OP_6E(291, 0)
    OP_0D()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #227
        (
            "\x07\x05艾丝蒂尔等人说明了情况\x01",
            "询问了关于内燃机的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #228
        0x9,
        (
            "#5P唔，虽然不清楚是什么事，\x01",
            "不过听起来好像相当重要。\x02\x03",

            "你们在这里等着。\x01",
            "我现在就去问问看。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    def lambda_4FF5():
        OP_90(0xFE, 0x0, 0x0, 0x1A90, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4FF5)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(2000)
    WaitChrThread(0x9, 0x1)
    FadeToBright(2000, 0)
    OP_8E(0x9, 0x1F4, 0x0, 0xFFFFF358, 0x7D0, 0x0)

    ChrTalk(    #229
        0x9,
        (
            "#5P我去问了负责人──\x02\x03",

            "这座要塞里好像\x01",
            "没有那个什么『内燃机』。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(70)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50DF")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_511D")

    label("loc_50DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5106")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_511D")

    label("loc_5106")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_511D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5144")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5182")

    label("loc_5144")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_516B")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5182")

    label("loc_516B")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5182")

    Sleep(1000)

    ChrTalk(    #230
        0x101,
        (
            "#1009F#6P怎、怎么可能！\x01",
            "维修长说了在这里啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x9,
        (
            "#5P我只是说『这座要塞』里没有。\x02\x03",

            "似乎刚好为了要归还给中央工房\x01",
            "而装进了一艘警备艇里。\x02\x03",

            "听说那艘警备艇因为那个异常现象\x01",
            "而紧急着陆在托兰特平原了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x101,
        "#1004F#6P啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_529C")

    ChrTalk(    #233
        0x108,
        "#070F#6P原来如此，是这么回事啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5303")

    label("loc_529C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52CD")

    ChrTalk(    #234
        0x103,
        "#027F#6P原来是这么一回事。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5303")

    label("loc_52CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5303")

    ChrTalk(    #235
        0x106,
        "#051F#6P原来如此，事情是那样的啊。\x02",
    )

    CloseMessageWindow()

    label("loc_5303")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5351")

    ChrTalk(    #236
        0x107,
        (
            "#560F#6P这么说，只要拜托\x01",
            "那艘警备艇上的士兵就可以了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_538F")

    label("loc_5351")


    ChrTalk(    #237
        0x102,
        (
            "#1040F#4P这么说，只要拜托\x01",
            "那艘警备艇的负责人就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_538F")


    ChrTalk(    #238
        0x9,
        (
            "#5P嗯，麻烦你们\x01",
            "去那边看看吧。\x02\x03",

            "警备艇应该在托兰特平原的\x01",
            "某个地方才对。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_A2(0x200E)
    OP_28(0xC2, 0x1, 0x20)
    OP_28(0xC2, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_17_4E6D end

    def Function_18_53F3(): pass

    label("Function_18_53F3")

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
        (0, "loc_546D"),
        (1, "loc_5473"),
        (SWITCH_DEFAULT, "loc_5479"),
    )


    label("loc_546D")

    OP_A2(0x1200)
    Jump("loc_5479")

    label("loc_5473")

    OP_A2(0x1201)
    Jump("loc_5479")

    label("loc_5479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5487")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_548B")

    label("loc_5487")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_548B")

    Return()

    # Function_18_53F3 end

    def Function_19_548C(): pass

    label("Function_19_548C")

    ClearMapFlags(0x1)
    OP_6D(0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_54C6")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_54E0")

    label("loc_54C6")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_54E0")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_19_548C end

    def Function_20_54F2(): pass

    label("Function_20_54F2")

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

    # Function_20_54F2 end

    def Function_21_554B(): pass

    label("Function_21_554B")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #239
        (
            "\x07\x05　　　　警告！　　　　\x01",
            "禁止在军事区域摄影\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_21_554B end

    def Function_22_55A7(): pass

    label("Function_22_55A7")

    EventBegin(0x1)

    ChrTalk(    #240
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_55D3():
        OP_6D(32020, -50, -31290, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_55D3)

    def lambda_55EB():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_55EB)

    def lambda_5603():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5603)

    def lambda_5613():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_5613)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #241
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_569A")
    OP_C0(0xE, 0x24, 0x7E71, 0xFFFFFFCE, 0xFFFF813E, 0x0, 0x7A08, 0xFFFFFE0C, 0xFFFF8AE4)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_56A9")

    label("loc_569A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56A9")
    EventEnd(0x1)

    label("loc_56A9")

    Return()

    # Function_22_55A7 end

    SaveToFile()

Try(main)
