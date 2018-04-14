from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4101_1 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T4101_1 ._SN',
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_2AC",          # 01, 1
        "Function_2_3B4",          # 02, 2
        "Function_3_59A",          # 03, 3
        "Function_4_6E6",          # 04, 4
        "Function_5_832",          # 05, 5
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D1, 2)), scpexpr(EXPR_END)), "loc_104")

    ChrTalk(    #0
        0xFE,
        (
            "#063F阿加特哥哥为什么\x01",
            "不一起吃冰淇淋？\x02\x03",

            "等我长大了他\x01",
            "会不会和我一起吃？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A8")

    label("loc_104")


    ChrTalk(    #1
        0xFE,
        (
            "#563F这里的冰淇淋\x01",
            "明明这么好吃……\x02\x03",

            "#063F阿加特哥哥为什么\x01",
            "不一起吃？\x02\x03",

            "#064F啊……难道他\x01",
            "讨厌冰淇淋？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1016F我倒不这么认为。\x02\x03",

            "#1007F按照阿加特的性格，\x01",
            "肯定是因为害羞而逞强。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 300)

    ChrTalk(    #3
        0xFE,
        (
            "#065F难、难道是因为要\x01",
            "和我这样的孩子一起的关系？\x02\x03",

            "那个那个……那么等我长大了\x01",
            "他会不会和我一起吃？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1016F这、这个么……\x01",
            "去问问他本人如何？\x02\x03",

            "#1015F不过，长大后的提妲啊……\x02\x03",

            "#1016F给阿加特可能太浪费了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "#065F啊啊？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x168A)

    label("loc_2A8")

    TalkEnd(0xFE)
    Return()

    # Function_0_AA end

    def Function_1_2AC(): pass

    label("Function_1_2AC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D1, 1)), scpexpr(EXPR_END)), "loc_2E0")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #6
        0xFE,
        (
            "#261F赶紧完成工作\x01",
            "回来哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B0")

    label("loc_2E0")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #7
        0xFE,
        (
            "#260F啊，姐姐。\x01",
            "工作还没结束？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1000F很快就好了，\x01",
            "你再稍微等会儿？\x02\x03",

            "等我去利贝尔通讯\x01",
            "调查完就回协会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "#264F真的？\x02\x03",

            "#265F那在此之前\x01",
            "我们就回去等着了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#1001F晚饭大伙儿\x01",
            "一起吃吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1689)

    label("loc_3B0")

    TalkEnd(0xFE)
    Return()

    # Function_1_2AC end

    def Function_2_3B4(): pass

    label("Function_2_3B4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3F6")

    ChrTalk(    #11
        0xFE,
        "去下水道有事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "进去是可以，\x01",
            "不过要小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_596")

    label("loc_3F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_431")

    ChrTalk(    #13
        0xFE,
        "去下水道有事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "游击士倒是\x01",
            "可以进去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_596")

    label("loc_431")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_488")

    ChrTalk(    #15
        0xFE,
        "哎呀，你们是游击士吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "我听说通缉魔兽的事了。\x01",
            "不用客气，请过去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_596")

    label("loc_488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D8")

    ChrTalk(    #17
        0xFE,
        (
            "很遗憾，不能\x01",
            "让你们进去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "如果要训练的话\x01",
            "请去别的地方。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_596")

    label("loc_4D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_51D")

    ChrTalk(    #19
        0xFE,
        "去下水道有事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "不好意思，暂时不能\x01",
            "让你们进去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_596")

    label("loc_51D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_596")

    ChrTalk(    #21
        0xFE,
        "这条下水道现在被封锁了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "因为最近来王都的\x01",
            "外国人增加。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "为了不让他们乱闯，\x01",
            "为慎重起见就在此警戒了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_596")

    TalkEnd(0xFE)
    Return()

    # Function_2_3B4 end

    def Function_3_59A(): pass

    label("Function_3_59A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_5A6")
    Return()

    label("loc_5A6")

    EventBegin(0x0)
    Fade(500)
    OP_6D(109680, 1500, 33080, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 108790, 1250, 32950, 90)
    SetChrPos(0x105, 107810, 1250, 33760, 90)
    SetChrPos(0x104, 107340, 1250, 32390, 90)
    SetChrPos(0x108, 106280, 1250, 33000, 90)
    OP_0D()

    ChrTalk(    #24
        0x101,
        "#1004F咦？锁开着？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x105,
        (
            "#044F这里的入口\x01",
            "在没有武术大会等活动的时候\x01",
            "都一直上着锁。\x02\x03",

            "#042F那么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x104,
        (
            "#035F呼，看来这就是\x01",
            "最终的目的地了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x108,
        (
            "#070F好……\x01",
            "赶紧进去吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0xC4, 0x1, 0x100)
    EventEnd(0x0)
    Return()

    # Function_3_59A end

    def Function_4_6E6(): pass

    label("Function_4_6E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_6F2")
    Return()

    label("loc_6F2")

    EventBegin(0x0)
    Fade(500)
    OP_6D(109680, 1500, 35580, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 108790, 1250, 35450, 90)
    SetChrPos(0x105, 107810, 1250, 36260, 90)
    SetChrPos(0x104, 107340, 1250, 34890, 90)
    SetChrPos(0x108, 106280, 1250, 35500, 90)
    OP_0D()

    ChrTalk(    #28
        0x101,
        "#1004F咦？锁开着？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x105,
        (
            "#044F这里的入口\x01",
            "在没有武术大会等活动的时候\x01",
            "都一直上着锁。\x02\x03",

            "#042F那么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x104,
        (
            "#035F呼，看来这就是\x01",
            "最终的目的地了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x108,
        (
            "#070F好……\x01",
            "赶紧进去吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0xC4, 0x1, 0x100)
    EventEnd(0x0)
    Return()

    # Function_4_6E6 end

    def Function_5_832(): pass

    label("Function_5_832")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_83E")
    Return()

    label("loc_83E")

    EventBegin(0x0)
    Fade(500)
    OP_6D(109680, 1500, 30580, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 108790, 1250, 30450, 90)
    SetChrPos(0x105, 107810, 1250, 31260, 90)
    SetChrPos(0x104, 107340, 1250, 29890, 90)
    SetChrPos(0x108, 106280, 1250, 30500, 90)
    OP_0D()

    ChrTalk(    #32
        0x101,
        "#1004F咦？锁开着？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x105,
        (
            "#044F这里的入口\x01",
            "在没有武术大会等活动的时候\x01",
            "都一直上着锁。\x02\x03",

            "#042F那么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x104,
        (
            "#035F呼，看来这就是\x01",
            "最终的目的地了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x108,
        (
            "#070F好……\x01",
            "赶紧进去吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0xC4, 0x1, 0x100)
    EventEnd(0x0)
    Return()

    # Function_5_832 end

    SaveToFile()

Try(main)
