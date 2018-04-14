from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0403_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C0403_1 ._SN',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '',                                     # 8
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
    Fade(1000)
    SetChrPos(0x101, -6090, 250, 1060, 90)
    SetChrPos(0x103, -6070, 250, 2780, 180)
    SetChrPos(0xF8, -8390, 250, 160, 90)
    SetChrPos(0xF9, -7890, 250, 2110, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_124")
    SetChrPos(0xF9, -8390, 250, 160, 90)
    SetChrPos(0xF8, -7890, 250, 2110, 135)

    label("loc_124")

    OP_6D(-6780, 250, 1000, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_22E")
    Sleep(1000)
    OP_44(0x8, 0x1)
    TurnDirection(0x8, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1B0")

    def lambda_194():

        label("loc_194")

        OP_97(0x8, 0xFFFFF060, 0x3E8, 0x57E40, 0x1B58, 0x1)
        OP_48()
        Jump("loc_194")

    QueueWorkItem2(0x8, 1, lambda_194)
    Jump("loc_1CF")

    label("loc_1B0")


    def lambda_1B6():

        label("loc_1B6")

        OP_97(0x8, 0xFFFFF060, 0x3E8, 0xFFFA81C0, 0x1B58, 0x1)
        OP_48()
        Jump("loc_1B6")

    QueueWorkItem2(0x8, 1, lambda_1B6)

    label("loc_1CF")

    SetChrChipByIndex(0x8, 11)
    ClearChrFlags(0x8, 0x400)
    SetChrFlags(0x8, 0x4)
    OP_22(0x15B, 0x0, 0x64)
    OP_22(0x8C, 0x0, 0x64)

    label("loc_1E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_220")
    OP_51(0x8, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_218")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_220")

    label("loc_218")

    Sleep(15)
    Jump("loc_1E8")

    label("loc_220")

    OP_44(0x8, 0x1)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x4)

    label("loc_22E")

    WaitChrThread(0x8, 0x1)
    OP_82(0x0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x34\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x234, 1)

    ChrTalk(    #1
        0x101,
        (
            "#1004F戒、戒指……！？\x02\x03",

            "为什么这里\x01",
            "会有这种东西……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_3F4")

    ChrTalk(    #2
        0x103,
        (
            "#022F……………………………\x02\x03",

            "刚才在这里的鸟……\x02\x03",

            "……是乌鸦吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #3
        0x101,
        (
            "#1002F嗯……\x02\x03",

            "好像是。\x01",
            "但实在有点反常……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x101)

    ChrTalk(    #4
        0x101,
        (
            "#1020F……啊……………\x02\x03",

            "难道说这个戒指……\x01",
            "是阿鲁姆的！？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 180, 400)

    ChrTalk(    #5
        0x103,
        (
            "#022F有这个可能。\x02\x03",

            "回城后去向本人\x01",
            "确认一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1002F嗯，明白了！\x02",
    )

    CloseMessageWindow()
    OP_28(0x72, 0x1, 0x4)
    Jump("loc_5BA")

    label("loc_3F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_420")

    ChrTalk(    #7
        0x105,
        "#043F是谁掉的东西呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A8")

    label("loc_420")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44A")

    ChrTalk(    #8
        0x107,
        "#064F是谁掉的东西？\x02",
    )

    CloseMessageWindow()
    Jump("loc_4A8")

    label("loc_44A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_485")

    ChrTalk(    #9
        0x104,
        (
            "#030F唔，大概是失物\x01",
            "总觉得深具意义。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A8")

    label("loc_485")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A8")

    ChrTalk(    #10
        0x108,
        "#073F是失物吗？\x02",
    )

    CloseMessageWindow()

    label("loc_4A8")


    ChrTalk(    #11
        0x103,
        (
            "#026F……如果是的话，这地方也太奇怪了。\x02\x03",

            "没有人会到\x01",
            "这种地方来郊游吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1007F确、确实如此……\x02\x03",

            "#1003F嗯～看起来\x01",
            "好像也没有刻记号的样子……\x02\x03",

            "……会是谁的戒指呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x103,
        (
            "#020F嗯，总之\x01",
            "先暂时保管着吧。\x02\x03",

            "如果在意的话\x01",
            "就去城镇里调查看看好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1000F是呀，先收着吧。\x02",
    )

    CloseMessageWindow()

    label("loc_5BA")

    OP_28(0x72, 0x1, 0x4000)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
