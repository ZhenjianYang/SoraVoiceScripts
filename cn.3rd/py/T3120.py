from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3120   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T3120   ._SN',
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
        '雾香',                                 # 9
        '提妲',                                 # 10
        '艾莉卡',                               # 11
        '埃尔文',                               # 12
        '耶鲁克',                               # 13
        '艾妲',                                 # 14
        '迪迪',                                 # 15
        '王',                                   # 16
        '冈多夫',                               # 17
        '目标用照相机',                         # 18
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
        'ED6_DT07/CH02610 ._CH',             # 00
        'ED6_DT07/CH02020 ._CH',             # 01
        'ED6_DT07/CH00060 ._CH',             # 02
        'ED6_DT06/CH20020 ._CH',             # 03
        'ED6_DT07/CH00030 ._CH',             # 04
        'ED6_DT07/CH00040 ._CH',             # 05
        'ED6_DT07/CH00033 ._CH',             # 06
        'ED6_DT07/CH00043 ._CH',             # 07
        'ED6_DT07/CH02620 ._CH',             # 08
        'ED6_DT07/CH00070 ._CH',             # 09
        'ED6_DT07/CH01040 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01030 ._CH',             # 0C
        'ED6_DT07/CH01160 ._CH',             # 0D
        'ED6_DT07/CH01760 ._CH',             # 0E
        'ED6_DT07/CH00023 ._CH',             # 0F
        'ED6_DT07/CH00053 ._CH',             # 10
        'ED6_DT07/CH00063 ._CH',             # 11
        'ED6_DT07/CH00073 ._CH',             # 12
        'ED6_DT07/CH01040 ._CH',             # 13
        'ED6_DT07/CH02490 ._CH',             # 14
        'ED6_DT27/CH03970 ._CH',             # 15
        'ED6_DT06/CH20137 ._CH',             # 16
        'ED6_DT07/CH01750 ._CH',             # 17
    )

    AddCharChipPat(
        'ED6_DT07/CH02610P._CP',             # 00
        'ED6_DT07/CH02020P._CP',             # 01
        'ED6_DT07/CH00060P._CP',             # 02
        'ED6_DT06/CH20020P._CP',             # 03
        'ED6_DT07/CH00030P._CP',             # 04
        'ED6_DT07/CH00040P._CP',             # 05
        'ED6_DT07/CH00033P._CP',             # 06
        'ED6_DT07/CH00043P._CP',             # 07
        'ED6_DT07/CH02620P._CP',             # 08
        'ED6_DT07/CH00070P._CP',             # 09
        'ED6_DT07/CH01040P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01030P._CP',             # 0C
        'ED6_DT07/CH01160P._CP',             # 0D
        'ED6_DT07/CH01760P._CP',             # 0E
        'ED6_DT07/CH00023P._CP',             # 0F
        'ED6_DT07/CH00053P._CP',             # 10
        'ED6_DT07/CH00063P._CP',             # 11
        'ED6_DT07/CH00073P._CP',             # 12
        'ED6_DT07/CH01040P._CP',             # 13
        'ED6_DT07/CH02490P._CP',             # 14
        'ED6_DT27/CH03970P._CP',             # 15
        'ED6_DT06/CH20137P._CP',             # 16
        'ED6_DT07/CH01750P._CP',             # 17
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 1200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1780,
        Z                   = 1000,
        Y                   = 53000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 52970,
        Z                   = 0,
        Y                   = 2400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 52390,
        Z                   = 0,
        Y                   = 53790,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 55570,
        Z                   = 0,
        Y                   = 51740,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 25480,
        Z                   = 0,
        Y                   = -3020,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 51290,
        Z                   = 4000,
        Y                   = 410,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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


    DeclActor(
        TriggerX            = -1320,
        TriggerZ            = 0,
        TriggerY            = -4700,
        TriggerRange        = 1400,
        ActorX              = -1320,
        ActorZ              = 2000,
        ActorY              = -4700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3480,
        TriggerZ            = 0,
        TriggerY            = -710,
        TriggerRange        = 400,
        ActorX              = 3500,
        ActorZ              = 1500,
        ActorY              = 1200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1830,
        TriggerZ            = 1000,
        TriggerY            = 51000,
        TriggerRange        = 400,
        ActorX              = 1780,
        ActorZ              = 2500,
        ActorY              = 53000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53210,
        TriggerZ            = 0,
        TriggerY            = 520,
        TriggerRange        = 400,
        ActorX              = 52970,
        ActorZ              = 1500,
        ActorY              = 2400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_33A",          # 00, 0
        "Function_1_3A7",          # 01, 1
        "Function_2_3A8",          # 02, 2
        "Function_3_44F",          # 03, 3
        "Function_4_473",          # 04, 4
        "Function_5_478",          # 05, 5
        "Function_6_56D",          # 06, 6
        "Function_7_651",          # 07, 7
        "Function_8_6F4",          # 08, 8
        "Function_9_6F9",          # 09, 9
        "Function_10_85A",         # 0A, 10
        "Function_11_CE1",         # 0B, 11
        "Function_12_CE6",         # 0C, 12
        "Function_13_1294",        # 0D, 13
        "Function_14_14F1",        # 0E, 14
        "Function_15_1E55",        # 0F, 15
        "Function_16_2D22",        # 10, 16
        "Function_17_2D5E",        # 11, 17
    )


    def Function_0_33A(): pass

    label("Function_0_33A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_371")
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_371")
    SetChrFlags(0x18, 0x10)

    label("loc_371")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_393")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 15)
    Jump("loc_3A6")

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_3A6")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_3A6")

    Return()

    # Function_0_33A end

    def Function_1_3A7(): pass

    label("Function_1_3A7")

    Return()

    # Function_1_3A7 end

    def Function_2_3A8(): pass

    label("Function_2_3A8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_3D9"),
        (1, "loc_3E5"),
        (2, "loc_3F1"),
        (3, "loc_3FD"),
        (4, "loc_409"),
        (5, "loc_415"),
        (6, "loc_421"),
        (SWITCH_DEFAULT, "loc_42D"),
    )


    label("loc_3D9")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_439")

    label("loc_3E5")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_439")

    label("loc_3F1")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_439")

    label("loc_3FD")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_439")

    label("loc_409")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_439")

    label("loc_415")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_439")

    label("loc_421")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_439")

    label("loc_42D")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_439")

    label("loc_439")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_439")

    label("loc_44E")

    Return()

    # Function_2_3A8 end

    def Function_3_44F(): pass

    label("Function_3_44F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_472")
    OP_8D(0xFE, 52620, 51160, 59990, 53120, 3000)
    Jump("Function_3_44F")

    label("loc_472")

    Return()

    # Function_3_44F end

    def Function_4_473(): pass

    label("Function_4_473")

    Call(0, 5)
    Return()

    # Function_4_473 end

    def Function_5_478(): pass

    label("Function_5_478")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_569")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4EB")
    OP_8C(0x13, 180, 0)

    ChrTalk(    #0
        0x13,
        (
            "……咦，库诺那家伙\x01",
            "跑到什么地方去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x13,
        (
            "我本来还以为\x01",
            "他又在排列商品了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_569")

    label("loc_4EB")


    ChrTalk(    #2
        0x13,
        (
            "啊，你好。\x01",
            "欢迎光临贝尔杂货店！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x13,
        (
            "要是有什么困难\x01",
            "随时可以跟我说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x13,
        (
            "我的目标是\x01",
            "开个广受地方百姓欢迎的店。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_569")

    TalkEnd(0x13)
    Return()

    # Function_5_478 end

    def Function_6_56D(): pass

    label("Function_6_56D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_64D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_5A7")

    ChrTalk(    #5
        0xFE,
        "好了，下个月的进货是……这样。\x02",
    )

    CloseMessageWindow()
    Jump("loc_64D")

    label("loc_5A7")


    ChrTalk(    #6
        0xFE,
        (
            "从这个月的情况看来\x01",
            "又是日用品卖得最好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "自从城里的导力停止以来，\x01",
            "油灯之类的东西都很畅销。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "事情虽然好像已经解决了，\x01",
            "可大家似乎还是很担心呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_64D")

    TalkEnd(0xFE)
    Return()

    # Function_6_56D end

    def Function_7_651(): pass

    label("Function_7_651")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_6F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_698")

    ChrTalk(    #9
        0xFE,
        "提妲姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "明天会跟我\x01",
            "一起玩吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F0")

    label("loc_698")


    ChrTalk(    #11
        0xFE,
        (
            "最近提妲姐姐\x01",
            "都不跟我玩呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "她好像总是很忙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "………………失望。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_6F0")

    TalkEnd(0xFE)
    Return()

    # Function_7_651 end

    def Function_8_6F4(): pass

    label("Function_8_6F4")

    Call(0, 9)
    Return()

    # Function_8_6F4 end

    def Function_9_6F9(): pass

    label("Function_9_6F9")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_856")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7C2")

    ChrTalk(    #14
        0x14,
        (
            "斯坦因先生真是固执呢，\x01",
            "他绝对不肯买进最新锐的武器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x14,
        (
            "虽然新武器缺乏可靠性的说法\x01",
            "我也无法反驳……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x14,
        (
            "不过还是觉得那是很不错的产品……\x01",
            "……好吧，下次再和他商量看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_856")

    label("loc_7C2")


    ChrTalk(    #17
        0x14,
        (
            "最近帝国的莱恩福尔特公司\x01",
            "正在扩充产品线呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x14,
        (
            "要是我们也能进些\x01",
            "新式的导力炮就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x14,
        (
            "好，\x01",
            "下次跟斯坦因老板商量看看吧。\x02",
        )
    )

    Jump("loc_852")

    label("loc_852")

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_856")

    TalkEnd(0x14)
    Return()

    # Function_9_6F9 end

    def Function_10_85A(): pass

    label("Function_10_85A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_CDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 6)), scpexpr(EXPR_END)), "loc_996")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_8FC")

    ChrTalk(    #20
        0xFE,
        (
            "这么说来，\x01",
            "我在利贝尔做游击士也很久了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "丹和卡西乌斯先生\x01",
            "早就辞退工作了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "嗯？　难不成\x01",
            "我是资历最老的了……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_993")

    label("loc_8FC")


    ChrTalk(    #23
        0xFE,
        "发掘新人吗…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "这么说来，\x01",
            "你也是被卡西乌斯先生\x01",
            "发掘出来的吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x106,
        (
            "#555F啰、啰嗦。\x02\x03",

            "以前的事\x01",
            "就不要拿出来说了。\x02",
        )
    )

    Jump("loc_98F")

    label("loc_98F")

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_993")

    Jump("loc_CDD")

    label("loc_996")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    ChrTalk(    #26
        0xFE,
        "嗯………………？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 500)
    Sleep(300)

    ChrTalk(    #27
        0xFE,
        "哟，这不是阿加特吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x106,
        (
            "#051F冈多夫……\x02\x03",

            "真稀奇，\x01",
            "你居然会来武器店啊。\x02",
        )
    )

    Jump("loc_A30")

    label("loc_A30")

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "哈哈，\x01",
            "我要乘下一班定期船出门……\x02",
        )
    )

    Jump("loc_A62")

    label("loc_A62")

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "不过船好像晚点了，\x01",
            "空出了些时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x106,
        (
            "#051F哦……\x01",
            "看来你还是这么忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "没克鲁茨那么忙啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "不过继艾丝蒂尔、约修亚之后，\x01",
            "连雾香也要走了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "哎呀呀，\x01",
            "又要为人手不足发愁了呢。\x02",
        )
    )

    Jump("loc_B39")

    label("loc_B39")

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F1, 0)), scpexpr(EXPR_END)), "loc_B95")

    ChrTalk(    #35
        0x106,
        (
            "#051F不过，\x01",
            "人手不足也是常有的事了。\x02\x03",

            "在新人加入之前\x01",
            "彼此都忍耐一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C13")

    label("loc_B95")


    ChrTalk(    #36
        0x106,
        (
            "#552F啊啊，\x01",
            "雾香那家伙\x01",
            "果然也要走了吗……\x02\x03",

            "#051F不过，\x01",
            "人手不足也是常有的事了。\x02\x03",

            "在新人加入之前\x01",
            "彼此都忍耐一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C13")

    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #37
        0xFE,
        "怎么了，阿加特……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "听你说话的口气，\x01",
            "好像有什么门路啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x106,
        (
            "#556F哼…………\x01",
            "倒不算什么门路啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "嘿嘿，是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "怎样都好，\x01",
            "等你的好消息啦。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x18, 0x10)
    OP_A2(0x2F86)

    label("loc_CDD")

    TalkEnd(0xFE)
    Return()

    # Function_10_85A end

    def Function_11_CE1(): pass

    label("Function_11_CE1")

    Call(0, 12)
    Return()

    # Function_11_CE1 end

    def Function_12_CE6(): pass

    label("Function_12_CE6")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_1290")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F1, 1)), scpexpr(EXPR_END)), "loc_DF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_D64")

    ChrTalk(    #42
        0x10,
        (
            "#790F阿加特，\x01",
            "着急的话就去中央工房吧。\x02\x03",

            "有空的话就顺便\x01",
            "解决一下公告板上的委托。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DEE")

    label("loc_D64")


    ChrTalk(    #43
        0x10,
        (
            "#790F阿加特，\x01",
            "着急的话就去中央工房吧。\x02\x03",

            "有空的话就顺便\x01",
            "解决一下公告板上的委托。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x106,
        "#050F哦、哦………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_DEE")

    Jump("loc_1290")

    label("loc_DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F1, 0)), scpexpr(EXPR_END)), "loc_FC8")

    ChrTalk(    #45
        0x10,
        (
            "#792F………………阿加特，\x01",
            "拜托你一件事可以吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x106,
        (
            "#052F哦，哦…………\x02\x03",

            "#051F……好啊，\x01",
            "只要是我能做的事，\x01",
            "就随便说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        (
            "#790F希望你能多来蔡斯照顾一下，\x01",
            "就算偶尔来几次也行。\x02\x03",

            "反正你有空吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x106,
        (
            "#551F没空啦。\x02\x03",

            "#051F不过………………\x01",
            "这点小事我能做到的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        (
            "#791F……谢谢你。\x02\x03",

            "我也把你的事\x01",
            "告诉接任的孩子了。\x02\x03",

            "要和她好好相处哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x106,
        (
            "#051F呵，\x01",
            "安排还是那么周到嘛。\x02",
        )
    )

    Jump("loc_FC1")

    label("loc_FC1")

    CloseMessageWindow()
    OP_A2(0x2F89)
    Jump("loc_1290")

    label("loc_FC8")

    EventBegin(0x0)
    Fade(500)
    OP_4A(0x10, 255)
    SetChrPos(0x106, 3750, 0, -700, 0)
    OP_6D(2910, 0, 1060, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #51
        0x10,
        (
            "#790F#11P哎呀，阿加特。\x01",
            "你不是要赶去工房吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x106,
        (
            "#052F#6P没事，做完准备马上就出发。话说回来……\x02\x03",

            "听说你辞掉协会工作，\x01",
            "要回国去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10,
        (
            "#792F#11P………………嗯嗯。\x02\x03",

            "#791F很早以前就决定了，\x01",
            "不过工作交接拖延了点时间。\x02\x03",

            "下个月初就会出发。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #54
        0x106,
        (
            "#053F#6P…………是吗。\x02\x03",

            "#051F以前也多次\x01",
            "承蒙你照顾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        (
            "#794F#11P……是啊。\x02\x03",

            "#792F阿加特，\x01",
            "可别再中毒倒下了啊。\x02\x03",

            "免得吓着接任的孩子。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #56
        0x106,
        (
            "#055F#6P又、又不是\x01",
            "我愿意倒下的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        "#791F#11P呵呵……………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F88)
    OP_4B(0x10, 255)
    EventEnd(0x0)

    label("loc_1290")

    TalkEnd(0x10)
    Return()

    # Function_12_CE6 end

    def Function_13_1294(): pass

    label("Function_13_1294")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_14ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F1, 2)), scpexpr(EXPR_END)), "loc_13BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1320")

    ChrTalk(    #58
        0xFE,
        (
            "哎呀，\x01",
            "接下来得赶紧\x01",
            "去亚尔摩温泉才行。\x02",
        )
    )

    Jump("loc_12E2")

    label("loc_12E2")

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "继续闲扯下去，\x01",
            "又要被雾香小姐\x01",
            "训斥了。\x02",
        )
    )

    Jump("loc_131C")

    label("loc_131C")

    CloseMessageWindow()
    Jump("loc_13B7")

    label("loc_1320")


    ChrTalk(    #60
        0xFE,
        (
            "听冈多夫先生说，\x01",
            "艾莉卡博士的丈夫\x01",
            "原来好像是游击士呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "而且据说\x01",
            "还相当厉害。\x02",
        )
    )

    Jump("loc_1386")

    label("loc_1386")

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "唔，\x01",
            "感觉真是一对奇怪的夫妇啊。\x02",
        )
    )

    Jump("loc_13B3")

    label("loc_13B3")

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_13B7")

    Jump("loc_14ED")

    label("loc_13BA")


    ChrTalk(    #63
        0xFE,
        (
            "啊……\x01",
            "这不是阿加特先生吗。\x02",
        )
    )

    Jump("loc_13E5")

    label("loc_13E5")

    CloseMessageWindow()

    ChrTalk(    #64
        0x106,
        "#051F哟，王，情况怎么样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "哎呀，这个嘛……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "阿加特先生，\x01",
            "你知道艾莉卡博士吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "据说是能与那个拉赛尔博士\x01",
            "相匹敌的破坏魔鬼……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "不知道是不是因为这个，\x01",
            "委托增加了好多啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #69
        0x106,
        "#053F…………是吗……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F8A)

    label("loc_14ED")

    TalkEnd(0xFE)
    Return()

    # Function_13_1294 end

    def Function_14_14F1(): pass

    label("Function_14_14F1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-960, 0, -2500, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x106, 1000, 0, -5800, 0)
    SetChrChipByIndex(0x106, 22)
    SetChrSubChip(0x106, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 1000, 0, -1260, 0)
    OP_4A(0x10, 255)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS369._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS368._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS368._CH")
    OP_C6(0x0, 0x0, -315000, -250000, 0)
    OP_C6(0x0, 0x1, 2000, 2000, 0)
    OP_C6(0x1, 0x0, -463000, -368000, 0)
    OP_C6(0x1, 0x1, 2500, 2500, 0)
    OP_C6(0x2, 0x0, -370000, -368000, 0)
    OP_C6(0x2, 0x1, 2500, 2500, 0)
    Sleep(500)
    OP_1F(0x0, 0x1F4)
    OP_C6(0x1, 0x3, -1, 100, 0)
    OP_C6(0x2, 0x3, -1, 100, 0)
    OP_22(0x80, 0x0, 0x64)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    OP_C6(0x0, 0x3, -1, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    Sleep(300)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(    #70
        "\x07\x00#052F什…………！？\x02",
    )

    Jump("loc_16FA")

    label("loc_16FA")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0xD5, 0x0, 0x64)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x1, 0xFF, 0x0)

    ChrTalk(    #71
        0x106,
        (
            "#057F#6P………………………………？\x02\x03",

            "（刚才好像感觉到\x01",
            "  很强的杀气……）\x02\x03",

            "#552F（话虽如此，\x01",
            "  只不过是工房的研究人员来委托而已……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #72
        0x106,
        "#050F#6P（……是我的错觉吗………）\x02",
    )

    CloseMessageWindow()
    OP_1F(0x64, 0x7D0)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 65535)
    SetChrSubChip(0x106, 0)
    Sleep(1000)

    NpcTalk(    #73
        0x12,
        "女性研究人员",
        "#5P哎呀，怎么回事呢……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 180, 500)
    Sleep(300)

    NpcTalk(    #74
        0x12,
        "女性研究人员",
        (
            "#1458F#11P那边的红毛小子\x01",
            "不就是阿加特·科洛斯纳吗。\x02\x03",

            "#1833F呼呼呼，可怜的人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x106,
        "#057F#6P…………啊？\x02",
    )

    CloseMessageWindow()

    def lambda_190B():
        OP_8E(0xFE, 0x3E8, 0x0, 0xFFFFF448, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_190B)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    NpcTalk(    #76
        0x12,
        "女性研究人员",
        (
            "#1833F#11P在即将受刑的时候\x01",
            "还能这么悠闲呢。\x02\x03",

            "这倒正好…………\x01",
            "我就直接告诉你吧。\x02\x03",

            "#1831F其实啊，\x01",
            "我准备了非常适合你的葬身之地哦。\x02\x03",

            "来来，到中央工房来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x106,
        (
            "#555F#6P你是谁啊……\x01",
            "要找我打架吗？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #78
        0x12,
        "女性研究人员",
        (
            "#1457F#11P才不是打架呢。\x02\x03",

            "#1456F……这是委托。\x02\x03",

            "交给游击士\x01",
            "阿加特·科洛斯纳的委托。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x106,
        (
            "#057F#6P哪有这么\x01",
            "莫名其妙的委托啊。\x02\x03",

            "#057F想要委托我，\x01",
            "就赶快找点\x01",
            "正经工作来吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #80
        0x12,
        "女性研究人员",
        (
            "#1833F#11P……唉，真伤脑筋，\x01",
            "这么不知好歹。\x02\x03",

            "#1835F#3S#30W……自己的罪孽，\x01",
            "总要有点自觉吧……！#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #81
        0x106,
        (
            "#055F#6P（这、这家伙搞什么啊……？）\x02\x03",

            "（眼神也不正常……）\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #82
        0x12,
        "女性研究人员",
        (
            "#1457F#11P…………明白没？\x01",
            "赶紧挖挖耳朵给我好好听着。\x02\x03",

            "#1452F这项委托的内容，\x01",
            "就是要拿导力装甲和你作比较，\x01",
            "进行机体性能的检查。\x02\x03",

            "……也就是说，\x01",
            "你要为改良导力装甲作贡献！\x02\x03",

            "#1458F呼呼，这样一来你的罪孽也就……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x106,
        (
            "#551F#6P……说什么\x01",
            "乱七八糟的…………\x02\x03",

            "#555F……你听着，所谓委托，\x01",
            "是要拿出真正有困难的事情。\x02\x03",

            "……游击士又不是便利店。\x02\x03",

            "我没工夫\x01",
            "听你的冷嘲热讽。\x02",
        )
    )

    Jump("loc_1DA7")

    label("loc_1DA7")

    CloseMessageWindow()

    NpcTalk(    #84
        0x12,
        "女性研究人员",
        (
            "#1458F#11P……………………\x02\x03",

            "嘻嘻…………\x02\x03",

            "#1833F哎呀哎呀，你害怕了～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x106,
        "#057F#6P…………………啊？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T3100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_14F1 end

    def Function_15_1E55(): pass

    label("Function_15_1E55")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-960, 0, -2500, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x106, 0, 0, -4000, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 0, 0, -2500, 180)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 2000, -500, -8000, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4A(0x10, 255)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #86
        0x106,
        (
            "#054F#6P既然这么\x01",
            "想找人帮忙……！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)

    def lambda_1F2D():
        OP_6D(40, 0, -3500, 1500)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_1F2D)

    def lambda_1F45():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1F45)

    def lambda_1F57():
        OP_8E(0xFE, 0x7D0, 0x0, 0xFFFFE890, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1F57)
    WaitChrThread(0x11, 0x1)
    OP_22(0x7, 0x0, 0x64)
    OP_8C(0x11, 315, 500)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    def lambda_1FBB():
        TurnDirection(0xFE, 0x11, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1FBB)
    Sleep(100)
    TurnDirection(0x12, 0x11, 500)
    Sleep(300)

    ChrTalk(    #87
        0x106,
        "#052F#5P提妲…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x11,
        "#064F#6P阿、阿加特大哥哥……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89 op#A op#5
        0x11,
        "#064F#6P#10A还有妈妈……　　　　\x05\x02",
    )


    def lambda_2057():
        OP_8E(0xFE, 0x618, 0x0, 0xFFFFF04D, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2057)
    WaitChrThread(0x12, 0x1)

    def lambda_2077():
        OP_8E(0xFE, 0x618, 0x0, 0xFFFFEA48, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2077)
    WaitChrThread(0x12, 0x1)
    TurnDirection(0x12, 0x106, 600)
    Sleep(300)
    CloseMessageWindow()

    NpcTalk(    #90
        0x12,
        "女性研究人员",
        (
            "#1458F#6P对了对了……\x01",
            "还有一点得事先声明……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #91
        0x12,
        "女性研究人员",
        (
            "#1830F#6P#3S不准靠近\x01",
            "我家提妲半径１塞尔矩以内！！\x02",
        )
    )

    OP_7C(0x0, 0x15E, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    NpcTalk(    #92
        0x12,
        "女性研究人员",
        (
            "#1830F#6P……明白了吗，\x01",
            "你这个不知天高地厚的家伙！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x106,
        "#052F#5P我、我说……\x02",
    )

    CloseMessageWindow()

    def lambda_21BF():
        OP_8C(0x12, 135, 800)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_21BF)

    NpcTalk(    #94
        0x12,
        "女性研究人员",
        "#5P咻…………！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x2)

    NpcTalk(    #95 op#A
        0x12,
        "女性研究人员",
        "#8A#11P咻咻…………！！\x02",
    )

    Sleep(200)

    def lambda_2230():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2230)

    def lambda_2242():
        OP_8E(0xFE, 0x618, 0xFFFFFE0C, 0xFFFFE0C0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2242)

    def lambda_225D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_225D)

    def lambda_226F():
        OP_8F(0xFE, 0x7D0, 0xFFFFFE0C, 0xFFFFE0C0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_226F)
    WaitChrThread(0x12, 0x1)
    WaitChrThread(0x11, 0x1)
    OP_22(0x7, 0x0, 0x64)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_22AB():
        OP_8C(0xFE, 180, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_22AB)

    ChrTalk(    #96
        0x106,
        "#055F#11P喂、喂…………！？\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #97
        0x106,
        (
            "#555F#11P……怎么回事，那家伙……？\x02\x03",

            "而且还把\x01",
            "提妲带走了……\x02",
        )
    )

    Jump("loc_233B")

    label("loc_233B")

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #98
        0x106,
        (
            "#057F#11P该不是要把\x01",
            "那小不点拐到什么\x01",
            "危险的地方去吧……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x10,
        "#792F这个不必担心。\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_23E5():
        OP_8C(0xFE, 45, 500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_23E5)

    def lambda_23F3():
        OP_6D(2460, 0, 1800, 2400)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_23F3)

    def lambda_240B():
        OP_6C(322000, 2400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_240B)
    WaitChrThread(0x19, 0x0)

    ChrTalk(    #100
        0x106,
        "#052F#4P……雾香，你在啊。\x02",
    )

    CloseMessageWindow()

    def lambda_2447():
        OP_8E(0xFE, 0xE4C, 0x0, 0xFFFFFBDC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2447)
    WaitChrThread(0x106, 0x1)
    TurnDirection(0x106, 0x10, 500)
    Sleep(300)

    ChrTalk(    #101
        0x10,
        (
            "#791F#11P她是艾莉卡·拉赛尔。\x01",
            "是提妲的母亲啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x106,
        (
            "#052F#6P……母亲………？\x02\x03",

            "#40W……那家伙，是提妲的？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #103
        0x106,
        "#055F#4S#6P啊…………！？#2S\x02",
    )

    OP_7C(0x0, 0x190, 0xBB8, 0x96)
    CloseMessageWindow()

    ChrTalk(    #104
        0x10,
        (
            "#792F#11P大概是两周前吧，\x01",
            "那孩子的父母回国了。\x02\x03",

            "丹·拉赛尔\x01",
            "和艾莉卡·拉赛尔博士。\x02\x03",

            "#791F……虽然听说发生了一些骚乱，\x01",
            "不过这是铁定的事实。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x106,
        "#555F#6P那、那种家伙……？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x106, 180, 500)
    Sleep(300)
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)

    ChrTalk(    #106
        0x10,
        (
            "#791F#11P……虽然你好像正忙着，\x01",
            "不过还是来交代一下工作的事情吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106)
    Sleep(200)
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x106, 0, 600)
    Sleep(300)

    ChrTalk(    #107
        0x106,
        (
            "#052F#6P哦，哦…………\x02\x03",

            "#051F傍晚之前都有空，\x01",
            "小委托倒是可以做几个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x10,
        (
            "#792F#11P…………那么首先，\x01",
            "是中央工房的委托。\x02\x03",

            "协助新兵器『导力装甲』\x01",
            "试作机进行各种实验。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x106,
        (
            "#052F#6P导力装……甲……？\x02\x03",

            "#555F……喂，给我慢着。\x01",
            "这个委托……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x10,
        (
            "#791F#11P艾莉卡博士的委托，\x01",
            "已经作为正式工作受理了。\x02\x03",

            "阿加特，指名你去做哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x106,
        (
            "#552F#6P……啧，那女人……\x02\x03",

            "居然真的\x01",
            "提出委托了吗……\x02",
        )
    )

    Jump("loc_2879")

    label("loc_2879")

    CloseMessageWindow()

    ChrTalk(    #112
        0x10,
        (
            "#792F#11P关于导力装甲\x01",
            "我也不知道详细情况。\x02\x03",

            "根据艾莉卡博士的说明来看，\x01",
            "应该是集结了利贝尔\x01",
            "所有导力技术精华的新兵器。\x02\x03",

            "开发似乎是由\x01",
            "拉赛尔家全员进行。\x02\x03",

            "#790F地点看来就是中央工房。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x106,
        "#052F#6P……新兵器…………？\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #114
        0x106,
        (
            "#053F#6P喂，\x01",
            "你刚才说由拉赛尔家全员进行……？\x02\x03",

            "#057F难不成……\x01",
            "连提妲\x01",
            "也算进去了吗？\x02",
        )
    )

    Jump("loc_2A06")

    label("loc_2A06")

    CloseMessageWindow()

    ChrTalk(    #115
        0x10,
        (
            "#792F#11P……这个，\x01",
            "我就没问得那么仔细了。\x02\x03",

            "#791F那孩子差不多也该结束见习，\x01",
            "成为正式技师了，\x01",
            "所以这种可能性很高。\x02\x03",

            "阿加特，有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x106,
        (
            "#552F#6P…………………不…………\x02\x03",

            "#551F（那家伙的双亲\x01",
            "  只是从提妲那里\x01",
            "  听过一点传闻而已……）\x02\x03",

            "（这跟说的完全不一样嘛。\x01",
            "  而且还好像有欺骗成分……）\x02\x03",

            "…………………………………………\x02\x03",

            "#057F（但是，要是那女人\x01",
            "  竟敢把提妲卷入\x01",
            "  新兵器的开发……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(500)

    ChrTalk(    #117
        0x106,
        (
            "#050F#6P……雾香。\x01",
            "这个委托，暂时中止吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x10,
        "#790F#11P保留……你是这个意思吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x106,
        (
            "#053F#6P………………没错。\x02\x03",

            "#057F……我去确认一下情况。\x01",
            "可别随便交给别人啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x106, 0x3, 0x0, 0x10)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitChrThread(0x106, 0x3)
    OP_A2(0x2F85)
    OP_C2(0x1, 0x1F)
    OP_41(0x5, 0x0, 0xFF)
    OP_31(0x5, 0x10, 0x5A)
    OP_31(0x5, 0x5, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_35(0x5, 0xFFFF)
    OP_34(0x5, 0xFFFF)
    OP_35(0x5, 0x0)
    OP_BB(0x5, 0x6, 0x101)
    OP_37(0x5, 0x7F, 0x0)
    OP_37(0x5, 0x7F, 0x2)
    OP_41(0x5, 0x3E8, 0xFF)
    OP_34(0x5, 0x82)
    OP_34(0x5, 0x83)
    OP_34(0x5, 0x57)
    OP_34(0x5, 0x1E)
    OP_34(0x5, 0xA)
    NewScene("ED6_DT21/T3100   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1E55 end

    def Function_16_2D22(): pass

    label("Function_16_2D22")

    OP_8C(0x106, 180, 600)

    def lambda_2D2F():
        OP_8E(0xFE, 0x6CC, 0x0, 0xFFFFE0C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2D2F)
    Sleep(1300)
    OP_22(0x6, 0x0, 0x64)
    Sleep(800)
    OP_22(0x7, 0x0, 0x64)
    Sleep(1000)
    Return()

    # Function_16_2D22 end

    def Function_17_2D5E(): pass

    label("Function_17_2D5E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2DD7")

    ChrTalk(    #120
        0x106,
        (
            "#057F……现在确认\x01",
            "提妲是不是真的被卷进去了\x01",
            "才是当务之急。\x02\x03",

            "要赶快去中央工房……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E55")

    label("loc_2DD7")


    ChrTalk(    #121
        0x106,
        (
            "#555F啧，委托还挺多的呢。 \x02\x03",

            "#053F…………也罢。\x01",
            "看来没什么很紧急的委托……\x02\x03",

            "现在先去中央工房吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_2E55")

    TalkEnd(0xFF)

    label("loc_2E58")

    Return()

    # Function_17_2D5E end

    SaveToFile()

Try(main)
