from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0101_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0101_1 ._SN',
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
        "Function_1_106",          # 01, 1
        "Function_2_1AF",          # 02, 2
        "Function_3_45C",          # 03, 3
        "Function_4_4A2",          # 04, 4
        "Function_5_4E8",          # 05, 5
        "Function_6_52E",          # 06, 6
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "进入地下水路\x01",      # 0
            "离开\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EE"),
        (1, "loc_FA"),
        (SWITCH_DEFAULT, "loc_100"),
    )


    label("loc_EE")

    NewScene("ED6_DT21/C0500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_100")

    label("loc_FA")

    TalkEnd(0xFF)
    Jump("loc_100")

    label("loc_100")

    Sleep(30)
    Return()

    # Function_0_AA end

    def Function_1_106(): pass

    label("Function_1_106")

    FadeToDark(0, 0, -1)
    OP_0D()
    OP_6D(75350, 0, 18760, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 75350, 0, 18760, 270)
    SetChrPos(0x1, 75350, 0, 18760, 270)
    SetChrPos(0x2, 75350, 0, 18760, 270)
    SetChrPos(0x3, 75350, 0, 18760, 270)
    OP_30(0x0)
    SetMapFlags(0x1)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    ClearMapFlags(0x80)
    Return()

    # Function_1_106 end

    def Function_2_1AF(): pass

    label("Function_2_1AF")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6F(0xD, 0)
    OP_6D(66130, 0, 55700, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_20F():
        OP_6D(66730, 0, 50970, 5500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20F)
    FadeToBright(1000, 0)
    Sleep(1000)
    OP_70(0xD, 0x3B)
    OP_73(0xD)
    Sleep(400)
    OP_43(0x101, 0x0, 0x1, 0x3)
    Sleep(1000)
    OP_43(0x103, 0x0, 0x1, 0x4)
    Sleep(1000)
    OP_43(0xF8, 0x0, 0x1, 0x5)
    Sleep(1000)
    OP_43(0xF9, 0x0, 0x1, 0x6)
    WaitChrThread(0xF9, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #0
        0x101,
        (
            "#1006F好了……\x01",
            "完成一件工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x103,
        "#022F赶快回到原来的工作中吧。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_303")

    ChrTalk(    #2
        0x106,
        (
            "#050F就是那个昏睡事件的调查吧。\x02\x03",

            "立即重新开始吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E4")

    label("loc_303")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_351")

    ChrTalk(    #3
        0x108,
        (
            "#072F嗯，是昏睡事件的调查吧。\x02\x03",

            "立刻重新开始打听情况吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E4")

    label("loc_351")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_397")

    ChrTalk(    #4
        0x104,
        (
            "#030F嗯，是昏睡事件的调查吧。\x02\x03",

            "立刻重新开始吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E4")

    label("loc_397")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E4")

    ChrTalk(    #5
        0x105,
        (
            "#042F嗯，是昏睡事件的调查吧……\x02\x03",

            "……重新开始打听情况吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E4")


    ChrTalk(    #6
        0x101,
        "#1002F嗯！\x02",
    )

    CloseMessageWindow()
    OP_28(0x74, 0x1, 0x400)
    OP_28(0x74, 0x1, 0x800)
    OP_28(0x74, 0x4, 0x10)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #7
        "\x07\x02任务【搜寻迷路的猫咪】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_2_1AF end

    def Function_3_45C(): pass

    label("Function_3_45C")

    SetChrPos(0xFE, 66000, 500, 55500, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x101D0, 0x0, 0xC8C8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x101D0, 0x0, 0xBF68, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_3_45C end

    def Function_4_4A2(): pass

    label("Function_4_4A2")

    SetChrPos(0xFE, 66000, 500, 55500, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x101D0, 0x0, 0xC8C8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFD51, 0x0, 0xC58A, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_4_4A2 end

    def Function_5_4E8(): pass

    label("Function_5_4E8")

    SetChrPos(0xFE, 66000, 500, 55500, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x101D0, 0x0, 0xC8C8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x10662, 0x0, 0xC58A, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_5_4E8 end

    def Function_6_52E(): pass

    label("Function_6_52E")

    SetChrPos(0xFE, 66000, 500, 55500, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x101D0, 0x1F4, 0xD0AC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_72(0xD, 0x800)
    OP_70(0xD, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xD)
    OP_71(0xD, 0x800)
    Sleep(1000)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x101D0, 0x0, 0xC8C8, 0x7D0, 0x0)
    Return()

    # Function_6_52E end

    SaveToFile()

Try(main)
