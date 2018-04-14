from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T3119_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3119_1 ._SN',
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
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    OP_59()
    Fade(1000)
    SetChrPos(0x101, -560, 0, 5410, 0)
    SetChrPos(0xF7, 50, 0, 4460, 0)
    SetChrPos(0xF8, -1250, 0, 4210, 0)
    SetChrPos(0xF9, -520, 0, 3020, 0)
    OP_6D(-560, 0, 5410, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #0
        0x101,
        (
            "#1020F这、这回是什么……\x02\x03",

            "为什么『卡佩尔』\x01",
            "写着这种事！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_231")

    ChrTalk(    #1
        0x107,
        (
            "#065F可能是盗取了密码\x01",
            "更改了数据。\x02\x03",

            "如果用管理者权限登录\x01",
            "任何人都能输入……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #2
        0x101,
        "#1004F谁、谁都行吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x107,
        (
            "#561F一、一般是不行的啦。\x02\x03",

            "就算是我\x01",
            "都难以置信。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30F")

    label("loc_231")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A4")

    ChrTalk(    #4
        0x104,
        (
            "#032F虽然不清楚详情，\x01",
            "但似乎是把里面的数据改写了。\x02\x03",

            "#031F哈哈哈。\x01",
            "要是敌人也只有称赞的份了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30F")

    label("loc_2A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30F")

    ChrTalk(    #5
        0x105,
        (
            "#042F虽然不清楚详情\x01",
            "但似乎是把内部的数据改写了呢。\x02\x03",

            "看起来不像是\x01",
            "外行人能处理的机器……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_362")

    ChrTalk(    #6
        0x106,
        (
            "#551F真是个深不可测的家伙啊。\x02\x03",

            "#050F这个暂且不论……\x01",
            "笔记记下了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AB")

    label("loc_362")


    ChrTalk(    #7
        0x103,
        (
            "#025F真是个深不可测的家伙啊。\x02\x03",

            "#020F这个暂且不提……\x01",
            "笔记记下了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AB")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #8
        0x101,
        (
            "#1006F嗯，当然。\x02\x03",

            "#1015F接下来好像又是城里了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_440")
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #9
        0x105,
        (
            "#040F要找的是\x01",
            "尖帽子三兄弟吧。\x02\x03",

            "这个也是\x01",
            "什么比喻吗。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x105, 400)
    Jump("loc_49C")

    label("loc_440")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49C")
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #10
        0x104,
        (
            "#030F然后是尖帽子三兄弟吗……\x02\x03",

            "这个也是\x01",
            "应该是比喻没错吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x104, 400)

    label("loc_49C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4D1")

    ChrTalk(    #11
        0x106,
        (
            "#050F好，知道这个就够了。\x02\x03",

            "回城里吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FE")

    label("loc_4D1")


    ChrTalk(    #12
        0x103,
        (
            "#020F知道这个就够了。\x02\x03",

            "好，返回城里吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FE")

    EventEnd(0x0)
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
