from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4230   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4230.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '艾莉茜雅女王',                         # 9
        '红茶',                                 # 10
        '红茶',                                 # 11
        '红茶',                                 # 12
        '红茶',                                 # 13
        '红茶',                                 # 14
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
        'ED6_DT07/CH02013 ._CH',             # 00
        'ED6_DT27/CH03003 ._CH',             # 01
        'ED6_DT07/CH00033 ._CH',             # 02
        'ED6_DT07/CH00043 ._CH',             # 03
        'ED6_DT07/CH00073 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH02013P._CP',             # 00
        'ED6_DT27/CH03003P._CP',             # 01
        'ED6_DT07/CH00033P._CP',             # 02
        'ED6_DT07/CH00043P._CP',             # 03
        'ED6_DT07/CH00073P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_1D0",          # 01, 1
        "Function_2_207",          # 02, 2
        "Function_3_4AE",          # 03, 3
        "Function_4_1606",         # 04, 4
        "Function_5_1DEE",         # 05, 5
        "Function_6_1E3D",         # 06, 6
        "Function_7_1EA0",         # 07, 7
        "Function_8_1F03",         # 08, 8
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BC")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -104230, 200, 9990, 225)

    label("loc_1BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1CF")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_1CF")

    Return()

    # Function_0_19A end

    def Function_1_1D0(): pass

    label("Function_1_1D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EC")
    OP_B1("t4230_y")
    Jump("loc_1F5")

    label("loc_1EC")

    OP_B1("t4230_n")

    label("loc_1F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_206")
    OP_72(0xB, 0x4)

    label("loc_206")

    Return()

    # Function_1_1D0 end

    def Function_2_207(): pass

    label("Function_2_207")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_297")
    Jump("loc_2D9")

    label("loc_297")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B3")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D9")

    label("loc_2B3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CF")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D9")

    label("loc_2CF")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D9")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F")

    ChrTalk(    #0
        0x8,
        (
            "#090F在卡西乌斯先生的帮助下\x01",
            "王国军正在踏踏实实地重建。\x02\x03",

            "#094F选择最好的道路前进……\x02\x03",

            "#090F说起来虽然容易，\x01",
            "不过做起来没有比这个更难的了。\x02\x03",

            "他是少数掌握了正确\x01",
            "前进方向的人。\x02\x03",

            "#093F本来他肯定是很想和艾丝蒂尔\x01",
            "享受天伦之乐的……\x02\x03",

            "#090F所以即便是为了回应他的精神，\x01",
            "我也要以我的方式\x01",
            "来努力。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_4A5")

    label("loc_42F")


    ChrTalk(    #1
        0x8,
        (
            "#090F卡西乌斯先生肯定是很想和艾丝蒂尔\x01",
            "享受天伦之乐的……\x02\x03",

            "所以即便是为了回应他的精神，\x01",
            "我也要以我的方式\x01",
            "来努力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A5")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_2_207 end

    def Function_3_4AE(): pass

    label("Function_3_4AE")

    EventBegin(0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x105, 0x40)
    SetChrFlags(0x104, 0x40)
    SetChrFlags(0x108, 0x40)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x108, 0x4)
    SetChrPos(0x8, -104230, 200, 9990, 225)
    SetChrPos(0x101, -105330, 200, 10390, 180)
    SetChrPos(0x105, -103780, 200, 9000, 270)
    SetChrPos(0x108, -105330, 50, 7670, 0)
    SetChrPos(0x104, -106680, 200, 9000, 90)
    SetChrPos(0x9, -104750, 550, 9430, 0)
    SetChrPos(0xA, -105280, 550, 9460, 0)
    SetChrPos(0xB, -104730, 550, 8950, 0)
    SetChrPos(0xC, -105280, 550, 8400, 0)
    SetChrPos(0xD, -105830, 550, 8950, 0)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x104, 2)
    SetChrChipByIndex(0x105, 3)
    SetChrChipByIndex(0x108, 4)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x105, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0x105, 2)
    OP_6D(-104610, 200, 9480, 0)
    OP_67(0, 5280, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(253, 0)
    OP_72(0xB, 0x4)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #2
        0x8,
        (
            "#094F对了……\x01",
            "你们是为了恐吓信的事来的吗？\x02\x03",

            "竟然连各国的大使馆\x01",
            "和教会都寄了……\x02\x03",

            "#092F让人觉得这已经不是\x01",
            "单纯的恶作剧了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1002F#6P嗯，是的。\x02\x03",

            "所以我们要通过\x01",
            "向相关人士打听情况\x01",
            "来找到罪犯的线索……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x105,
        (
            "#043F#4P祖母大人，关于这起事件您\x01",
            "有什么线索吗？\x02\x03",

            "特别是国内方面的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        "#094F让我想想……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(300)

    ChrTalk(    #6
        0x8,
        (
            "#090F科洛蒂娅，\x01",
            "你自己怎么认为？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x105,
        "#044F#4P我吗……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#090F你作为王位继承者，\x01",
            "平时应该有就国内形势\x01",
            "进行分析……\x02\x03",

            "你能不能对我说说？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x105,
        (
            "#542F#4P是、是……\x02\x03",

            "#047F…………………………………\x02\x03",

            "#042F关于互不侵犯条约，\x01",
            "国内应该几乎没有什么\x01",
            "反对势力。\x02\x03",

            "不过我听说在政变后\x01",
            "极右势力有被逼到\x01",
            "绝境的趋势。\x02\x03",

            "他们有可能把这份情绪\x01",
            "转换为恐吓信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#094F呵呵……很好。\x02\x03",

            "#090F和我的意见大致相同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#1004F#6P请问，这是怎么回事？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    Sleep(300)

    ChrTalk(    #12
        0x8,
        (
            "#094F除了理查德上校之外\x01",
            "以前还有不少\x01",
            "主张扩充军备的人。\x02\x03",

            "#092F不过在政变后，\x01",
            "这种主张完全\x01",
            "被封锁了。\x02\x03",

            "他们一定积聚了不安和\x01",
            "不满的情绪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#1002F#6P那么就是说……\x02\x03",

            "还有除了理查德上校\x01",
            "之外的扩军主义者在记恨政府？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#090F也可以\x01",
            "这么说。\x02\x03",

            "#094F如果是这样的话……\x01",
            "与其说这是他们的罪，\x01",
            "倒不如说是我的责任。\x02\x03",

            "因为利贝尔的言论自由，\x01",
            "是我所给予认可的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x105,
        "#043F#4P祖母大人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1015F#6P我觉得没必要\x01",
            "太同情他们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#092F不，言论自由是\x01",
            "至为宝贵的。\x02\x03",

            "即便是扩军论，也是\x01",
            "基于爱国的精神。\x02\x03",

            "对这些言论进行全面地研究，\x01",
            "然后把握好国家的发展方向……\x02\x03",

            "这是作为国家元首的责任。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x105,
        "#049F#4P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x108,
        (
            "#070F嗯，不过这样的话……\x02\x03",

            "条约实际被阻碍的\x01",
            "危险就很低了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "#090F如果恐吓犯是扩军\x01",
            "主义者的话可能是这样。\x02\x03",

            "在理查德上校已经被捕的现在，\x01",
            "他们没有闹事的力量。\x02\x03",

            "#094F问题是恐吓犯如果是\x01",
            "其他人的话……\x02\x03",

            "关于这种可能性\x01",
            "我也没什么线索。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1007F#6P这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x104,
        (
            "#030F#6P艾莉茜雅女王。\x01",
            "能问您一个问题吗？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(75)
    SetChrSubChip(0x101, 2)
    SetChrSubChip(0x105, 0)

    ChrTalk(    #23
        0x8,
        "#097F嗯，请问吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x104,
        (
            "#032F#6P陛下为什么要在现在\x01",
            "倡导互不侵犯条约呢？\x02\x03",

            "不管怎么说现在还是政变的\x01",
            "混乱尚未完全平息的时期。\x02\x03",

            "我倒是认为应该先专注于\x01",
            "国内问题而非外交。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #25
        0x101,
        "#1019F喂喂，奥利维尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#094F呵呵，可能正如\x01",
            "奥利维尔先生所说。\x02\x03",

            "#090F不过关于互不侵犯条约，\x01",
            "在政变之前我就\x01",
            "向两国政府试探过了。\x02\x03",

            "如果推迟此事，\x01",
            "势必影响到国家的威信。\x02\x03",

            "而且『克洛斯贝尔问题』\x01",
            "也正处于不断加热的过程中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x104,
        "#033F#6P哟……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(300)

    ChrTalk(    #28
        0x101,
        (
            "#1004F克洛斯贝尔是……\x01",
            "小玲居住的自治州？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x105,
        (
            "#042F嗯，是位于帝国和\x01",
            "共和国之间的自治州。\x02\x03",

            "近几年，围绕着该自治州的归属\x01",
            "问题，两国的对立立场很激烈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x108,
        (
            "#070F就好像是哽在帝国和共和国\x01",
            "之间的鱼骨。\x02\x03",

            "这些纠纷被概括起来\x01",
            "称为『克洛斯贝尔问题』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1015F是吗……\x01",
            "原来是那样的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x104,
        (
            "#035F#6P也就是说由利贝尔通过\x01",
            "互不侵犯条约来拔去这根鱼骨……\x02\x03",

            "#030F您的目的是这个吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "#090F这不是一朝一夕\x01",
            "能解决的问题。\x02\x03",

            "我只是想\x01",
            "提供一种契机。\x02\x03",

            "并且这跟大陆西部的稳定\x01",
            "和提高利贝尔的发言权也\x01",
            "有所关联。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x104,
        (
            "#035F#6P呼，我真是有眼不识泰山。\x02\x03",

            "看来侵略利贝尔的行为\x01",
            "比我想象的还要愚蠢。\x02\x03",

            "我再次深深地体会到了这一点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#1007F现在还说这些干吗……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #36
        0x101,
        (
            "#1004F#6P啊，对了。\x01",
            "稍微改变一下话题。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x05向艾莉茜雅女王询问了关于玲的双亲的事。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #38
        0x8,
        "#097F啊……有这样的事啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#1008F#6P即便是女王陛下应该\x01",
            "也不会对此有什么线索吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12BD")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇已经和希尔丹夫人对话】\x01",      # 0
            "【◇尚未和希尔丹夫人对话】\x01",      # 1
            "【◇什么也没有变更】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_12B1"),
        (1, "loc_12B7"),
        (SWITCH_DEFAULT, "loc_12BD"),
    )


    label("loc_12B1")

    OP_A2(0x1626)
    Jump("loc_12BD")

    label("loc_12B7")

    OP_A3(0x1626)
    Jump("loc_12BD")

    label("loc_12BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_END)), "loc_13E8")

    ChrTalk(    #40
        0x8,
        (
            "#093F嗯……\x01",
            "抱歉……\x02\x03",

            "#090F如果前去格兰赛尔城的话\x01",
            "我想希尔丹夫人\x01",
            "应该知道……\x02\x03",

            "你们已经去见过她了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#1015F#6P是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x105,
        (
            "#043F#4P希尔丹夫人看来也\x01",
            "没什么线索。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "#094F这样啊……\x02\x03",

            "#090F如果你们需要，我可以\x01",
            "联系克洛斯贝尔自治政府。\x02\x03",

            "随时可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1018F#6P啊……是！\x02",
    )

    CloseMessageWindow()
    Jump("loc_14CA")

    label("loc_13E8")


    ChrTalk(    #45
        0x8,
        (
            "#093F嗯……\x01",
            "抱歉……\x02\x03",

            "#090F如果来了格兰赛尔城的话\x01",
            "我想希尔丹夫人会知道。\x02\x03",

            "你们去问问她看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#1006F#6P是，我们会的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "#090F如果你们需要，我可以\x01",
            "联系克洛斯贝尔自治政府。\x02\x03",

            "随时可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        "#1018F#6P啊……是！\x02",
    )

    CloseMessageWindow()

    label("loc_14CA")


    ChrTalk(    #49
        0x105,
        (
            "#041F#4P祖母大人。\x01",
            "谢谢。\x02\x03",

            "#542F我们也该去进行\x01",
            "下面的调查了……\x02\x03",

            "#049F所以……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(300)

    ChrTalk(    #50
        0x8,
        (
            "#094F呵呵，我明白。\x02\x03",

            "#090F你今晚会留在\x01",
            "格兰赛尔城堡吧？\x02\x03",

            "到时让我好好\x01",
            "听听你的想法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x105,
        (
            "#047F#4P是……\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x104, 65535)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 65535)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x105, 0x40)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x40)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x108, 0x40)
    ClearChrFlags(0x108, 0x4)
    Sleep(500)
    Call(0, 4)
    Return()

    # Function_3_4AE end

    def Function_4_1606(): pass

    label("Function_4_1606")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x108, 0x80)
    SetChrFlags(0x104, 0x80)
    OP_6D(-1000, 8000, 35200, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3C)
    OP_72(0x1, 0x10)
    OP_0D()
    OP_43(0x101, 0x1, 0x0, 0x5)
    Sleep(800)
    OP_43(0x108, 0x1, 0x0, 0x6)
    Sleep(800)
    OP_43(0x104, 0x1, 0x0, 0x7)
    Sleep(800)
    OP_43(0x105, 0x1, 0x0, 0x8)
    OP_6D(-200, 8000, 27500, 4000)
    WaitChrThread(0x105, 0x1)
    OP_71(0x1, 0x10)
    Sleep(500)

    ChrTalk(    #52
        0x104,
        (
            "#031F#6P哎呀，真是一位了不起的人物。\x02\x03",

            "那种绝妙的平衡感\x01",
            "可以说是大陆第一了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x108,
        (
            "#071F嗯……\x01",
            "简直是理想的君主。\x02\x03",

            "我还真羡慕利贝尔国民。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1006F哼哼，那是当然。\x02\x03",

            "谁叫这是咱们的\x01",
            "女王呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x105,
        "#049F#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #56
        0x101,
        "#1004F怎么了？科洛丝？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x105,
        (
            "#542F#5P啊，不……\x02\x03",

            "#045F我又一次感受到了\x01",
            "祖母大人的厉害。\x02\x03",

            "我果然是\x01",
            "望尘莫及啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#1026F啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x105, 400)
    Sleep(500)

    ChrTalk(    #59
        0x104,
        (
            "#035F#6P呼，公主殿下。\x02\x03",

            "女王陛下是\x01",
            "什么时候即位的？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x104, 400)
    Sleep(300)

    ChrTalk(    #60
        0x105,
        (
            "#044F#5P啊，哦。\x01",
            "应该是２０岁。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x104,
        "#030F#6P那么殿下的芳龄是？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x105,
        (
            "#043F#5P快１６了……\x02\x03",

            "#044F……啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x104,
        (
            "#031F#6P呵呵，就是这么回事。\x02\x03",

            "陛下刚即位时\x01",
            "也不见得能施展\x01",
            "现在的政治手腕吧。\x02\x03",

            "更不用说你现在还不到\x01",
            "陛下即位时的年龄呢。\x02\x03",

            "这是没的比的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x108,
        (
            "#074F在武术领域，只有拥有\x01",
            "『器』的人才能到达『理』的境界。\x02\x03",

            "可即便是拥有了『器』，\x01",
            "不经过一步步坚实的积累，\x01",
            "也绝对无法到达那一境界。\x02\x03",

            "#070F现在陛下已经看出你\x01",
            "拥有能到达『理』的『器』。\x02\x03",

            "所以你没必要着急。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)
    Sleep(500)

    ChrTalk(    #65
        0x105,
        (
            "#542F#5P奥利维尔先生、金先生……\x02\x03",

            "#041F……谢谢你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1006F呵呵，你们俩\x01",
            "还真有口才。\x02\x03",

            "堪称老当益壮。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)
    Sleep(300)

    ChrTalk(    #67
        0x104,
        (
            "#032F#6P你真没礼貌……\x01",
            "我才２５岁哦。\x02\x03",

            "比金先生可要\x01",
            "年轻５岁呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x108,
        (
            "#075F你才是个没\x01",
            "礼貌的人……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C4B")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇没和希尔丹夫人对话/已去女佣室问了行踪】\x01",      # 0
            "【◇没和希尔丹夫人对话/还没去女佣室】\x01",            # 1
            "【◇已经和希尔丹夫人对话】\x01",                       # 2
            "【◇什么也没有变更】\x01",                             # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C33"),
        (1, "loc_1C3C"),
        (2, "loc_1C45"),
        (SWITCH_DEFAULT, "loc_1C4B"),
    )


    label("loc_1C33")

    OP_A3(0x1626)
    OP_A2(0x1629)
    Jump("loc_1C4B")

    label("loc_1C3C")

    OP_A3(0x1626)
    OP_A3(0x1629)
    Jump("loc_1C4B")

    label("loc_1C45")

    OP_A2(0x1626)
    Jump("loc_1C4B")

    label("loc_1C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 1)), scpexpr(EXPR_END)), "loc_1CCE")

    ChrTalk(    #69
        0x105,
        (
            "#045F#5P呵呵……\x02\x03",

            "#048F那么我们也去\x01",
            "和希尔丹夫人聊聊吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "那么我们去\x01",
            "左侧的资料室吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D4B")

    label("loc_1CCE")


    ChrTalk(    #71
        0x105,
        (
            "#045F#5P呵呵……\x02\x03",

            "#048F那么我们也去\x01",
            "和希尔丹夫人聊聊吧。\x02\x03",

            "去女佣室问问，\x01",
            "就应该能知道她在哪儿了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1006F嗯，ＯＫ。\x02",
    )

    CloseMessageWindow()

    label("loc_1D4B")

    Jump("loc_1DDD")

    label("loc_1D4E")


    ChrTalk(    #73
        0x105,
        (
            "#045F#5P呵呵……\x02\x03",

            "#048F总之现在和祖母大人\x01",
            "以及希尔丹夫人都对话过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#1006F嗯……\x01",
            "要不要回市区？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x105,
        "#542F#5P嗯，是啊。\x02",
    )

    CloseMessageWindow()
    OP_28(0x8B, 0x2, 0x80)
    OP_28(0x8B, 0x1, 0x100)

    label("loc_1DDD")

    Sleep(100)
    OP_A2(0x1625)
    OP_28(0x8B, 0x1, 0x400)
    EventEnd(0x0)
    Return()

    # Function_4_1606 end

    def Function_5_1DEE(): pass

    label("Function_5_1DEE")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -870, 8000, 37870, 180)
    ClearChrFlags(0xFE, 0x80)

    def lambda_1E15():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E15)
    OP_8E(0xFE, 0xFFFFFC7C, 0x1F40, 0x6590, 0x7D0, 0x0)
    OP_8C(0xFE, 360, 400)
    Return()

    # Function_5_1DEE end

    def Function_6_1E3D(): pass

    label("Function_6_1E3D")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -870, 8000, 37870, 180)
    ClearChrFlags(0xFE, 0x80)

    def lambda_1E64():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1E64)
    OP_8E(0xFE, 0xFFFFFC18, 0x1F40, 0x6EE6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x46, 0x1F40, 0x6978, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_6_1E3D end

    def Function_7_1EA0(): pass

    label("Function_7_1EA0")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -870, 8000, 37870, 180)
    ClearChrFlags(0xFE, 0x80)

    def lambda_1EC7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1EC7)
    OP_8E(0xFE, 0xFFFFFC18, 0x1F40, 0x6EE6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF862, 0x1F40, 0x6978, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_7_1EA0 end

    def Function_8_1F03(): pass

    label("Function_8_1F03")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -870, 8000, 37870, 180)
    ClearChrFlags(0xFE, 0x80)

    def lambda_1F2A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1F2A)
    OP_8E(0xFE, 0xFFFFFC18, 0x1F40, 0x8980, 0x7D0, 0x0)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFFD44, 0x1F40, 0x6E28, 0x7D0, 0x0)
    Return()

    # Function_8_1F03 end

    SaveToFile()

Try(main)
