from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4111   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '卡特莉娜夫人',                         # 9
        '达丽娅',                               # 10
        '阿温格',                               # 11
        '瑞切尔',                               # 12
        '马丁',                                 # 13
        '玛丽安',                               # 14
        '海伦娜',                               # 15
        '诺琪',                                 # 16
        '',                                     # 17
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
        'ED6_DT07/CH01220 ._CH',             # 00
        'ED6_DT07/CH01230 ._CH',             # 01
        'ED6_DT07/CH01020 ._CH',             # 02
        'ED6_DT07/CH01210 ._CH',             # 03
        'ED6_DT07/CH02490 ._CH',             # 04
        'ED6_DT07/CH01180 ._CH',             # 05
        'ED6_DT07/CH01350 ._CH',             # 06
        'ED6_DT07/CH01480 ._CH',             # 07
        'ED6_DT07/CH01220 ._CH',             # 08
        'ED6_DT07/CH01150 ._CH',             # 09
        'ED6_DT07/CH02730 ._CH',             # 0A
        'ED6_DT26/CH20687 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH01220P._CP',             # 00
        'ED6_DT07/CH01230P._CP',             # 01
        'ED6_DT07/CH01020P._CP',             # 02
        'ED6_DT07/CH01210P._CP',             # 03
        'ED6_DT07/CH02490P._CP',             # 04
        'ED6_DT07/CH01180P._CP',             # 05
        'ED6_DT07/CH01350P._CP',             # 06
        'ED6_DT07/CH01480P._CP',             # 07
        'ED6_DT07/CH01220P._CP',             # 08
        'ED6_DT07/CH01150P._CP',             # 09
        'ED6_DT07/CH02730P._CP',             # 0A
        'ED6_DT26/CH20687P._CP',             # 0B
    )

    DeclNpc(
        X                   = 6600,
        Z                   = 0,
        Y                   = -55460,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 6600,
        Z                   = 0,
        Y                   = -56390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -3550,
        Z                   = 0,
        Y                   = 68290,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -5000,
        Z                   = -100,
        Y                   = 68700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 115690,
        Z                   = 0,
        Y                   = 60750,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 113990,
        Z                   = 0,
        Y                   = -55210,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 114980,
        Z                   = 0,
        Y                   = -55400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 57440,
        Z                   = 0,
        Y                   = 2570,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )


    DeclActor(
        TriggerX            = -5000,
        TriggerZ            = 0,
        TriggerY            = 68840,
        TriggerRange        = 1000,
        ActorX              = -4840,
        ActorZ              = 1200,
        ActorY              = 68840,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_22E",          # 00, 0
        "Function_1_268",          # 01, 1
        "Function_2_286",          # 02, 2
        "Function_3_2AA",          # 03, 3
        "Function_4_2CE",          # 04, 4
        "Function_5_2F2",          # 05, 5
        "Function_6_3FC",          # 06, 6
        "Function_7_4A6",          # 07, 7
        "Function_8_557",          # 08, 8
        "Function_9_691",          # 09, 9
        "Function_10_7F5",         # 0A, 10
        "Function_11_8C9",         # 0B, 11
        "Function_12_9A4",         # 0C, 12
    )


    def Function_0_22E(): pass

    label("Function_0_22E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_267")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)

    label("loc_267")

    Return()

    # Function_0_22E end

    def Function_1_268(): pass

    label("Function_1_268")

    OP_B1("t4111_n")
    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_285")
    OP_65(0x0, 0x1)

    label("loc_285")

    Return()

    # Function_1_268 end

    def Function_2_286(): pass

    label("Function_2_286")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A9")
    OP_8D(0xFE, 113830, 62500, 117900, 58880, 2000)
    Jump("Function_2_286")

    label("loc_2A9")

    Return()

    # Function_2_286 end

    def Function_3_2AA(): pass

    label("Function_3_2AA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CD")
    OP_8D(0xFE, -1150, 59690, -3770, 62520, 3000)
    Jump("Function_3_2AA")

    label("loc_2CD")

    Return()

    # Function_3_2AA end

    def Function_4_2CE(): pass

    label("Function_4_2CE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F1")
    OP_8D(0xFE, 56680, 3500, 58350, 1840, 2000)
    Jump("Function_4_2CE")

    label("loc_2F1")

    Return()

    # Function_4_2CE end

    def Function_5_2F2(): pass

    label("Function_5_2F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_3DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_35C")

    ChrTalk(    #0
        0xFE,
        (
            "这种时候\x01",
            "可不能慌乱哦。\x02",
        )
    )

    Jump("loc_32D")

    label("loc_32D")

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "虽然对年轻人来说\x01",
            "这也是没办法的事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DA")

    label("loc_35C")


    ChrTalk(    #2
        0xFE,
        "瑞切尔快该生产了呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "那个人差不多也该\x01",
            "从哈肯大门冲回来了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "呵呵，\x01",
            "我已经迫不及待抱孙子了。\x02",
        )
    )

    Jump("loc_3D6")

    label("loc_3D6")

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_3DA")

    Jump("loc_3F8")

    label("loc_3DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_3E7")
    Jump("loc_3F8")

    label("loc_3E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_3F1")
    Jump("loc_3F8")

    label("loc_3F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_3F8")

    label("loc_3F8")

    TalkEnd(0xFE)
    Return()

    # Function_5_2F2 end

    def Function_6_3FC(): pass

    label("Function_6_3FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_487")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_44A")

    ChrTalk(    #5
        0xFE,
        "我妻子快生产了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "……现在真想待在她身边啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_484")

    label("loc_44A")

    OP_8C(0xFE, 270, 0)

    ChrTalk(    #7
        0xFE,
        "没关系，有我在。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "不用担心任何事。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_484")

    Jump("loc_4A2")

    label("loc_487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_491")
    Jump("loc_4A2")

    label("loc_491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_49B")
    Jump("loc_4A2")

    label("loc_49B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_4A2")

    label("loc_4A2")

    TalkEnd(0xFE)
    Return()

    # Function_6_3FC end

    def Function_7_4A6(): pass

    label("Function_7_4A6")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_538")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4ED")

    ChrTalk(    #9
        0x13,
        (
            "女神啊，\x01",
            "请赐予这孩子祝福吧……\x02",
        )
    )

    Jump("loc_4E9")

    label("loc_4E9")

    CloseMessageWindow()
    Jump("loc_535")

    label("loc_4ED")


    ChrTalk(    #10
        0x13,
        (
            "嗯嗯、嗯嗯……\x01",
            "我知道。\x02",
        )
    )

    Jump("loc_517")

    label("loc_517")

    CloseMessageWindow()

    ChrTalk(    #11
        0x13,
        "……一定没问题的。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_535")

    Jump("loc_553")

    label("loc_538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_542")
    Jump("loc_553")

    label("loc_542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_54C")
    Jump("loc_553")

    label("loc_54C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_553")

    label("loc_553")

    TalkEnd(0x13)
    Return()

    # Function_7_4A6 end

    def Function_8_557(): pass

    label("Function_8_557")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_672")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5D0")

    ChrTalk(    #12
        0xFE,
        "嗯……嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "啊啊，\x01",
            "什么都想不出来！\x02",
        )
    )

    Jump("loc_5A3")

    label("loc_5A3")

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "这、这种时候\x01",
            "竟然帮不上一点忙……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66F")

    label("loc_5D0")


    ChrTalk(    #15
        0xFE,
        "夫、夫人，我该做些什么呢……\x02",
    )

    CloseMessageWindow()
    OP_4A(0x10, 255)
    TurnDirection(0x10, 0xFE, 500)
    Sleep(300)

    ChrTalk(    #16
        0x10,
        "冷静点，达丽娅。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "总而言之，\x01",
            "先想想小宝宝的名字怎么样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "名、名字……吗？\x02",
    )

    CloseMessageWindow()
    OP_4B(0x10, 255)
    OP_8C(0x10, 90, 0)
    OP_A2(0x1)

    label("loc_66F")

    Jump("loc_68D")

    label("loc_672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_67C")
    Jump("loc_68D")

    label("loc_67C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_686")
    Jump("loc_68D")

    label("loc_686")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_68D")

    label("loc_68D")

    TalkEnd(0xFE)
    Return()

    # Function_8_557 end

    def Function_9_691(): pass

    label("Function_9_691")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_7D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_6E9")

    ChrTalk(    #19
        0xFE,
        "女王诞辰庆典还有５个月……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "啊啊，我该怎么办才好啊！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D3")

    label("loc_6E9")


    ChrTalk(    #21
        0xFE,
        "啊啊，我说你们！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "就没有什么\x01",
            "能让人吃惊的活动吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "对、对了。\x01",
            "就当是过生日也没关系哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x103,
        "#1640F我的已经过了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x151,
        "#1651F我的还早。\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #26
        0xFE,
        (
            "是、是吗。\x01",
            "……唉呀，真抱歉呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_7D3")

    Jump("loc_7F1")

    label("loc_7D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_7E0")
    Jump("loc_7F1")

    label("loc_7E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_7EA")
    Jump("loc_7F1")

    label("loc_7EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_7F1")

    label("loc_7F1")

    TalkEnd(0xFE)
    Return()

    # Function_9_691 end

    def Function_10_7F5(): pass

    label("Function_10_7F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_8AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_846")

    ChrTalk(    #27
        0xFE,
        (
            "那个人啊，每年到这个时期\x01",
            "都会像这样陷入半狂乱状态呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A7")

    label("loc_846")


    ChrTalk(    #28
        0xFE,
        (
            "那个人啊，\x01",
            "一没有活动参加就会坐立不安呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "是不是给他弄个\x01",
            "纪念日什么的比较好呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_8A7")

    Jump("loc_8C5")

    label("loc_8AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_8B4")
    Jump("loc_8C5")

    label("loc_8B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_8BE")
    Jump("loc_8C5")

    label("loc_8BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_8C5")

    label("loc_8C5")

    TalkEnd(0xFE)
    Return()

    # Function_10_7F5 end

    def Function_11_8C9(): pass

    label("Function_11_8C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_985")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_92C")
    OP_8C(0xFE, 0, 0)

    ChrTalk(    #30
        0xFE,
        (
            "喂，妈妈，\x01",
            "就这样放着不管没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "是不是应该\x01",
            "给点惩罚？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_982")

    label("loc_92C")


    ChrTalk(    #32
        0xFE,
        (
            "爸爸呢，\x01",
            "其实是某个大公司的重要职员哦。\x02",
        )
    )

    Jump("loc_966")

    label("loc_966")

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "虽然看起来不像。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_982")

    Jump("loc_9A0")

    label("loc_985")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_98F")
    Jump("loc_9A0")

    label("loc_98F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_999")
    Jump("loc_9A0")

    label("loc_999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_9A0")

    label("loc_9A0")

    TalkEnd(0xFE)
    Return()

    # Function_11_8C9 end

    def Function_12_9A4(): pass

    label("Function_12_9A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_A7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_A0E")

    ChrTalk(    #34
        0xFE,
        (
            "我那口子啊，\x01",
            "总是过了半夜才回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "反正就是\x01",
            "不把我当回事啦！\x02",
        )
    )

    Jump("loc_A0A")

    label("loc_A0A")

    CloseMessageWindow()
    Jump("loc_A79")

    label("loc_A0E")


    ChrTalk(    #36
        0xFE,
        (
            "我那口子啊，\x01",
            "工作时就只忙着工作不回家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "而休息日就\x01",
            "只忙着去玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "我实在无法忍受了！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_A79")

    Jump("loc_A97")

    label("loc_A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_A86")
    Jump("loc_A97")

    label("loc_A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_A90")
    Jump("loc_A97")

    label("loc_A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_A97")

    label("loc_A97")

    TalkEnd(0xFE)
    Return()

    # Function_12_9A4 end

    SaveToFile()

Try(main)
