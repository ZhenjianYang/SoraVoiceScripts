from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4110   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4110.x',
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
        '拉科舒',                               # 9
        '菲利奥',                               # 10
        '西加罗',                               # 11
        '芭蒂',                                 # 12
        '拉尔夫',                               # 13
        '比尔爷爷',                             # 14
        '伊鲁妮婆婆',                           # 15
        '丹克',                                 # 16
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
        'ED6_DT07/CH01030 ._CH',             # 00
        'ED6_DT07/CH01043 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01490 ._CH',             # 03
        'ED6_DT07/CH01180 ._CH',             # 04
        'ED6_DT07/CH01460 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01030P._CP',             # 00
        'ED6_DT07/CH01043P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01490P._CP',             # 03
        'ED6_DT07/CH01180P._CP',             # 04
        'ED6_DT07/CH01460P._CP',             # 05
    )

    DeclNpc(
        X                   = 59570,
        Z                   = 0,
        Y                   = 58710,
        Direction           = 3,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 57660,
        Z                   = 0,
        Y                   = 58150,
        Direction           = 53,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 7220,
        Z                   = 200,
        Y                   = 53570,
        Direction           = 269,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -29600,
        Z                   = 4000,
        Y                   = 1830,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -27310,
        Z                   = 0,
        Y                   = -4370,
        Direction           = 81,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 28110,
        Z                   = 0,
        Y                   = -950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 32189,
        Z                   = 0,
        Y                   = 6630,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 91740,
        Z                   = 0,
        Y                   = -1110,
        Direction           = 23,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    ScpFunction(
        "Function_0_1DA",          # 00, 0
        "Function_1_30B",          # 01, 1
        "Function_2_331",          # 02, 2
        "Function_3_355",          # 03, 3
        "Function_4_70A",          # 04, 4
        "Function_5_AB4",          # 05, 5
        "Function_6_E7E",          # 06, 6
        "Function_7_1327",         # 07, 7
        "Function_8_1652",         # 08, 8
        "Function_9_1B23",         # 09, 9
        "Function_10_1BA3",        # 0A, 10
    )


    def Function_0_1DA(): pass

    label("Function_0_1DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1FF")
    SetChrFlags(0xD, 0x10)
    SetChrPos(0xE, 31320, 0, 100, 270)
    SetChrFlags(0xE, 0x10)
    Jump("loc_30A")

    label("loc_1FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_25E")
    SetChrPos(0xB, -27310, 0, -4370, 81)
    OP_43(0xB, 0x0, 0x6, 0x2)
    SetChrPos(0xC, -29600, 4000, 1830, 90)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0xE, 31320, 0, 100, 270)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_30A")

    label("loc_25E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_29D")
    SetChrPos(0xB, -27310, 0, -4370, 81)
    OP_43(0xB, 0x0, 0x6, 0x2)
    SetChrPos(0xC, -29600, 4000, 1830, 90)
    OP_43(0xC, 0x0, 0x0, 0x2)
    SetChrFlags(0xE, 0x10)
    Jump("loc_30A")

    label("loc_29D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_2DC")
    SetChrPos(0xB, -27310, 0, -4370, 81)
    OP_43(0xB, 0x0, 0x6, 0x2)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xC, -29600, 4000, 1830, 90)
    OP_43(0xC, 0x0, 0x0, 0x2)
    Jump("loc_30A")

    label("loc_2DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EA")
    Jump("loc_30A")

    label("loc_2EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2F9")
    SetChrFlags(0xE, 0x10)
    Jump("loc_30A")

    label("loc_2F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_303")
    Jump("loc_30A")

    label("loc_303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_30A")

    label("loc_30A")

    Return()

    # Function_0_1DA end

    def Function_1_30B(): pass

    label("Function_1_30B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_327")
    OP_B1("t4110_y")
    Jump("loc_330")

    label("loc_327")

    OP_B1("t4110_n")

    label("loc_330")

    Return()

    # Function_1_30B end

    def Function_2_331(): pass

    label("Function_2_331")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_354")
    OP_8D(0xFE, -30880, 4000, -29430, 0, 2000)
    Jump("Function_2_331")

    label("loc_354")

    Return()

    # Function_2_331 end

    def Function_3_355(): pass

    label("Function_3_355")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_43D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3C1")

    ChrTalk(    #0
        0xFE,
        (
            "我丈夫为了保护仓库\x01",
            "好像去了港口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "他是不是在我的教育下终于\x01",
            "觉醒了工作的热情？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43A")

    label("loc_3C1")


    ChrTalk(    #2
        0xFE,
        (
            "隔壁的那家主人我好像\x01",
            "在哪儿见过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "不过当我想看清他的脸时\x01",
            "他就躲到店里去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "大概是个容易害羞的人……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_43A")

    Jump("loc_706")

    label("loc_43D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_4E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_49A")

    ChrTalk(    #5
        0xFE,
        (
            "对了，隔壁的空房\x01",
            "似乎找到房客了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "不知道会搬来\x01",
            "一个怎样的人呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E4")

    label("loc_49A")


    ChrTalk(    #7
        0xFE,
        (
            "听说我丈夫卷入了一个事件\x01",
            "我可担心死了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "他没事真是太好了……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_4E4")

    Jump("loc_706")

    label("loc_4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_588")

    ChrTalk(    #9
        0xFE,
        (
            "今天我给在港口工作的丈夫\x01",
            "送去了亲手特制的便当。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "光是对他压力\x01",
            "他也受不了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "这就是所谓的大棒和萝卜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "我可是参考帝国的伟人\x01",
            "写的书哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_706")

    label("loc_588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F1")

    ChrTalk(    #13
        0xFE,
        (
            "因为我丈夫赖床，我就把穿着\x01",
            "睡衣的他直接拖到外面，让他上班去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "这也是为了他好！\x02",
    )

    CloseMessageWindow()
    Jump("loc_706")

    label("loc_5F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_677")

    ChrTalk(    #15
        0xFE,
        "我想了很久……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "就因为我没好好提醒丈夫，\x01",
            "结果就把他给惯坏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "就算今后被说成是狠心的妻子\x01",
            "我也要为了丈夫拼了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_706")

    label("loc_677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_706")

    ChrTalk(    #18
        0xFE,
        (
            "自从在卢安的游戏吧大败之后\x01",
            "我丈夫就在港口认真工作着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "因为那件事他终于清醒了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "虽然我想这么认为，\x01",
            "不过还不能放松警惕。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_706")

    TalkEnd(0xFE)
    Return()

    # Function_3_355 end

    def Function_4_70A(): pass

    label("Function_4_70A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_79D")

    ChrTalk(    #21
        0xFE,
        (
            "虽然因为导力器不能用，\x01",
            "我也消沉了一阵子，\x01",
            "不过还是只能努力活下去啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "我妻子艾德尔也在\x01",
            "店里努力工作，\x01",
            "我也必须努力不输给她。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB0")

    label("loc_79D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_81F")

    ChrTalk(    #23
        0xFE,
        (
            "听说一部分港口的设施\x01",
            "被坦克给破坏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "住在隔壁的丹克先生\x01",
            "好像也被特务兵抓走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "希望他不要受伤什么的……\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB0")

    label("loc_81F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_8DB")

    ChrTalk(    #26
        0xFE,
        (
            "市民们在柏斯的教会祈祷\x01",
            "生意兴隆，修女可生气了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "哈哈，女神\x01",
            "确实不是财神啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "好像共和国有些人信奉\x01",
            "掌管生意兴隆的神。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "……如果我妻子知道了\x01",
            "一定会飞去共和国的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB0")

    label("loc_8DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_984")

    ChrTalk(    #30
        0xFE,
        (
            "洛连特的教会虽然简陋，不过迪拜恩\x01",
            "教区长是个很容易让人留下印象的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "沉稳又有威严，\x01",
            "对草药也很有研究。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "确实可以说是个\x01",
            "与教区长身份相符的人。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB0")

    label("loc_984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_A2F")

    ChrTalk(    #33
        0xFE,
        (
            "不久前我和妻子一起\x01",
            "周游了利贝尔所有的七耀教会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "虽然妻子的目的\x01",
            "是购物……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "不过在卡兰大主教的劝说下\x01",
            "她总结了一篇周游的游记。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "好～我要努力了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB0")

    label("loc_A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_AB0")

    ChrTalk(    #37
        0xFE,
        (
            "我的妻子在东街区\x01",
            "经营着百货商店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "你问我是干什么的？\x01",
            "唔～大概可以说是宗教家之类的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "我绝不是家庭妇男哦。\x02",
    )

    CloseMessageWindow()

    label("loc_AB0")

    TalkEnd(0xFE)
    Return()

    # Function_4_70A end

    def Function_5_AB4(): pass

    label("Function_5_AB4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B0D")

    ChrTalk(    #40
        0xFE,
        (
            "啊～导力器都不能用了，\x01",
            "真不方便啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "真希望女王\x01",
            "能赶紧想想办法。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E7A")

    label("loc_B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_C5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF7")

    ChrTalk(    #42
        0xFE,
        (
            "武术大会时我丈夫\x01",
            "通宵帮我占座位。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "所以有时得献一下媚，\x01",
            "让他明年也能替我努力㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "……呵呵，一半是玩笑啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "努力做家务\x01",
            "是因为我爱他……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "我平时之所以会任性\x01",
            "是因为想看到他为了我\x01",
            "竭尽所能的样子。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_C58")

    label("loc_BF7")


    ChrTalk(    #47
        0xFE,
        (
            "我其实很想每天\x01",
            "好好地为他做家务……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "可是这样一来就\x01",
            "看不到他为了我\x01",
            "竭尽所能的样子了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C58")

    Jump("loc_E7A")

    label("loc_C5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_C94")

    ChrTalk(    #49
        0xFE,
        "哼哼哼～⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "那么赶快开始\x01",
            "准备晚饭吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E7A")

    label("loc_C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_CC4")

    ChrTalk(    #51
        0xFE,
        "哼哼哼～⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "啦啦啦、啦啦啦⊙\x02",
    )

    CloseMessageWindow()
    Jump("loc_E7A")

    label("loc_CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D22")

    ChrTalk(    #53
        0xFE,
        (
            "这个叫希德\x01",
            "中校的人强不强呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "光看照片的话感觉\x01",
            "也没什么了不起的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E7A")

    label("loc_D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_DB9")

    ChrTalk(    #55
        0xFE,
        (
            "尤莉亚上尉和卡西乌斯准将\x01",
            "打的话谁比较强呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "唔，这可难以估计……\x01",
            "得再收集些情报……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "对了，让我先生去\x01",
            "侦察一下军队的演习吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E7A")

    label("loc_DB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_E3F")

    ChrTalk(    #58
        0xFE,
        (
            "王国军的卡西乌斯准将\x01",
            "是百日战役的英雄吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "如果这样的人参加武术大会的话\x01",
            "一定会引起轰动的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "这一定要特别注意！\x02",
    )

    CloseMessageWindow()
    Jump("loc_E7A")

    label("loc_E3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_E7A")

    ChrTalk(    #61
        0xFE,
        "啊，明年快点来吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "真期待下一届武术大会。\x02",
    )

    CloseMessageWindow()

    label("loc_E7A")

    TalkEnd(0xFE)
    Return()

    # Function_5_AB4 end

    def Function_6_E7E(): pass

    label("Function_6_E7E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_E8B")
    Jump("loc_1323")

    label("loc_E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_EFE")

    ChrTalk(    #63
        0xFE,
        "好烫！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "白天还好，\x01",
            "有阳光的温暖……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "晚上做饭可是\x01",
            "非常麻烦的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "得注意不要\x01",
            "引发火灾。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1323")

    label("loc_EFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_F53")

    ChrTalk(    #67
        0xFE,
        "怎、怎么办，太奇怪了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "你、你们，帮帮我！\x01",
            "我妻子今天也在做家务！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1323")

    label("loc_F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_103D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FDA")

    ChrTalk(    #69
        0xFE,
        "…………奇怪。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "今天妻子一直\x01",
            "在做着家务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "不，这样一来我当然省力了……\x01",
            "不过她不会是在图谋着什么吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_103A")

    label("loc_FDA")


    ChrTalk(    #72
        0xFE,
        (
            "虽然妻子一个人做家务\x01",
            "我是轻松多了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "不过还要分析她有什么企图，\x01",
            "搞得我完全无法休息。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_103A")

    Jump("loc_1323")

    label("loc_103D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1082")

    ChrTalk(    #74
        0xFE,
        (
            "呼，难得白天妻子\x01",
            "也会做饭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "可以偶尔休息一下了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1323")

    label("loc_1082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10EC")

    ChrTalk(    #76
        0xFE,
        (
            "啊，今天也一如既往地\x01",
            "一天就这么过去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "空之女神啊，难道说我的\x01",
            "人生就像这样了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1323")

    label("loc_10EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1182")

    ChrTalk(    #78
        0xFE,
        (
            "武术大会时\x01",
            "为了妻子通宵排队，\x01",
            "终于抢到了最前排的位子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "可这么做似乎反而\x01",
            "助长了妻子的任性……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "感觉自己好像被\x01",
            "差使得更厉害了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1323")

    label("loc_1182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_12A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1252")

    ChrTalk(    #81
        0xFE,
        (
            "她让我买东西时顺便\x01",
            "买本武术大会的特辑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "唔，希望她除了零食以外\x01",
            "不要再增加家里的经济负担了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "妻子都等不及武术大会了，\x01",
            "现在就在预估冠军人选。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "可参加的人都还没确定呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_12A5")

    label("loc_1252")


    ChrTalk(    #85
        0xFE,
        (
            "妻子都等不及武术大会了，\x01",
            "现在就在预估冠军人选。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "可参加的人都还没确定呢。\x02",
    )

    CloseMessageWindow()

    label("loc_12A5")

    Jump("loc_1323")

    label("loc_12A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1323")

    ChrTalk(    #87
        0xFE,
        (
            "妻子至今还沉浸在\x01",
            "武术大会的兴奋中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "关心明年的武术大会是可以……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "不过现在我希望\x01",
            "她能帮着干点家务哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1323")

    TalkEnd(0xFE)
    Return()

    # Function_6_E7E end

    def Function_7_1327(): pass

    label("Function_7_1327")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_13A0")

    ChrTalk(    #90
        0xFE,
        (
            "没什么啦，我们年轻时\x01",
            "还没导力器之类的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "如果想成是回到过去的话，\x01",
            "就一点都不会觉得不方便了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164E")

    label("loc_13A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_13DF")

    ChrTalk(    #92
        0xFE,
        "喂，老婆子……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "我们生活中最\x01",
            "重要的是什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164E")

    label("loc_13DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1446")

    ChrTalk(    #94
        0xFE,
        "很久没见孙子了，真想啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "到了我这个年纪，最希望的是\x01",
            "儿子媳妇能带着孙子来看看我们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164E")

    label("loc_1446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_148D")

    ChrTalk(    #96
        0xFE,
        "呼，今天的天气也不错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "天气好的时候\x01",
            "心情也会开朗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164E")

    label("loc_148D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14E4")

    ChrTalk(    #98
        0xFE,
        "哟，已经傍晚了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "空之女神，感谢您今天\x01",
            "也赐给我们一天的和平。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164E")

    label("loc_14E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_156B")

    ChrTalk(    #100
        0xFE,
        (
            "虽然发生了那么\x01",
            "可耻的政变……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "互不侵犯条约的签字仪式\x01",
            "能安然无恙就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "有卡西乌斯准将在\x01",
            "我想是没有问题的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164E")

    label("loc_156B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_1608")

    ChrTalk(    #103
        0xFE,
        (
            "哎呀呀，三国之间的\x01",
            "互不侵犯条约真是了不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "竟然能顺利地让帝国和\x01",
            "共和国互相收刀入鞘……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "说艾莉茜雅女王是利贝尔的\x01",
            "骄傲一点也不为过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164E")

    label("loc_1608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_164E")

    ChrTalk(    #106
        0xFE,
        "今天天气真不错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "偶尔也想和老伴去\x01",
            "艾尔贝离宫散步。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_164E")

    TalkEnd(0xFE)
    Return()

    # Function_7_1327 end

    def Function_8_1652(): pass

    label("Function_8_1652")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_16EC")

    ChrTalk(    #108
        0xFE,
        (
            "虽说是回到了过去，\x01",
            "不过还是有不方便的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "不过还是要忍耐再忍耐……\x01",
            "这一点永远是一样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "只要忍耐，女王陛下\x01",
            "一定会想办法的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1F")

    label("loc_16EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_178D")

    ChrTalk(    #111
        0xFE,
        (
            "对了，老头子，\x01",
            "最重要的不就是忍耐吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "无论遇到什么样的困境，\x01",
            "忍耐下去的话一定会有所好转。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "如果拥有能忍耐的坚强的心，\x01",
            "一定能得到幸福的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1F")

    label("loc_178D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1807")

    ChrTalk(    #114
        0xFE,
        (
            "对了，我在百货商店\x01",
            "看见了一个穿白衣服的女孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "呵呵，这让我想起来孙儿们。\x01",
            "不知道他们现在怎么样了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1F")

    label("loc_1807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_18A2")

    ChrTalk(    #116
        0xFE,
        (
            "临近签字仪式，城里的气氛\x01",
            "好像一下子变得活跃了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "我还是最喜欢\x01",
            "热闹的王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "因为这里是我遇到老头子的地方，\x01",
            "也是和他一起生活的城市。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1F")

    label("loc_18A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199D")

    ChrTalk(    #119
        0xFE,
        (
            "世界如果能朝好的方向\x01",
            "发展就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "我真的不知道现在\x01",
            "这个世界是怎么了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "从前一切都是\x01",
            "那么地简单。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "自从导力革命以来，\x01",
            "世风就渐渐地变化了……\x01",
            "我们感到很不安啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "真希望这世界上的所有人\x01",
            "都能抱持着感恩的心。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1A10")

    label("loc_199D")


    ChrTalk(    #124
        0xFE,
        (
            "自从导力革命以来，\x01",
            "世风就渐渐地变化了……\x01",
            "我们感到很不安啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "真希望这世界上的所有人\x01",
            "都能抱持着感恩的心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A10")

    Jump("loc_1B1F")

    label("loc_1A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1A71")

    ChrTalk(    #126
        0xFE,
        (
            "老头子啊……\x01",
            "火太大的话血压会上升的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "茶马上就好了，\x01",
            "你先坐下来歇着吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1F")

    label("loc_1A71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_1AD4")

    ChrTalk(    #128
        0xFE,
        (
            "我能和老头子\x01",
            "这样自由地生活\x01",
            "都是拜女王陛下所赐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "呵呵，真的要感谢\x01",
            "女王陛下啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1F")

    label("loc_1AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1B1F")

    ChrTalk(    #130
        0xFE,
        (
            "以前经常和老头子\x01",
            "散步去离宫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "政变之后\x01",
            "还一次也没去过呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B1F")

    TalkEnd(0xFE)
    Return()

    # Function_8_1652 end

    def Function_9_1B23(): pass

    label("Function_9_1B23")

    TalkBegin(0xFE)

    ChrTalk(    #132
        0xFE,
        (
            "哈……\x01",
            "而且港口又封锁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "明明政变的影响好不容易\x01",
            "过去了，一切刚走上正规。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "这样下去的话\x01",
            "不是又要失业了吗！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_1B23 end

    def Function_10_1BA3(): pass

    label("Function_10_1BA3")

    TalkBegin(0xFE)

    ChrTalk(    #135
        0xFE,
        (
            "看来妻子很\x01",
            "为我担心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "我在工作休息时也不偷懒，\x01",
            "而是帮助妻子做家务哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_1BA3 end

    SaveToFile()

Try(main)
