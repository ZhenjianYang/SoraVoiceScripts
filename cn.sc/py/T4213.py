from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4213   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4213.x',
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
        '尤莉亚上尉',                           # 9
        '亲卫队队员',                           # 10
        '亲卫队队员',                           # 11
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
        'ED6_DT27/CH03580 ._CH',             # 00
        'ED6_DT07/CH01320 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT27/CH03580P._CP',             # 00
        'ED6_DT07/CH01320P._CP',             # 01
    )

    DeclNpc(
        X                   = 74150,
        Z                   = 0,
        Y                   = -35040,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 64650,
        Z                   = 0,
        Y                   = -33590,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 70330,
        Z                   = 0,
        Y                   = -41620,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_14F",          # 01, 1
        "Function_2_175",          # 02, 2
        "Function_3_199",          # 03, 3
        "Function_4_1BD",          # 04, 4
        "Function_5_522",          # 05, 5
        "Function_6_64A",          # 06, 6
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_12E")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_14E")

    label("loc_12E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_138")
    Jump("loc_14E")

    label("loc_138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_147")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_14E")

    label("loc_147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_14E")

    label("loc_14E")

    Return()

    # Function_0_11A end

    def Function_1_14F(): pass

    label("Function_1_14F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16B")
    OP_B1("t4213_y")
    Jump("loc_174")

    label("loc_16B")

    OP_B1("t4213_n")

    label("loc_174")

    Return()

    # Function_1_14F end

    def Function_2_175(): pass

    label("Function_2_175")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_198")
    OP_8D(0xFE, 62680, -31070, 69060, -36680, 2000)
    Jump("Function_2_175")

    label("loc_198")

    Return()

    # Function_2_175 end

    def Function_3_199(): pass

    label("Function_3_199")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1BC")
    OP_8D(0xFE, 65860, -37440, 73950, -46540, 2000)
    Jump("Function_3_199")

    label("loc_1BC")

    Return()

    # Function_3_199 end

    def Function_4_1BD(): pass

    label("Function_4_1BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_51E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_464")

    ChrTalk(    #0
        0x8,
        (
            "#173F科洛蒂娅殿下……\x01",
            "艾丝蒂尔也在一起啊，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1008F这次是被尤莉亚上尉\x01",
            "和亲卫队给救了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#171F呵呵，这是因为有了希德中校\x01",
            "那迅速又恰当的判断。\x02\x03",

            "#176F而且如果凯文先生不在的话\x01",
            "我们也来不及追上凯诺娜……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1002F凯诺娜上尉啊……\x01",
            "她现在在雷斯顿要塞？\x02\x03",

            "她好像愿意说出玲和\x01",
            "结社的事了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#170F凯诺娜她明白现在的危急情况\x01",
            "以及自己的作用。\x02\x03",

            "她需要的是一种契机。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1011F……这样啊，你认识她，\x01",
            "难怪这么了解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#170F我和她在士官学校时代\x01",
            "曾是互相竞争和提高的关系……\x02\x03",

            "在我被配属到亲卫队，\x01",
            "她被配属到情报部之后\x01",
            "应该也没改变。\x02\x03",

            "#176F现在想来，说不定正因为有了她，\x01",
            "才有了现在的我……\x02\x03",

            "#178F我……从没想到结果\x01",
            "会是这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x105,
        "#042F尤莉亚上尉……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1668)
    Jump("loc_51E")

    label("loc_464")


    ChrTalk(    #8
        0x8,
        (
            "#170F还有结社。\x02\x03",

            "#176F执行者们的能力自不必说，竟然\x01",
            "还拥有制造出那个巨大机器人的技术能力……\x02\x03",

            "#170F看来我们的敌人\x01",
            "比想象中的强大。\x02\x03",

            "虽然我们以前并没有轻视他们，\x01",
            "不过还是要重新认识。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51E")

    TalkEnd(0xFE)
    Return()

    # Function_4_1BD end

    def Function_5_522(): pass

    label("Function_5_522")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_581")

    ChrTalk(    #9
        0xFE,
        (
            "柏斯地区真的\x01",
            "出现了龙？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "王国军的飞船竟然和龙战斗了，\x01",
            "看来会写入历史了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_646")

    label("loc_581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_5EF")

    ChrTalk(    #11
        0xFE,
        (
            "想不到情报部的那些家伙在\x01",
            "背地里开发出了那样的东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "如果队长没来的话\x01",
            "王都会变得怎样呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_646")

    label("loc_5EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_646")

    ChrTalk(    #13
        0xFE,
        (
            "尤莉亚上尉\x01",
            "现在不在这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "为了给埃尔赛尤换引擎，\x01",
            "她现在在雷斯顿要塞。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_646")

    TalkEnd(0xFE)
    Return()

    # Function_5_522 end

    def Function_6_64A(): pass

    label("Function_6_64A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6DB")

    ChrTalk(    #15
        0xFE,
        (
            "我们亲卫队如果不能用枪的话，\x01",
            "作战能力就会下降了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "如果这时候帝国来进攻的话……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "……哎，\x01",
            "对了，帝国也一样不能用枪啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A8")

    label("loc_6DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_744")

    ChrTalk(    #18
        0xFE,
        (
            "以前亲卫队好像\x01",
            "有个很厉害的大队长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "是个被称为魔鬼\x01",
            "大队长的人，\x01",
            "到底是怎样一个人呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A8")

    label("loc_744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_7A8")

    ChrTalk(    #20
        0xFE,
        (
            "现在已经号称拥有最高性能的埃尔\x01",
            "赛尤竟然还要更为进化……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "到底要变成一艘怎样的船啊？\x02",
    )

    CloseMessageWindow()

    label("loc_7A8")

    TalkEnd(0xFE)
    Return()

    # Function_6_64A end

    SaveToFile()

Try(main)
