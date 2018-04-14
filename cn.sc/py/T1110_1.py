from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1110_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1110_1 ._SN',
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
        "Function_1_71D",          # 01, 1
        "Function_2_96C",          # 02, 2
        "Function_3_D6A",          # 03, 3
        "Function_4_E8E",          # 04, 4
        "Function_5_F0E",          # 05, 5
        "Function_6_F6C",          # 06, 6
        "Function_7_1002",         # 07, 7
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x11, 17570, 0, 30850, 90)
    SetChrPos(0x101, 19190, 0, 30760, 270)
    SetChrPos(0xF7, 20060, 0, 30110, 270)
    SetChrPos(0xF8, 20850, 0, 31090, 270)
    SetChrPos(0xF9, 19940, 0, 31760, 270)
    OP_6D(19700, 0, 31270, 0)
    OP_67(0, 5760, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        (
            "#1000F#1P那个，打扰一下？\x02\x03",

            "请问米拉诺小姐\x01",
            "的房间是这里吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x11,
        "啊啊，我就是米拉诺。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x11,
        (
            "你们\x01",
            "是游击士对吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20E")

    ChrTalk(    #3
        0x104,
        (
            "#030F呼，我是协助人员。\x02\x03",

            "据说有需要护卫到拉文努村\x01",
            "的任务，是吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308")

    label("loc_20E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_263")

    ChrTalk(    #4
        0x108,
        (
            "#070F啊啊，正是这样。\x02\x03",

            "据说有需要护卫到拉文努村\x01",
            "的任务，是吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308")

    label("loc_263")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B6")

    ChrTalk(    #5
        0x103,
        (
            "#020F嗯，是这样的。\x02\x03",

            "据说有需要护卫到拉文努村\x01",
            "的任务，是吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308")

    label("loc_2B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_308")

    ChrTalk(    #6
        0x106,
        (
            "#050F啊啊，正是这样。\x02\x03",

            "据说有需要护卫到拉文努村\x01",
            "的任务，是吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_308")


    ChrTalk(    #7
        0x11,
        "啊啊，是这么打算的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        (
            "打算去看看\x01",
            "果园的情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x11,
        (
            "不过，还有这么年轻\x01",
            "的小姐在啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        "能不能胜任呢啊？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #11
        0x101,
        (
            "#1009F#1P唔，真、真没礼貌。\x02\x03",

            "我也是正游击士哦。\x01",
            "麻烦你别小看我。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43B")

    ChrTalk(    #12
        0x106,
        (
            "#057F这家伙的实力我担保。\x02\x03",

            "这样还是不相信的话，\x01",
            "不好意思，另请高明吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_561")

    label("loc_43B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49C")

    ChrTalk(    #13
        0x103,
        (
            "#026F我可以担保这女孩的实力。\x02\x03",

            "这样还是不相信的话，\x01",
            "不好意思，另请高明吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_561")

    label("loc_49C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F9")

    ChrTalk(    #14
        0x108,
        (
            "#072F我可以担保她的实力。\x02\x03",

            "这样还是不相信的话，\x01",
            "不好意思，另请高明吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_561")

    label("loc_4F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_561")

    ChrTalk(    #15
        0x104,
        (
            "#032F我可以担保她的实力。\x02\x03",

            "不过，这样还是不相信的话，\x01",
            "不好意思，您只能另请高明了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_561")


    ChrTalk(    #16
        0x11,
        (
            "呼，所谓的\x01",
            "人不可貌相呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        (
            "算了，好吧。\x01",
            "姑且相信你们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x11,
        (
            "那么，咋办。\x01",
            "现在能马上出发吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_28(0x7C, 0x1, 0x1)
    OP_28(0x7C, 0x4, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64E")

    ChrTalk(    #19
        0x101,
        (
            "#1006F#1P嗯。\x01",
            "随时都ＯＫ哦。\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 2)
    Return()

    label("loc_64E")


    ChrTalk(    #20
        0x101,
        (
            "#1008F#1P啊，抱歉。\x01",
            "其实现在有点不方便。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x11,
        (
            "什么？\x01",
            "还有其他事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        (
            "咳～真没法子。\x01",
            "为什么不先办妥了再来？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1007F#1P对，对不起哦。\x01",
            "我们马上回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        "哦，麻烦你喽。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)
    OP_28(0x7C, 0x1, 0x8000)
    EventEnd(0x0)
    OP_4B(0x11, 255)
    OP_44(0x11, 0x0)
    OP_43(0x11, 0x0, 0x0, 0x2)
    Return()

    # Function_0_AA end

    def Function_1_71D(): pass

    label("Function_1_71D")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0x11, 255)
    SetChrPos(0x11, 17570, 0, 30850, 90)
    SetChrPos(0x101, 19190, 0, 30760, 270)
    SetChrPos(0xF7, 20060, 0, 30110, 270)
    SetChrPos(0xF8, 20850, 0, 31090, 270)
    SetChrPos(0xF9, 19940, 0, 31760, 270)
    OP_6D(19700, 0, 31270, 0)
    OP_67(0, 5760, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_80B")

    ChrTalk(    #25
        0x11,
        (
            "啊哟，挺快的嘛。\x01",
            "就回来啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x11,
        (
            "那么，咋样。\x01",
            "现在能马上出发吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_842")

    label("loc_80B")


    ChrTalk(    #27
        0x11,
        "呼哟，我等好久了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x11,
        (
            "那，这下总\x01",
            "可以出发了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_842")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BD")

    ChrTalk(    #29
        0x101,
        (
            "#1006F#1P啊，嗯。\x01",
            "ＯＫ了哦。\x02",
        )
    )

    CloseMessageWindow()
    Call(1, 2)
    Return()

    label("loc_8BD")


    ChrTalk(    #30
        0x101,
        (
            "#1015F#1P唔～其实\x01",
            "还是有点不方便呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x11,
        "咳～怎么又来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x11,
        (
            "有事就全部\x01",
            "解决之后再来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#1007F#1P抱歉，我去去就来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x11,
        "哦，我就在这等你们。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)
    OP_4B(0x11, 255)
    OP_44(0x11, 0x0)
    OP_43(0x11, 0x0, 0x0, 0x2)
    EventEnd(0x0)
    Return()

    # Function_1_71D end

    def Function_2_96C(): pass

    label("Function_2_96C")


    ChrTalk(    #35
        0x11,
        (
            "好了！\x01",
            "那么，赶快出发吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1000F#1P要去拉文努村对吧。\x02\x03",

            "那就是说，要从城西门\x01",
            "前往西柏斯街道。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9FD")

    ChrTalk(    #37
        0x105,
        "#040F对，就是这样。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A7A")

    label("loc_9FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A29")

    ChrTalk(    #38
        0x108,
        "#070F啊啊，应该没错。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A7A")

    label("loc_A29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A53")

    ChrTalk(    #39
        0x103,
        "#020F嗯，是这样吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_A7A")

    label("loc_A53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A7A")

    ChrTalk(    #40
        0x106,
        "#051F啊啊，没错了。\x02",
    )

    CloseMessageWindow()

    label("loc_A7A")


    ChrTalk(    #41
        0x11,
        (
            "那么，我就先\x01",
            "去西门等着了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x11,
        (
            "你们应该\x01",
            "也需要做些准备吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1018F#1P啊，这样最好不过了。\x02\x03",

            "那么，稍后再\x01",
            "到西门会合吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        "好，那么出发吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x11,
        "那，等你们喽。\x02",
    )

    CloseMessageWindow()

    def lambda_B2C():

        label("loc_B2C")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B2C")

    QueueWorkItem2(0x0, 1, lambda_B2C)

    def lambda_B3D():

        label("loc_B3D")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B3D")

    QueueWorkItem2(0x1, 1, lambda_B3D)

    def lambda_B4E():

        label("loc_B4E")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B4E")

    QueueWorkItem2(0x2, 1, lambda_B4E)

    def lambda_B5F():

        label("loc_B5F")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_B5F")

    QueueWorkItem2(0x3, 1, lambda_B5F)
    Sleep(400)

    def lambda_B75():
        OP_6D(19700, 0, 39150, 4000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_B75)
    OP_8E(0x11, 0x4BB4, 0x0, 0x7F4E, 0x7D0, 0x0)
    OP_8E(0x11, 0x4BB4, 0x0, 0x942A, 0x7D0, 0x0)
    OP_8E(0x11, 0x4664, 0x0, 0x942A, 0x7D0, 0x0)

    def lambda_BC9():
        OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_BC9)
    OP_8E(0x11, 0x40EC, 0x0, 0x942A, 0x7D0, 0x0)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x11, 0x2)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    SetChrFlags(0x11, 0x80)
    Fade(1000)
    OP_6D(20620, 0, 31160, 0)
    OP_0D()

    def lambda_C25():
        OP_8C(0x101, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C25)
    Sleep(100)

    def lambda_C38():
        OP_8C(0xF7, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_C38)

    def lambda_C46():
        OP_8C(0xF9, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_C46)
    Sleep(100)
    OP_8C(0xF8, 270, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #46
        0x101,
        (
            "#1006F#1P好了，那么\x01",
            "我们也走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CB2")

    ChrTalk(    #47
        0x109,
        "#1060F噢，城西门是吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D61")

    label("loc_CB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CDE")

    ChrTalk(    #48
        0x105,
        "#040F好，是城西门吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D61")

    label("loc_CDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D0C")

    ChrTalk(    #49
        0x107,
        "#060F嗯，是城西门对吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D61")

    label("loc_D0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D38")

    ChrTalk(    #50
        0x104,
        "#030F啊啊，城西门吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D61")

    label("loc_D38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D61")

    ChrTalk(    #51
        0x108,
        "#070F啊啊，城西门啊。\x02",
    )

    CloseMessageWindow()

    label("loc_D61")

    OP_28(0x7C, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_2_96C end

    def Function_3_D6A(): pass

    label("Function_3_D6A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D77")
    Return()

    label("loc_D77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D89")
    Return()

    label("loc_D89")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xA)"), scpexpr(EXPR_END)), "loc_DC4")
    Call(1, 4)
    Jump("loc_E87")

    label("loc_DC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x12)"), scpexpr(EXPR_END)), "loc_DD3")
    Call(1, 5)
    Jump("loc_E87")

    label("loc_DD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xE)"), scpexpr(EXPR_END)), "loc_DE2")
    Call(1, 6)
    Jump("loc_E87")

    label("loc_DE2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xB)"), scpexpr(EXPR_END)), "loc_DF1")
    Call(1, 7)
    Jump("loc_E87")

    label("loc_DF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_END)), "loc_E49")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #52
        (
            "\x07\x05试着出示了照片，\x01",
            "但似乎没有见过的印象。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_E87")

    label("loc_E49")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #53
        "\x07\x05附近没有人可以确认照片。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_E87")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_3_D6A end

    def Function_4_E8E(): pass

    label("Function_4_E8E")

    TalkBegin(0xA)

    ChrTalk(    #54
        0xA,
        (
            "唔，１０年前的战役中\x01",
            "行踪不明的人吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        (
            "十分遗憾，\x01",
            "看来我帮不上忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xA,
        (
            "请去问问别人看吧。\x01",
            "说不定能找到线索。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_4_E8E end

    def Function_5_F0E(): pass

    label("Function_5_F0E")

    TalkBegin(0x12)

    ChrTalk(    #57
        0x12,
        "寻找战争孤儿吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x12,
        "嗨，真令人心痛啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x12,
        (
            "一回忆起当时的事\x01",
            "现在还心如刀绞呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_5_F0E end

    def Function_6_F6C(): pass

    label("Function_6_F6C")

    TalkBegin(0xE)

    ChrTalk(    #60
        0xE,
        (
            "百日战役的时候许多\x01",
            "这样的孩子都成了孤儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xE,
        (
            "无论用什么理由开脱，\x01",
            "那都是彻头彻尾的错事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xE,
        (
            "不管是谁看见这张照片，\x01",
            "都应该会注意到……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_6_F6C end

    def Function_7_1002(): pass

    label("Function_7_1002")

    TalkBegin(0xB)

    ChrTalk(    #63
        0xB,
        (
            "那个照片里的孩子\x01",
            "竟然是在战争中失踪的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xB,
        (
            "真可怕啊……\x01",
            "我曾经也有个女儿……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_7_1002 end

    SaveToFile()

Try(main)
