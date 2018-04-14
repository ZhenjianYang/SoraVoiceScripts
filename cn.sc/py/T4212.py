from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4212   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4212.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        '达扬',                                 # 9
        '托克斯',                               # 10
        '赫穆特',                               # 11
        '杜南公爵',                             # 12
        '菲利普',                               # 13
        '王都市民',                             # 14
        '王都市民',                             # 15
        '王都市民',                             # 16
        '沃尔特议员',                           # 17
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
        'ED6_DT07/CH01570 ._CH',             # 00
        'ED6_DT07/CH01560 ._CH',             # 01
        'ED6_DT07/CH01220 ._CH',             # 02
        'ED6_DT07/CH02140 ._CH',             # 03
        'ED6_DT07/CH02470 ._CH',             # 04
        'ED6_DT07/CH01120 ._CH',             # 05
        'ED6_DT07/CH01020 ._CH',             # 06
        'ED6_DT07/CH01200 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01570P._CP',             # 00
        'ED6_DT07/CH01560P._CP',             # 01
        'ED6_DT07/CH01220P._CP',             # 02
        'ED6_DT07/CH02140P._CP',             # 03
        'ED6_DT07/CH02470P._CP',             # 04
        'ED6_DT07/CH01120P._CP',             # 05
        'ED6_DT07/CH01020P._CP',             # 06
        'ED6_DT07/CH01200P._CP',             # 07
    )

    DeclNpc(
        X                   = -68100,
        Z                   = 0,
        Y                   = -32320,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x111,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = -65500,
        Z                   = 0,
        Y                   = -41540,
        Direction           = 279,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -61160,
        Z                   = 0,
        Y                   = -35270,
        Direction           = 86,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -62490,
        Z                   = 0,
        Y                   = -31190,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -62170,
        Z                   = 0,
        Y                   = -33200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -63350,
        Z                   = 0,
        Y                   = -33470,
        Direction           = 21,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -65060,
        Z                   = 0,
        Y                   = -31070,
        Direction           = 73,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -64550,
        Z                   = 0,
        Y                   = -32810,
        Direction           = 48,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -65099,
        Z                   = 0,
        Y                   = -44670,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )


    ScpFunction(
        "Function_0_20A",          # 00, 0
        "Function_1_2D6",          # 01, 1
        "Function_2_2FC",          # 02, 2
        "Function_3_516",          # 03, 3
        "Function_4_6BF",          # 04, 4
        "Function_5_758",          # 05, 5
        "Function_6_9B5",          # 06, 6
        "Function_7_D64",          # 07, 7
        "Function_8_DC6",          # 08, 8
        "Function_9_E20",          # 09, 9
        "Function_10_E59",         # 0A, 10
        "Function_11_ED6",         # 0B, 11
    )


    def Function_0_20A(): pass

    label("Function_0_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_22D")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_2B2")

    label("loc_22D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_292")
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xB, -62830, 0, -30860, 220)
    ClearChrFlags(0xB, 0x10)
    SetChrPos(0xC, -61160, 0, -34980, 335)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0x9, -65500, 0, -43300, 165)
    SetChrFlags(0x9, 0x10)
    Jump("loc_2B2")

    label("loc_292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2A1")
    SetChrFlags(0xA, 0x80)
    Jump("loc_2B2")

    label("loc_2A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2B2")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)

    label("loc_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D5")
    SetMapFlags(0x10000000)
    Event(0, 11)

    label("loc_2D5")

    Return()

    # Function_0_20A end

    def Function_1_2D6(): pass

    label("Function_1_2D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F2")
    OP_B1("t4212_y")
    Jump("loc_2FB")

    label("loc_2F2")

    OP_B1("t4212_n")

    label("loc_2FB")

    Return()

    # Function_1_2D6 end

    def Function_2_2FC(): pass

    label("Function_2_2FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3B9")

    ChrTalk(    #0
        0xFE,
        (
            "因为导力器完全不能用了，\x01",
            "来申诉的市民很多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "公爵不在的话还真会\x01",
            "有一点点忙不过来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "话虽如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "导力器停止之后\x01",
            "要估算经济损失的话光是王都\x01",
            "就相当严重了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_512")

    label("loc_3B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_466")

    ChrTalk(    #4
        0xFE,
        (
            "呼，被改动的\x01",
            "预算谜团终于解开了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "看来似乎消失了的预算\x01",
            "是用作奥尔杰尤的开发了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "政变时那东西如果完成的话\x01",
            "会变成怎样呢？。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "……真让人有点后怕。\x02",
    )

    CloseMessageWindow()
    Jump("loc_512")

    label("loc_466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_512")

    ChrTalk(    #8
        0xFE,
        (
            "政变的善后处理\x01",
            "看来还得持续一阵子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "现在在调查情报部过去的\x01",
            "预算和实际的经费。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "看看这个就知道预算有\x01",
            "被大幅度改动的痕迹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "这笔钱消失去了哪里呢……\x02",
    )

    CloseMessageWindow()

    label("loc_512")

    TalkEnd(0xFE)
    Return()

    # Function_2_2FC end

    def Function_3_516(): pass

    label("Function_3_516")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5AA")

    ChrTalk(    #12
        0xFE,
        (
            "我都说了，导力停止的\x01",
            "原因现在还在调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "艾莉茜雅女王也很忙，\x01",
            "现在不能马上见你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "如果我们有什么发现\x01",
            "会联络大使馆的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BB")

    label("loc_5AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_623")

    ChrTalk(    #15
        0xFE,
        (
            "凯诺娜上尉被捕\x01",
            "是件好事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "不过这次为了修理港湾设施，\x01",
            "还要追加预算。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "唔，拜托，\x01",
            "别再有下次了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BB")

    label("loc_623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_6BB")

    ChrTalk(    #18
        0xFE,
        (
            "业务倒是逐渐地在正常化，\x01",
            "不过还是很忙啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "市民们对政变\x01",
            "提的问题也还很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "我负责做出各种各样的补偿，\x01",
            "不过总之问题还是堆积如山。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BB")

    TalkEnd(0xFE)
    Return()

    # Function_3_516 end

    def Function_4_6BF(): pass

    label("Function_4_6BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_754")

    ChrTalk(    #21
        0xFE,
        (
            "唉，我老婆这时候\x01",
            "大概在热衷于钓鱼吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "这样下去别说男的尊严了，\x01",
            "连丈夫的位置都危险了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "好，悄悄特训一下，\x01",
            "一定要赶上老婆。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_754")

    TalkEnd(0xFE)
    Return()

    # Function_4_6BF end

    def Function_5_758(): pass

    label("Function_5_758")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_874")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F9")

    ChrTalk(    #24
        0xB,
        (
            "#223F你们是……\x02\x03",

            "#220F要见陛下和科洛蒂娅\x01",
            "现在应该还不行。\x02\x03",

            "想知道详细原因\x01",
            "可以去问希尔丹夫人。\x02\x03",

            "抱歉，我从早到晚\x01",
            "都要应对请愿团……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_871")

    label("loc_7F9")


    ChrTalk(    #25
        0xB,
        (
            "#220F要见陛下和科洛蒂娅\x01",
            "现在应该还不行。\x02\x03",

            "想知道详细原因\x01",
            "可以去问希尔丹夫人。\x02\x03",

            "抱歉，我从早到晚\x01",
            "都要应对请愿团……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_871")

    Jump("loc_9B1")

    label("loc_874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_9B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96C")

    ChrTalk(    #26
        0xB,
        (
            "#222F唔……\x02\x03",

            "那些不明\x01",
            "身份的人在进出\x01",
            "利贝尔吗……\x02\x03",

            "…………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1011F（哟，一副平时见不到的认真表情呢。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x105,
        (
            "#040F（因为这次的事件，叔叔\x01",
            "　好像深刻地认识到结社的存在。）\x02\x03",

            "（可能叔叔他也有\x01",
            "　自己的想法呢。)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1669)
    Jump("loc_9B1")

    label("loc_96C")


    ChrTalk(    #29
        0xB,
        (
            "#222F那些不明\x01",
            "身份的人在进出\x01",
            "利贝尔吗……\x02\x03",

            "…………………………\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B1")

    TalkEnd(0xFE)
    Return()

    # Function_5_758 end

    def Function_6_9B5(): pass

    label("Function_6_9B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B35")

    ChrTalk(    #30
        0xFE,
        (
            "#721F哟，这不是\x01",
            "艾丝蒂尔小姐和约修亚先生吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        (
            "#1040F菲利普先生，\x01",
            "实在久疏问候。\x02\x03",

            "是诞辰庆典之后到现在了吧……\x01",
            "您的身体还是如此安康，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "#720F嗯，承蒙你们的关心。\x02\x03",

            "约修亚先生不在时，\x01",
            "我和大人都受到了\x01",
            "艾丝蒂尔小姐的关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        "#1044F艾丝蒂尔……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1008F说得我都不好意思了，我可\x01",
            "没做什么了不起的事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        "#1040F…………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20F1)
    Jump("loc_B6B")

    label("loc_B35")


    ChrTalk(    #36
        0xFE,
        (
            "#720F大人这次终于\x01",
            "有了干劲。\x02\x03",

            "希望能持续下去……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B6B")

    Jump("loc_D60")

    label("loc_B6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D30")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #37
        0xFE,
        "#720F哟，这不是艾丝蒂尔小姐吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#1000F菲利普先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "#720F非常感谢您上次\x01",
            "搭救大人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1018F我还要感谢菲利普先生\x01",
            "您照顾了大家呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "#722F不敢当，\x02\x03",

            "我只能以那种方式帮助你们，\x01",
            "真是太惭愧了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1015F可我们也是因为\x01",
            "有菲利普先生在\x01",
            "才能安心地去了港口……\x02\x03",

            "#1001F从这层意义上来说，\x01",
            "能搭救公爵是托了\x01",
            "菲利普先生的福。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "#721F艾丝蒂尔小姐……\x01",
            "您太抬举我了……\x02\x03",

            "#720F希望趁此机会\x01",
            "大人能够改变行事作风……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x166A)
    Jump("loc_D60")

    label("loc_D30")


    ChrTalk(    #44
        0xFE,
        (
            "#720F希望趁此机会\x01",
            "大人能够改变行事作风……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D60")

    TalkEnd(0xFE)
    Return()

    # Function_6_9B5 end

    def Function_7_D64(): pass

    label("Function_7_D64")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_DC2")

    ChrTalk(    #45
        0xFE,
        (
            "看来杜南公爵远比我们想象中的\x01",
            "了不起呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "不过发型却和传闻一样\x01",
            "果然是很……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC2")

    TalkEnd(0xFE)
    Return()

    # Function_7_D64 end

    def Function_8_DC6(): pass

    label("Function_8_DC6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E1C")

    ChrTalk(    #47
        0xFE,
        (
            "我得知王室\x01",
            "也在那么拼命应对之后\x01",
            "就放心多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "我们也得继续加油了。\x02",
    )

    CloseMessageWindow()

    label("loc_E1C")

    TalkEnd(0xFE)
    Return()

    # Function_8_DC6 end

    def Function_9_E20(): pass

    label("Function_9_E20")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E55")

    ChrTalk(    #49
        0xFE,
        (
            "原来如此，女王陛下也\x01",
            "考虑得很周到呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E55")

    TalkEnd(0xFE)
    Return()

    # Function_9_E20 end

    def Function_10_E59(): pass

    label("Function_10_E59")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_ED2")

    ChrTalk(    #50
        0xFE,
        (
            "我、我是共和国议会\x01",
            "议员沃尔特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "做、做好必要的准备\x01",
            "总没错吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "我到底什么时候\x01",
            "能和本国取得联系？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED2")

    TalkEnd(0xFE)
    Return()

    # Function_10_E59 end

    def Function_11_ED6(): pass

    label("Function_11_ED6")

    EventBegin(0x0)
    OP_6D(-62620, 0, -30760, 0)
    OP_67(0, 5140, -10000, 0)
    OP_6B(2970, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -62430, 0, -40080, 0)
    SetChrPos(0x102, -63520, 0, -40530, 0)
    SetChrPos(0xF8, -61650, 0, -40780, 0)
    SetChrPos(0xF9, -62780, 0, -41900, 0)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #53
        0xD,
        (
            "导力停止之后，\x01",
            "夜晚又冷又暗，\x01",
            "做饭也不方便……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xF,
        (
            "总之每天\x01",
            "都很不安！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xE,
        (
            "王室今后究竟\x01",
            "怎么做呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xB,
        (
            "#225F#5P啊～咳……\x02\x03",

            "#222F关于导力停止现象，\x01",
            "正在以王国军为中心进行调查。\x02\x03",

            "详细情况\x01",
            "目前还不清楚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xF,
        "太不负责任了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xB,
        (
            "#222F#5P算了，冷静点。\x01",
            "确实还有很多事是不明原因的……\x02\x03",

            "正因为如此，女王希望\x01",
            "我们和市民全力配合，\x01",
            "尽到最大的努力。\x02\x03",

            "#225F比如东街区的历史资料馆───\x01",
            "为了使市民能尽量放松\x01",
            "而免费开放着。\x02\x03",

            "#220F另外在陛下的援助保证下，\x01",
            "餐饮店也尽量不关门，\x01",
            "努力保持着营业状态。\x02\x03",

            "我们通过这些方式来\x01",
            "平复市民们的心情。\x02\x03",

            "另外在关键时刻可以把\x01",
            "亚宁堡当作避难所……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(-61920, 0, -38980, 0)
    OP_67(0, 6840, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #59
        0x101,
        (
            "#1004F#4P好、好像公爵在说些\x01",
            "非常像模像样的话……\x02\x03",

            "#1015F是吗？就像武术大会时\x01",
            "被人支使的一样吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x102,
        (
            "#1040F#6P不，那不是打招呼，\x01",
            "并不是事先准备好\x01",
            "然后说一通的那种……\x02\x03",

            "明显是以他自己的意志为基础\x01",
            "说出来的属于他自己的话。\x02\x03",

            "公爵好像是因为某种原因\x01",
            "而开始改变了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#1015F是吗……\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_A2(0x20F0)
    OP_4B(0xB, 255)
    OP_4B(0xC, 255)
    OP_4B(0xD, 255)
    OP_4B(0xE, 255)
    OP_4B(0xF, 255)
    EventEnd(0x0)
    Return()

    # Function_11_ED6 end

    SaveToFile()

Try(main)
