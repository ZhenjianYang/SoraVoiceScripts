from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4135_1 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4135.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T4135_1 ._SN',
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
        "Function_1_29D",          # 01, 1
        "Function_2_41B",          # 02, 2
        "Function_3_968",          # 03, 3
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(500)
    OP_6D(7120, 4000, -2220, 0)
    OP_67(0, 6860, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(52000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 6870, 4000, -2400, 192)
    SetChrPos(0x105, 6210, 4000, -1560, 181)
    SetChrPos(0x104, 7220, 4000, -1410, 180)
    SetChrPos(0x108, 6750, 4000, -500, 197)
    SetChrPos(0x9, 7000, 4000, -3740, 0)
    SetChrSubChip(0x9, 0)
    OP_0D()

    ChrTalk(    #0
        0x9,
        "啊，你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1000F你好，我们是游击士协会的人。\x02\x03",

            "看了公告板上的任务委托\x01",
            "而来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x9,
        "哦哦，正等着呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        (
            "我这就说明委托的事\x01",
            "可以吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_237")
    Call(1, 2)
    Jump("loc_29A")

    label("loc_237")


    ChrTalk(    #4
        0x101,
        (
            "#1016F嗯～对不起。\x02\x03",

            "现在暂时手头没空。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        "是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x9,
        (
            "那么下次有机会\x01",
            "麻烦再来好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0xC4, 0x1, 0x8000)

    label("loc_29A")

    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_29D(): pass

    label("Function_1_29D")

    EventBegin(0x0)
    Fade(500)
    OP_6D(7120, 4000, -2220, 0)
    OP_67(0, 6860, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(52000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 6870, 4000, -2400, 192)
    SetChrPos(0x105, 6210, 4000, -1560, 181)
    SetChrPos(0x104, 7220, 4000, -1410, 180)
    SetChrPos(0x108, 6750, 4000, -500, 197)
    SetChrPos(0x9, 7000, 4000, -3740, 0)
    SetChrSubChip(0x9, 0)
    OP_0D()

    ChrTalk(    #7
        0x9,
        (
            "哎呀，可以\x01",
            "听我的委托了吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B5")
    Call(1, 2)
    Jump("loc_418")

    label("loc_3B5")


    ChrTalk(    #8
        0x101,
        (
            "#1016F嗯～对不起。\x02\x03",

            "现在暂时手头没空。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        "是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x9,
        (
            "那么下次有机会\x01",
            "麻烦再来好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0xC4, 0x1, 0x8000)

    label("loc_418")

    EventEnd(0x0)
    Return()

    # Function_1_29D end

    def Function_2_41B(): pass

    label("Function_2_41B")


    ChrTalk(    #11
        0x101,
        (
            "#1000F嗯嗯，没问题了。\x02\x03",

            "#1002F那么……\x01",
            "到底是什么被偷了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x9,
        "这可怎么说……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)

    ChrTalk(    #13
        0x9,
        (
            "你们看这附近\x01",
            "不觉得有什么不协调吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4A6():
        OP_8C(0x101, 135, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4A6)
    Sleep(100)

    def lambda_4B9():
        OP_8C(0x105, 135, 400)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4B9)
    Sleep(100)

    def lambda_4CC():
        OP_8C(0x104, 135, 400)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4CC)
    Sleep(50)

    def lambda_4DF():
        OP_8C(0x108, 135, 400)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_4DF)
    WaitChrThread(0x108, 0x2)

    ChrTalk(    #14
        0x101,
        (
            "#1015F不协调……？\x02\x03",

            "这里是展示\x01",
            "飞船照片的展馆吧。\x02\x03",

            "嗯～你这么一说\x01",
            "是感觉少了点什么……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x105,
        (
            "#042F……明白了。\x02\x03",

            "记得那边的墙壁上\x01",
            "本来是装饰着\x01",
            "『埃尔赛尤』的照片的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #16
        0x101,
        "#1004F啊，这么说来……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x104,
        (
            "#030F唔，我在参观王都时，\x01",
            "也记得在这里见过照片。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x108,
        (
            "#072F这么说，被盗的\x01",
            "就是那幅埃尔赛尤的照片吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)

    ChrTalk(    #19
        0x9,
        "唔，你观察得没错。\x02",
    )

    CloseMessageWindow()

    def lambda_65E():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_65E)
    Sleep(100)

    def lambda_671():
        OP_8C(0x105, 180, 400)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_671)
    Sleep(100)

    def lambda_684():
        OP_8C(0x104, 180, 400)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_684)
    Sleep(50)

    def lambda_697():
        OP_8C(0x108, 180, 400)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_697)
    WaitChrThread(0x108, 0x2)

    ChrTalk(    #20
        0x9,
        (
            "早上确实还在的\x01",
            "过了中午，不知\x01",
            "什么时候就不见了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        (
            "取而代之的是这张卡\x01",
            "贴在墙上。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #22
        (
            "\x07\x05　　美丽的公主及其随从啊。　　\x01",
            "　　 高尚的白鹰的剪影画\x01",
            "　　    飘落在我手中。　　\x02\x03",

            "　　  如果就想要寻求它\x01",
            "　　  就要回应我的挑战。 　\x02\x03",

            "　  第一把钥匙在老将之居。　　\x01",
            "　 探索『时间的旁观者』吧。　　\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #23
        0x101,
        (
            "#1007F哦……\x01",
            "又是那家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x105,
        "#045F伤、伤脑筋啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x104,
        (
            "#035F呼，看来他已经\x01",
            "燃起了针对我的抗争心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x108,
        (
            "#073F怪盗绅士布卢布兰……\x01",
            "『噬身之蛇』的执行者吗。\x02\x03",

            "#072F传闻倒是听过，\x01",
            "好像是个相当特立独行的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x9,
        (
            "嗬，已经有\x01",
            "犯人的线索了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "这真令人振奋。\x01",
            "就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        (
            "#1000F嗯，知道了。\x02\x03",

            "那么马上就去\x01",
            "调查如何呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0xC4, 0x4, 0x4)
    OP_28(0xC4, 0x4, 0x8)
    OP_28(0xC4, 0x1, 0x1)
    OP_28(0xC4, 0x1, 0x2)
    Return()

    # Function_2_41B end

    def Function_3_968(): pass

    label("Function_3_968")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(7120, 4000, 4420, 0)
    OP_67(0, 6860, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(52000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 6870, 4000, -2400, 192)
    SetChrPos(0x105, 6210, 4000, -1560, 181)
    SetChrPos(0x104, 7220, 4000, -1410, 180)
    SetChrPos(0x108, 6750, 4000, -500, 197)
    SetChrPos(0x9, 7000, 4000, -3740, 0)
    SetChrSubChip(0x9, 0)
    OP_4A(0x9, 255)
    OP_72(0x1, 0x4)
    FadeToBright(1000, 0)
    OP_6D(7120, 4000, -2220, 4000)

    ChrTalk(    #30
        0x9,
        "呀，真是帮大忙了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        (
            "可是，那个怪盗什么的\x01",
            "为什么要偷埃尔赛尤的照片\x01",
            "这种东西呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "虽然是很棒，但也不过是照片，\x01",
            "也没多大价值嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1015F唉，一定要说的话\x01",
            "就是算是故意\x01",
            "怄我们生气吧……\x02\x03",

            "#1013F因为这个，实在抱歉。\x01",
            "或许是把您卷进来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "哈哈，不必道歉。\x01",
            "又不是你们干的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x9,
        "总之真是辛苦了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #36
        "\x07\x02任务【消失的展览品】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0xC4, 0x4, 0x10)
    OP_28(0xC4, 0x1, 0x200)
    OP_A2(0x3)
    OP_4B(0x9, 255)
    SetChrPos(0x9, 7000, 4000, -3740, 90)
    EventEnd(0x0)
    Return()

    # Function_3_968 end

    SaveToFile()

Try(main)
