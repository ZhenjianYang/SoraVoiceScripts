from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1131_2 ._SN',
        MapName             = 'Bose',
        Location            = 'T1131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        "Function_1_FA9",          # 01, 1
        "Function_2_102A",         # 02, 2
        "Function_3_12B4",         # 03, 3
        "Function_4_1752",         # 04, 4
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0xA, 255)
    SetChrPos(0xA, -47710, 0, 44840, 270)
    SetChrPos(0x101, -46020, 0, 44370, 270)
    SetChrPos(0xF7, -45610, 0, 45370, 270)
    SetChrPos(0xF8, -44250, 0, 45330, 270)
    SetChrPos(0xF9, -44580, 0, 44110, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_127")
    SetChrPos(0x4, -43430, 0, 44650, 270)

    label("loc_127")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_139")
    OP_8C(0xA, 90, 0)

    label("loc_139")

    OP_6D(-46490, 0, 45440, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E7")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇QST018完成】\x01",        # 0
            "【◇QST018未完成】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D7"),
        (1, "loc_1DF"),
        (SWITCH_DEFAULT, "loc_1E7"),
    )


    label("loc_1D7")

    OP_28(0x12, 0x4, 0x10)
    Jump("loc_1E7")

    label("loc_1DF")

    OP_28(0x12, 0x3, 0x10)
    Jump("loc_1E7")

    label("loc_1E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_28D")

    ChrTalk(    #0
        0xA,
        "哎呀，游击士们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xA,
        (
            "委托你们工作\x01",
            "没问题了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28A")

    ChrTalk(    #2
        0x101,
        (
            "#1007F抱歉，还不行。\x02\x03",

            "#1002F我们还会再来的，\x01",
            "那时再说吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x7B, 0x1, 0x1000)
    EventEnd(0x0)
    OP_4B(0xA, 255)
    OP_44(0xA, 0x0)
    OP_43(0xA, 0x0, 0x0, 0x2)
    Return()

    label("loc_28A")

    Jump("loc_51F")

    label("loc_28D")

    ClearChrFlags(0xA, 0x10)
    OP_8C(0xA, 90, 400)

    ChrTalk(    #3
        0xA,
        "是，什么事？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_37B")

    ChrTalk(    #4
        0x101,
        (
            "#1000F嗯，我们是看了\x01",
            "公告板来的……\x02\x03",

            "你是格露娜小姐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xA,
        "嗯嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xA,
        "哎呀？你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xA,
        (
            "不是之前\x01",
            "帮我收集食材的人吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1017F嘿嘿，好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xA,
        (
            "啊哈哈，看来\x01",
            "好像很有缘呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F1")

    label("loc_37B")


    ChrTalk(    #10
        0x101,
        (
            "#1000F嗯，我们是看了\x01",
            "公告板来的……\x02\x03",

            "你是格露娜小姐？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xA,
        "嗯嗯，我就是格露娜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xA,
        (
            "是游击士们吧。\x01",
            "正等你们呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F1")


    ChrTalk(    #13
        0xA,
        (
            "事不宜迟，\x01",
            "可以帮忙工作了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51F")

    ChrTalk(    #14
        0x101,
        (
            "#1006F嗯，当然。\x02\x03",

            "#1007F……虽然想马上开始，\x01",
            "但其实还有些急事要做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xA,
        (
            "是吗……\x01",
            "因为那个龙的骚乱事件吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xA,
        (
            "那样就没办法了。\x01",
            "有空了请再来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xA,
        (
            "也不是什么紧急的工作，\x01",
            "不用着急的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1002F抱歉。\x01",
            "那，我们会再来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x7B, 0x1, 0x1000)
    EventEnd(0x0)
    OP_4B(0xA, 255)
    OP_44(0xA, 0x0)
    OP_43(0xA, 0x0, 0x0, 0x2)
    Return()

    label("loc_51F")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_652")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_5B5")

    ChrTalk(    #19
        0x101,
        (
            "#1007F抱歉，还不行。\x02\x03",

            "我们会再来的，\x01",
            "那时再说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63A")

    label("loc_5B5")


    ChrTalk(    #20
        0x101,
        (
            "#1015F嗯……抱歉。\x01",
            "现在有点不方便。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xA,
        "哎呀呀，这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xA,
        (
            "嗯，明白了。\x01",
            "有空了请再来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1007F抱歉。\x01",
            "那就先这样吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63A")

    OP_28(0x7B, 0x1, 0x1000)
    EventEnd(0x0)
    OP_4B(0xA, 255)
    OP_44(0xA, 0x0)
    OP_43(0xA, 0x0, 0x0, 0x2)
    Return()

    label("loc_652")


    ChrTalk(    #24
        0x101,
        (
            "#1006F嗯，没问题。\x02\x03",

            "#1015F公告板上面写着\x01",
            "收集食材的工作吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xA,
        "嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xA,
        (
            "为了研究新菜单，\x01",
            "我需要稀有的食材。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        (
            "而且，还想顺便\x01",
            "麻烦收集其他的食材。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_747")

    ChrTalk(    #28
        0xA,
        (
            "倒不是很紧急的工作，\x01",
            "但时间也不多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xA,
        (
            "所以请各位\x01",
            "尽快解决吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_835")

    label("loc_747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_7A3")

    ChrTalk(    #30
        0xA,
        (
            "由于龙的骚乱事件\x01",
            "大家都很忙吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xA,
        (
            "不是什么紧急的工作，\x01",
            "有空的时候再来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_835")

    label("loc_7A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_803")

    ChrTalk(    #32
        0xA,
        (
            "似乎发生了什么事件，\x01",
            "大家都很忙吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "不是什么紧急的工作，\x01",
            "有空的时候再来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_835")

    label("loc_803")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_835")

    ChrTalk(    #34
        0xA,
        (
            "也不是紧急的工作，\x01",
            "有空的时候再来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_835")


    ChrTalk(    #35
        0x101,
        "#1006F原来如此，明白了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B9")

    ChrTalk(    #36
        0x106,
        (
            "#050F那么，说明一下\x01",
            "寻找食材的方法吧。\x02\x03",

            "因为必要的食材清单里\x01",
            "也有很稀有的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EC")

    label("loc_8B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_921")

    ChrTalk(    #37
        0x103,
        (
            "#020F那么，能说明一下\x01",
            "寻找食材的方法吗？\x02\x03",

            "因为必要的食材清单里\x01",
            "也有很稀有的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EC")

    label("loc_921")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_987")

    ChrTalk(    #38
        0x108,
        (
            "#070F那么，说明一下\x01",
            "寻找食材的方法吧。\x02\x03",

            "因为必要的食材清单里\x01",
            "也有很稀有的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EC")

    label("loc_987")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9EC")

    ChrTalk(    #39
        0x104,
        (
            "#030F那么，不说明一下\x01",
            "寻找食材的方法吗？\x02\x03",

            "因为必要的食材清单里\x01",
            "也有很稀有的东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EC")


    ChrTalk(    #40
        0x101,
        (
            "#1011F啊，这个得确认一下。\x02\x03",

            "#1015F例如『魔兽之骨』什么的，\x01",
            "好像还挺难弄到的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xA,
        (
            "难得到的有\x01",
            "『魔兽之骨』和『魔兽之角』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        (
            "其它特别该举出来的，\x01",
            "就是『魔兽之牙』什么的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1002F这些全部\x01",
            "都能在柏斯地区弄到吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xA,
        (
            "嗯嗯，应该是的。\x01",
            "大致的魔兽身上都有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        (
            "首先，『魔兽之骨』\x01",
            "应该能在迷雾峡谷找到哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xA,
        (
            "而『魔兽之角』\x01",
            "在北边的拉文努山道……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        (
            "最后的『魔兽之牙』也\x01",
            "能在古罗尼山顶弄到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1007F地、地方都散落各处呢。\x02\x03",

            "这搞不好挺麻烦的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        "呼呼，那是当然的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xA,
        (
            "正因为麻烦，\x01",
            "才这样委托各位嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#1008F啊……说得也是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xA,
        (
            "如果食材全部集齐了，\x01",
            "就请拿来这里吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        "麻烦请集齐了再来哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xA,
        (
            "分别拿来也不会接受的，\x01",
            "这点请注意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1006F一个不少的集齐了\x01",
            "交来这里就行了吧？\x02\x03",

            "的确，这样我们\x01",
            "也少费点工夫。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D3A")

    ChrTalk(    #56
        0x109,
        (
            "#1066F嗯，只要不自己偷吃掉\x01",
            "就没问题了。\x02\x03",

            "还有，做饭的时候\x01",
            "要注意所使用的食材哟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB3")

    label("loc_D3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D98")

    ChrTalk(    #57
        0x104,
        (
            "#035F呼，这么说\x01",
            "就是严禁我们先偷吃吧。\x02\x03",

            "做饭的时候\x01",
            "要注意所使用的食材。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB3")

    label("loc_D98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DF4")

    ChrTalk(    #58
        0x108,
        (
            "#070F哈哈，这么一来\x01",
            "就严禁偷吃了哟。\x02\x03",

            "做饭的时候\x01",
            "要注意所使用的食材。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB3")

    label("loc_DF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E54")

    ChrTalk(    #59
        0x103,
        (
            "#027F嗯嗯，只要某人\x01",
            "不先偷吃就行了。\x02\x03",

            "做料理的时候\x01",
            "要注意所使用的食材啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB3")

    label("loc_E54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB3")

    ChrTalk(    #60
        0x106,
        (
            "#053F啊啊，只要某人\x01",
            "不先偷吃就行。\x02\x03",

            "在外边做饭的时候\x01",
            "要注意所使用的食材哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB3")


    ChrTalk(    #61
        0x101,
        "#1016F啊哈哈，这个确实……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xA,
        (
            "没有别的问题了？\x01",
            "没有的话我就回去工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#1015F嗯，取得食材的地方\x01",
            "和交付方法都问了……\x02\x03",

            "#1006F嗯，我想没问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xA,
        "那就拜托你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xA,
        "我就在这里等吧。\x02",
    )

    CloseMessageWindow()
    OP_28(0x7B, 0x1, 0x1)
    OP_28(0x7B, 0x1, 0x2)
    OP_28(0x7B, 0x1, 0x4)
    OP_28(0x7B, 0x4, 0x4)
    OP_28(0x7B, 0x4, 0x8)
    EventEnd(0x0)
    OP_4B(0xA, 255)
    OP_44(0xA, 0x0)
    OP_43(0xA, 0x0, 0x0, 0x2)
    Return()

    # Function_0_AA end

    def Function_1_FA9(): pass

    label("Function_1_FA9")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【说话】\x01",          # 0
            "【展示食材】\x01",      # 1
            "【离开】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1013")
    Call(0, 9)
    Return()

    label("loc_1013")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1028")
    Call(2, 2)
    Return()

    label("loc_1028")

    Return()

    # Function_1_FA9 end

    def Function_2_102A(): pass

    label("Function_2_102A")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0xA, 255)
    SetChrPos(0xA, -47710, 0, 44840, 90)
    SetChrPos(0x101, -46020, 0, 44370, 270)
    SetChrPos(0xF7, -45610, 0, 45370, 270)
    SetChrPos(0xF8, -44250, 0, 45330, 270)
    SetChrPos(0xF9, -44580, 0, 44110, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10A7")
    SetChrPos(0x4, -43430, 0, 44650, 270)

    label("loc_10A7")

    OP_6D(-46490, 0, 45440, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #66
        0xA,
        (
            "哎呀，把食材\x01",
            "拿来了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_112D")

    ChrTalk(    #67
        0x101,
        "#1002F嗯，你确认一下。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1149")

    label("loc_112D")


    ChrTalk(    #68
        0x101,
        "#1006F嗯，你确认一下。\x02",
    )

    CloseMessageWindow()

    label("loc_1149")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #69
        "\x07\x05向格露娜展示了食材。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_11BD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "OP_40(0x3A9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x3A2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11BA")
    Call(2, 3)
    Return()

    label("loc_11BA")

    Jump("loc_120D")

    label("loc_11BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3A7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_EXEC_OP, "OP_40(0x3A9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x3A2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x39E, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x3A3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x3A1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_120D")
    Call(2, 3)
    Return()

    label("loc_120D")


    ChrTalk(    #70
        0xA,
        "嗯～很抱歉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        "食材好像没齐呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1004F啊，是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        "嗯嗯，没错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xA,
        (
            "再确认一次\x01",
            "需要的食材吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#1015F是吗……\x02\x03",

            "那下次再来吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_4B(0xA, 255)
    OP_44(0xA, 0x0)
    OP_43(0xA, 0x0, 0x0, 0x2)
    Return()

    # Function_2_102A end

    def Function_3_12B4(): pass

    label("Function_3_12B4")


    ChrTalk(    #76
        0xA,
        (
            "嗯……\x01",
            "全部集齐了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xA,
        (
            "那么，\x01",
            "我就收下了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1386")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #78
        "\x1F\xA7\x03\x07\x00交付了１０个。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #79
        "\x1F\xA2\x03\x07\x00交付了１０个。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #80
        "\x1F\xA9\x03\x07\x00交付了１０个。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x3A7, 10)
    OP_3F(0x3A2, 10)
    OP_3F(0x3A9, 10)
    Jump("loc_1479")

    label("loc_1386")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #81
        "\x1F\x9E\x03\x07\x00交付了５个。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #82
        "\x1F\xA3\x03\x07\x00交付了５个。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #83
        "\x1F\xA1\x03\x07\x00交付了５个。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #84
        "\x1F\xA7\x03\x07\x00交付了１０个。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #85
        "\x1F\xA2\x03\x07\x00交付了１０个。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #86
        "\x1F\xA9\x03\x07\x00交付了１０个。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x39E, 5)
    OP_3F(0x3A3, 5)
    OP_3F(0x3A1, 5)
    OP_3F(0x3A7, 10)
    OP_3F(0x3A2, 10)
    OP_3F(0x3A9, 10)

    label("loc_1479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15A4")

    ChrTalk(    #87
        0x101,
        (
            "#1002F好，这样委托就完成了吧。\x02\x03",

            "那，格露娜……\x01",
            "不好意思，我们这就告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xA,
        "看来好像很急呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        (
            "难道你们\x01",
            "因为刚才那龙的事……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        "#1002F嗯，有紧急的事呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        (
            "是吗……\x01",
            "那就不留你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xA,
        (
            "今天谢谢你们帮忙了。\x01",
            "你们也要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1006F谢谢了。\x02\x03",

            "格露娜也加油哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_172F")

    label("loc_15A4")


    ChrTalk(    #94
        0x101,
        "#1007F呼～这样就完成委托了吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xA,
        "呵呵，辛苦辛苦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xA,
        (
            "百忙之中真是谢谢你们了。\x01",
            "多亏你们帮了大忙。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1645")

    ChrTalk(    #97
        0xA,
        (
            "还连商人\x01",
            "也顺便介绍过来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_2B(0x7B, 0x2)
    OP_2C(0x7B, 0x5DC)

    label("loc_1645")


    ChrTalk(    #98
        0x101,
        (
            "#1001F嘿嘿，别介意。\x02\x03",

            "能帮上忙就再好不过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xA,
        (
            "如果有空\x01",
            "请务必来我家做客。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xA,
        (
            "那，今后\x01",
            "也请努力工作哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        (
            "#1006F嗯，谢谢。\x02\x03",

            "格露娜也加油哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #102
        "\x07\x02任务【美味的调制】\x07\x00完成了！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_172F")

    OP_28(0x7B, 0x1, 0x20)
    OP_28(0x7B, 0x4, 0x10)
    OP_A2(0x3)
    OP_A2(0xB)
    EventEnd(0x0)
    OP_4B(0xA, 255)
    OP_44(0xA, 0x0)
    OP_43(0xA, 0x0, 0x0, 0x2)
    Return()

    # Function_3_12B4 end

    def Function_4_1752(): pass

    label("Function_4_1752")

    EventBegin(0x0)
    ClearChrFlags(0x11, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0x11, 255)
    SetChrPos(0xA, -47710, 0, 44840, 90)
    SetChrPos(0x11, -46020, 0, 44840, 270)
    SetChrPos(0x101, -44910, 0, 44600, 270)
    SetChrPos(0xF7, -44680, 0, 45560, 270)
    SetChrPos(0xF8, -43250, 0, 45520, 270)
    SetChrPos(0xF9, -43450, 0, 44560, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17E4")
    SetChrPos(0x4, -42250, 0, 45000, 270)

    label("loc_17E4")

    OP_6D(-46490, 0, 45440, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #103
        0xA,
        "──嗯，品质也没有问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xA,
        (
            "那么，这里的食材\x01",
            "我就先收下了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #105
        (
            "\x07\x05『魔兽之骨』，『魔兽之角』，\x01",
            "『魔兽之牙』都交给了格露娜。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #106
        0x101,
        (
            "#1000F呼，得救了。\x02\x03",

            "这下很麻烦的食材\x01",
            "就全部收齐了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xA,
        "嗯嗯，是呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xA,
        (
            "拜托你们找\x01",
            "剩下的食材吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#1006F嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xA,
        "话虽如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xA,
        (
            "这么珍稀的食材\x01",
            "竟然有库存呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x11,
        (
            "哈哈哈，那当然啦。\x02\x03",

            "怎么说本商会可是\x01",
            "专业出售高级食材的嘛。\x02\x03",

            "跟那些普通的小食品店\x01",
            "进的货品可不一样。\x02\x03",

            "需要什么的时候，\x01",
            "请再联络本商会吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xA,
        "一定会的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xA,
        (
            "本来还想介绍给厨师长，\x01",
            "但现在他比较忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xA,
        (
            "十分抱歉，\x01",
            "能在这里稍等片刻吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x11,
        (
            "好说好说，多长时间\x01",
            "我都等。\x02\x03",

            "……那么，一会儿见。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_8E(0x11, 0xFFFF4C0A, 0x0, 0xB518, 0x7D0, 0x0)

    def lambda_1AC4():

        label("loc_1AC4")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1AC4")

    QueueWorkItem2(0xF6, 1, lambda_1AC4)

    def lambda_1AD5():

        label("loc_1AD5")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1AD5")

    QueueWorkItem2(0xF7, 1, lambda_1AD5)

    def lambda_1AE6():

        label("loc_1AE6")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1AE6")

    QueueWorkItem2(0xF8, 1, lambda_1AE6)

    def lambda_1AF7():

        label("loc_1AF7")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1AF7")

    QueueWorkItem2(0xF9, 1, lambda_1AF7)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B1F")

    def lambda_1B14():

        label("loc_1B14")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B14")

    QueueWorkItem2(0x4, 1, lambda_1B14)

    label("loc_1B1F")

    OP_8E(0x11, 0xFFFF5AA6, 0x0, 0xB518, 0x7D0, 0x0)
    OP_8E(0x11, 0xFFFF5EF2, 0x0, 0xB0C2, 0x7D0, 0x0)
    OP_8E(0x11, 0xFFFF70CC, 0x0, 0xAF28, 0x7D0, 0x0)
    OP_44(0xF6, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B7B")
    OP_44(0x4, 0x1)

    label("loc_1B7B")

    SetChrPos(0x11, -33640, 0, 42550, 0)

    def lambda_1B92():
        OP_8C(0xF6, 270, 400)
        ExitThread()

    QueueWorkItem(0xF6, 1, lambda_1B92)

    def lambda_1BA0():
        OP_8C(0xF7, 270, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1BA0)
    Sleep(100)

    def lambda_1BB3():
        OP_8C(0xF8, 270, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1BB3)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BD5")

    def lambda_1BCD():
        OP_8C(0x4, 270, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_1BCD)

    label("loc_1BD5")

    OP_8C(0xF9, 270, 400)

    ChrTalk(    #117
        0xA,
        (
            "好了，剩下的食材\x01",
            "大多是简单的东西了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xA,
        (
            "那么各位，\x01",
            "还需要再麻烦你们一下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x7B, 0x1, 0x8)
    OP_28(0x7B, 0x1, 0x10)
    EventEnd(0x0)
    OP_4B(0xA, 255)
    OP_44(0xA, 0x0)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_4B(0x11, 255)
    Return()

    # Function_4_1752 end

    SaveToFile()

Try(main)
