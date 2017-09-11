from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T2500_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2500.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
    )

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_3C6",          # 01, 1
        "Function_2_D64",          # 02, 2
        "Function_3_179C",         # 03, 3
    )


    def Function_0_66(): pass

    label("Function_0_66")

    EventBegin(0x0)
    Fade(1000)
    OP_6C(135000, 0)
    OP_0D()

    ChrTalk(    #0
        0xFE,
        "*sigh*... I'm bushed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "At this rate, I'll never finish\x01",
            "getting these decorations up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "And all the students who\x01",
            "were helping me are busy\x01",
            "with other stuff.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 135, 400)

    ChrTalk(    #3
        0xFE,
        (
            "Just look around. There are\x01",
            "still plenty of places that\x01",
            "aren't decorated yet.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17E():
        OP_6D(49960, 1500, 53870, 2000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17E)
    Sleep(100)
    OP_8B(0x101, 0xC328, 0xD26E, 0x190)
    Sleep(150)
    OP_8B(0x105, 0xC328, 0xD26E, 0x190)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CF")
    OP_8B(0x13B, 0xC328, 0xD26E, 0x190)

    label("loc_1CF")

    WaitChrThread(0xFE, 0x1)

    ChrTalk(    #4
        0x101,
        (
            "#004FUh-oh...\x01",
            "There's no center curtain.\x02\x03",

            "#003FThat might not look so good.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #5
        0xFE,
        "See what I mean?\x02",
    )

    CloseMessageWindow()

    def lambda_248():
        OP_69(0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_248)
    Sleep(100)
    TurnDirection(0x101, 0xFE, 400)
    Sleep(100)
    TurnDirection(0x105, 0xFE, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27D")
    TurnDirection(0x13B, 0xFE, 400)

    label("loc_27D")

    WaitChrThread(0xFE, 0x1)

    ChrTalk(    #6
        0xFE,
        (
            "If you see any other bare\x01",
            "spots like that, please let\x01",
            "me know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "I'll be over to get them\x01",
            "fixed up in a jiffy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I think you know what to\x01",
            "keep an eye out for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#000FAny place like this, where\x01",
            "there are no decorations.\x02\x03",

            "I've got it. If I spot any,\x01",
            "I'll let you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "I appreciate it.\x02",
    )

    CloseMessageWindow()
    OP_28(0x27, 0x1, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    EventEnd(0x1)
    Return()

    # Function_0_66 end

    def Function_1_3C6(): pass

    label("Function_1_3C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D60")
    EventBegin(0x0)
    Fade(1000)
    OP_6C(225000, 0)
    SetChrPos(0x101, 21320, 250, 26540, 180)
    SetChrPos(0x105, 21880, 0, 27550, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_423")
    SetChrPos(0x13B, 20790, 0, 27100, 180)

    label("loc_423")

    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #11
        0x101,
        (
            "#004FHuh...?\x02\x03",

            "There's no flag here...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47E")
    TurnDirection(0x101, 0x13B, 400)
    Jump("loc_485")

    label("loc_47E")

    TurnDirection(0x101, 0x105, 400)

    label("loc_485")


    ChrTalk(    #12
        0x101,
        (
            "#002FSee, the other buildings have\x01",
            "flags over the doors.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_556")

    ChrTalk(    #13
        0x13B,
        (
            "#643FNow that you mention it...\x02\x03",

            "I guess this spot isn't\x01",
            "finished, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x105,
        "#040FLet's go tell Mr. Parkes about it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)
    Jump("loc_5D4")

    label("loc_556")


    ChrTalk(    #15
        0x105,
        (
            "#044FSo it would seem. I suppose\x01",
            "that the decorating isn't\x01",
            "finished here, then.\x02\x03",

            "#040FLet's go tell Mr. Parkes about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D4")


    ChrTalk(    #16
        0x101,
        "#000FOkay.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x15, 30130, 0, 28910, 270)
    SetChrPos(0x101, 22450, 0, 27570, 180)
    SetChrPos(0x105, 21590, 0, 28160, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_641")
    SetChrPos(0x13B, 20300, 0, 27960, 90)

    label("loc_641")

    OP_8C(0x101, 90, 0)
    OP_8C(0x105, 90, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_664")
    OP_8C(0x13B, 90, 0)

    label("loc_664")

    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrFlags(0x15, 0x40)
    OP_8E(0x15, 0x5F3C, 0x0, 0x6CC0, 0xBB8, 0x0)
    OP_8E(0x15, 0x5BEA, 0x0, 0x6A5E, 0xBB8, 0x0)
    OP_4A(0x15, 255)
    Sleep(400)
    OP_8C(0x15, 225, 400)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #17
        0x15,
        "Ah, you're right. Nice catch.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(    #18
        0x15,
        "Okay, I'll go take care of it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_768")
    TurnDirection(0x13B, 0x101, 400)

    ChrTalk(    #19
        0x13B,
        "#644FWhy don't we come and help?\x02",
    )

    CloseMessageWindow()

    def lambda_756():
        TurnDirection(0x105, 0x13B, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_756)
    TurnDirection(0x101, 0x13B, 400)
    Jump("loc_795")

    label("loc_768")


    ChrTalk(    #20
        0x105,
        "#040FWhy don't we come and help?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    label("loc_795")


    ChrTalk(    #21
        0x101,
        "#000FYeah, sounds good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x15,
        "Hey, thanks.\x02",
    )

    CloseMessageWindow()

    def lambda_7CA():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7CA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7EE")

    def lambda_7E6():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_7E6)

    label("loc_7EE")

    TurnDirection(0x101, 0x15, 400)

    ChrTalk(    #23
        0x15,
        "I'd be glad for the help.\x02",
    )

    CloseMessageWindow()

    def lambda_81A():
        OP_8E(0x101, 0x57B2, 0x0, 0x6658, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81A)

    def lambda_835():
        OP_8E(0x105, 0x5456, 0x0, 0x6720, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_835)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_873")

    def lambda_85E():
        OP_8E(0x13B, 0x5154, 0xFA, 0x65A4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_85E)

    label("loc_873")


    def lambda_879():
        OP_8E(0x15, 0x5AB4, 0xFA, 0x65B8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_879)

    def lambda_894():
        OP_6C(135000, 2500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_894)
    OP_6D(22030, 3500, 24930, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x105, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8D7")
    WaitChrThread(0x13B, 0x1)

    label("loc_8D7")

    WaitChrThread(0x15, 0x1)
    Sleep(400)
    OP_72(0x1E, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Sleep(400)
    OP_28(0x27, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C08")

    ChrTalk(    #24
        0x15,
        "...All right, that should do it.\x02",
    )

    CloseMessageWindow()
    OP_69(0x101, 0x5DC)
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(    #25
        0x15,
        (
            "Phew... That looks like\x01",
            "the last of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x15,
        "You kids have been a big help.\x02",
    )

    CloseMessageWindow()

    def lambda_9A8():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9A8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9CC")

    def lambda_9C4():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_9C4)

    label("loc_9CC")

    TurnDirection(0x101, 0x15, 400)

    ChrTalk(    #27
        0x101,
        (
            "#000FNo prob.\x02\x03",

            "We all want the festival\x01",
            "to go well, so helping out\x01",
            "isn't a big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x105,
        (
            "#040FThat's right.\x02\x03",

            "It's our festival, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A9C")
    TurnDirection(0x13B, 0x105, 400)

    ChrTalk(    #29
        0x13B,
        "#644FThat's the spirit, Kloe.\x02",
    )

    CloseMessageWindow()

    label("loc_A9C")


    ChrTalk(    #30
        0x15,
        "Ha ha. I suppose you're right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13B, 0x15, 400)

    ChrTalk(    #31
        0x15,
        "I'm looking forward to it myself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#006FJust leave it to us!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B41")

    ChrTalk(    #33
        0x13B,
        "#649FHa ha...glad to hear it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B5E")

    label("loc_B41")


    ChrTalk(    #34
        0x105,
        "#040FWe'll do our best.\x02",
    )

    CloseMessageWindow()

    label("loc_B5E")


    ChrTalk(    #35
        0x15,
        (
            "Got my fingers crossed for\x01",
            "you, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x27, 0x1, 0x10)
    OP_28(0x3D, 0x1, 0x200)
    OP_2C(0x3D, 0x1F4)
    OP_2B(0x3D, 0x1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #36
        (
            "\x07\x00Festival help quest\x01\x07\x02",
            "[Decorate the Campus] \x07\x00completed!\x02",
        )
    )

    OP_83(0x2, 0x2)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_CBD")

    label("loc_C08")


    ChrTalk(    #37
        0x15,
        "...All right, that should do it.\x02",
    )

    CloseMessageWindow()
    OP_69(0x101, 0x5DC)
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(    #38
        0x15,
        "Let me know if you see any more.\x02",
    )

    CloseMessageWindow()

    def lambda_C68():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C68)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C8C")

    def lambda_C84():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_C84)

    label("loc_C8C")

    TurnDirection(0x101, 0x15, 400)

    ChrTalk(    #39
        0x101,
        "#006FSure thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x105,
        "#040FYes, sir.\x02",
    )

    CloseMessageWindow()

    label("loc_CBD")


    def lambda_CC3():

        label("loc_CC3")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_CC3")

    QueueWorkItem2(0x0, 1, lambda_CC3)

    def lambda_CD4():

        label("loc_CD4")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_CD4")

    QueueWorkItem2(0x1, 1, lambda_CD4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CFE")

    def lambda_CF3():

        label("loc_CF3")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_CF3")

    QueueWorkItem2(0x2, 1, lambda_CF3)

    label("loc_CFE")

    OP_8E(0x15, 0x6086, 0x0, 0x6E6E, 0xBB8, 0x0)
    OP_8E(0x15, 0x7A30, 0x0, 0x6D60, 0xBB8, 0x0)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D40")
    OP_44(0x2, 0xFF)

    label("loc_D40")

    SetChrPos(0x15, 47880, 0, 56070, 135)
    ClearChrFlags(0x15, 0x40)
    OP_4B(0x15, 255)
    OP_64(0x3, 0x1)
    EventEnd(0x0)

    label("loc_D60")

    TalkEnd(0xFF)
    Return()

    # Function_1_3C6 end

    def Function_2_D64(): pass

    label("Function_2_D64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1798")
    EventBegin(0x0)
    Fade(1000)
    OP_6C(45000, 0)
    SetChrPos(0x101, 38970, 0, 68950, 90)
    SetChrPos(0x105, 40770, 0, 68550, 45)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DC1")
    SetChrPos(0x13B, 38560, 0, 70140, 90)

    label("loc_DC1")

    OP_0D()
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #41
        0x105,
        "#044FHuh...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E07")

    def lambda_DFF():
        TurnDirection(0x13B, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_DFF)

    label("loc_E07")

    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #42
        0x101,
        "#000FWhat's wrong?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #43
        0x105,
        (
            "#044FDon't you think a tapestry\x01",
            "should go here?\x02\x03",

            "It would look nice, just\x01",
            "opposite the door.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 0, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB2")

    def lambda_EAA():
        OP_8C(0x13B, 0, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_EAA)

    label("loc_EB2")

    OP_8C(0x101, 0, 400)
    OP_6D(41580, 2000, 73990, 1500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F07")

    ChrTalk(    #44
        0x13B,
        (
            "#643FHmm... Now that you\x01",
            "mention it...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F1B")

    label("loc_F07")


    ChrTalk(    #45
        0x101,
        "#004FOh, yeah.\x02",
    )

    CloseMessageWindow()

    label("loc_F1B")

    OP_69(0x105, 0x5DC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F43")
    Sleep(100)

    def lambda_F3B():
        TurnDirection(0x13B, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_F3B)

    label("loc_F43")

    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #46
        0x101,
        "#000FWe should go let Mr. Parkes know.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #47
        0x105,
        "#040FYes, let's.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x15, 45200, 0, 65300, 270)
    SetChrPos(0x101, 39140, 0, 69780, 135)
    SetChrPos(0x105, 38830, 0, 68410, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF5")
    Sleep(100)
    SetChrPos(0x13B, 37730, 0, 69120, 135)

    label("loc_FF5")

    OP_69(0x101, 0x0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_1011():

        label("loc_1011")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1011")

    QueueWorkItem2(0x0, 1, lambda_1011)

    def lambda_1022():

        label("loc_1022")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1022")

    QueueWorkItem2(0x1, 1, lambda_1022)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_104C")

    def lambda_1041():

        label("loc_1041")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1041")

    QueueWorkItem2(0x2, 1, lambda_1041)

    label("loc_104C")

    SetChrFlags(0x15, 0x40)
    OP_8E(0x15, 0x9FE2, 0x0, 0x1046E, 0xBB8, 0x0)
    OP_8E(0x15, 0x9F42, 0x0, 0x10BC6, 0xBB8, 0x0)
    OP_4A(0x15, 255)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1097")
    OP_44(0x2, 0xFF)

    label("loc_1097")

    Sleep(400)
    OP_8C(0x15, 45, 400)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #48
        0x15,
        "Yeah, I see what you mean.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(    #49
        0x15,
        "I'll get right to work on it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1132")

    ChrTalk(    #50
        0x13B,
        "#644FWe'll help.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x13B, 400)
    Jump("loc_1160")

    label("loc_1132")

    TurnDirection(0x101, 0x15, 400)

    ChrTalk(    #51
        0x101,
        "#000FWe'd be glad to help.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    label("loc_1160")


    ChrTalk(    #52
        0x15,
        "Thanks...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x15,
        "I appreciate it.\x02",
    )

    CloseMessageWindow()

    def lambda_118B():
        OP_6C(135000, 4000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_118B)

    def lambda_119B():
        OP_8E(0x101, 0xA028, 0x0, 0x111FC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_119B)

    def lambda_11B6():
        OP_8E(0x105, 0x9F42, 0x0, 0x10BC6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11B6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11F4")

    def lambda_11DF():
        OP_8E(0x13B, 0x9CC2, 0x0, 0x10F04, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_11DF)

    label("loc_11F4")


    def lambda_11FA():
        OP_6D(41770, 3500, 69260, 4000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_11FA)
    OP_8E(0x15, 0x9FE2, 0x0, 0x107AC, 0x7D0, 0x0)
    OP_8E(0x15, 0x9506, 0x0, 0x109A0, 0x7D0, 0x0)
    FadeToDark(1000, 0, -1)
    OP_8E(0x15, 0x959C, 0x0, 0x11A9E, 0xBB8, 0x0)
    OP_72(0x5, 0x2)
    OP_6F(0x5, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x105, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_127C")
    WaitChrThread(0x13B, 0x1)

    label("loc_127C")

    WaitChrThread(0x15, 0x1)
    WaitChrThread(0x15, 0x2)
    OP_72(0x12, 0x4)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x15, 43990, 0, 73850, 270)
    OP_6F(0x5, 60)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12C7")
    SetChrPos(0x13B, 41160, 0, 69290, 90)

    label("loc_12C7")

    FadeToBright(1000, 0)
    OP_8E(0x15, 0xA258, 0x1F4, 0x121EC, 0xBB8, 0x0)
    OP_72(0x5, 0x800)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)
    OP_8E(0x15, 0x959C, 0x0, 0x11A9E, 0xBB8, 0x0)
    OP_8E(0x15, 0x9470, 0x0, 0x10BC6, 0xBB8, 0x0)
    OP_8C(0x15, 90, 400)
    OP_71(0x5, 0x800)
    Sleep(400)
    OP_28(0x27, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_163B")

    ChrTalk(    #54
        0x15,
        "Okay, that should do it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    def lambda_1381():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1381)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A5")

    def lambda_139D():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_139D)

    label("loc_13A5")

    TurnDirection(0x101, 0x15, 400)
    OP_69(0x101, 0x5DC)

    ChrTalk(    #55
        0x15,
        (
            "Phew... That looks like the\x01",
            "last of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x15,
        "You kids have been a big help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#000FNo prob.\x02\x03",

            "We all want the festival\x01",
            "to go well, so helping out\x01",
            "isn't a big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x105,
        (
            "#040FThat's right.\x02\x03",

            "It's our festival, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14CF")
    TurnDirection(0x13B, 0x105, 400)

    ChrTalk(    #59
        0x13B,
        "#644FThat's the spirit, Kloe.\x02",
    )

    CloseMessageWindow()

    label("loc_14CF")


    ChrTalk(    #60
        0x15,
        "Ha ha. I suppose you're right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13B, 0x15, 400)

    ChrTalk(    #61
        0x15,
        "I'm looking forward to it myself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#006FJust leave it to us!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1574")

    ChrTalk(    #63
        0x13B,
        "#649FHa ha...glad to hear it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1591")

    label("loc_1574")


    ChrTalk(    #64
        0x105,
        "#040FWe'll do our best.\x02",
    )

    CloseMessageWindow()

    label("loc_1591")


    ChrTalk(    #65
        0x15,
        (
            "Got my fingers crossed for\x01",
            "you, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x27, 0x1, 0x10)
    OP_28(0x3D, 0x1, 0x200)
    OP_2C(0x3D, 0x1F4)
    OP_2B(0x3D, 0x1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #66
        (
            "\x07\x00Festival help quest\x01\x07\x02",
            "[Decorate the Campus] \x07\x00completed!\x02",
        )
    )

    OP_83(0x2, 0x2)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_16F0")

    label("loc_163B")


    ChrTalk(    #67
        0x15,
        "...All right, that should do it.\x02",
    )

    CloseMessageWindow()

    def lambda_1667():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1667)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_168B")

    def lambda_1683():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_1683)

    label("loc_168B")

    TurnDirection(0x101, 0x15, 400)
    OP_69(0x101, 0x5DC)
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(    #68
        0x15,
        "Let me know if you see any more.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#006FSure thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x105,
        "#040FYes, sir.\x02",
    )

    CloseMessageWindow()

    label("loc_16F0")


    def lambda_16F6():

        label("loc_16F6")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_16F6")

    QueueWorkItem2(0x0, 1, lambda_16F6)

    def lambda_1707():

        label("loc_1707")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1707")

    QueueWorkItem2(0x1, 1, lambda_1707)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1731")

    def lambda_1726():

        label("loc_1726")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1726")

    QueueWorkItem2(0x2, 1, lambda_1726)

    label("loc_1731")

    SetChrFlags(0x15, 0x40)
    OP_8E(0x15, 0x9B6E, 0x0, 0xFF32, 0xBB8, 0x0)
    OP_8E(0x15, 0xB4C8, 0x0, 0xFF3C, 0xBB8, 0x0)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1778")
    OP_44(0x2, 0xFF)

    label("loc_1778")

    SetChrPos(0x15, 47880, 0, 56070, 135)
    ClearChrFlags(0x15, 0x40)
    OP_4B(0x15, 255)
    OP_64(0x4, 0x1)
    EventEnd(0x0)

    label("loc_1798")

    TalkEnd(0xFF)
    Return()

    # Function_2_D64 end

    def Function_3_179C(): pass

    label("Function_3_179C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22B9")
    OP_28(0x27, 0x1, 0x8)
    EventBegin(0x0)
    Fade(1000)
    OP_6C(270000, 0)
    SetChrPos(0x101, 53860, 0, 28500, 90)
    SetChrPos(0x105, 53290, 0, 29520, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17FF")
    SetChrPos(0x13B, 52540, 0, 30290, 90)

    label("loc_17FF")

    OP_69(0x101, 0x0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #71
        0x101,
        (
            "#004FHuh...?\x02\x03",

            "Maybe...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    OP_94(0x1, 0x101, 0xB4, 0x3E8, 0x7D0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1871")

    def lambda_1864():
        TurnDirection(0x13B, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_1864)
    Sleep(150)

    label("loc_1871")

    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #72
        0x105,
        "#040FIs something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        "#002FThere's no flag here.\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_18C1():

        label("loc_18C1")

        TurnDirection(0x105, 0x101, 0)
        OP_48()
        Jump("loc_18C1")

    QueueWorkItem2(0x105, 1, lambda_18C1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18EB")

    def lambda_18E0():

        label("loc_18E0")

        TurnDirection(0x13B, 0x101, 0)
        OP_48()
        Jump("loc_18E0")

    QueueWorkItem2(0x13B, 1, lambda_18E0)

    label("loc_18EB")

    OP_8E(0x101, 0xC80A, 0x0, 0x6C3E, 0x1770, 0x0)
    Sleep(100)
    Fade(1000)
    OP_6C(135000, 0)
    OP_6D(51210, 0, 27710, 0)
    Sleep(100)
    OP_8C(0x101, 90, 400)
    Sleep(400)

    ChrTalk(    #74
        0x101,
        "#000FBut there's one on the other side.\x02",
    )

    CloseMessageWindow()
    OP_44(0x105, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1992")
    OP_44(0x13B, 0x1)

    def lambda_197D():
        OP_8E(0x13B, 0xCD96, 0x0, 0x73A0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_197D)

    label("loc_1992")

    OP_8E(0x105, 0xCCCE, 0x0, 0x6C66, 0xBB8, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19C2")

    def lambda_19BA():
        OP_8C(0x13B, 315, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_19BA)

    label("loc_19C2")

    OP_8C(0x105, 315, 400)
    Sleep(200)
    OP_8C(0x105, 180, 400)
    Sleep(200)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x105, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A52")

    ChrTalk(    #75
        0x105,
        "#044FAh, you're right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13B, 0x101, 400)

    ChrTalk(    #76
        0x13B,
        "#643FGood eyes, Madame Bracer.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13B, 400)
    Jump("loc_1A8E")

    label("loc_1A52")


    ChrTalk(    #77
        0x105,
        (
            "#044FOh, you're right.\x02\x03",

            "Good thinking, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    label("loc_1A8E")


    ChrTalk(    #78
        0x101,
        (
            "#001FHeh heh... Pure chance, really.\x02\x03",

            "Let's go tell Mr. Parkes about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x105,
        "#041FYes, let's.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x15, 49850, 0, 28600, 90)
    SetChrPos(0x101, 55720, 0, 29180, 270)
    SetChrPos(0x105, 55170, 0, 30090, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B4F")
    SetChrPos(0x13B, 56220, 0, 30860, 270)

    label("loc_1B4F")

    Sleep(1000)
    FadeToBright(1000, 0)
    OP_6C(270000, 0)
    OP_6D(54350, 0, 28820, 0)
    OP_0D()

    def lambda_1B7E():

        label("loc_1B7E")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1B7E")

    QueueWorkItem2(0x0, 1, lambda_1B7E)

    def lambda_1B8F():

        label("loc_1B8F")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1B8F")

    QueueWorkItem2(0x1, 1, lambda_1B8F)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BB9")

    def lambda_1BAE():

        label("loc_1BAE")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_1BAE")

    QueueWorkItem2(0x2, 1, lambda_1BAE)

    label("loc_1BB9")

    SetChrFlags(0x15, 0x40)
    OP_8E(0x15, 0xD598, 0x0, 0x6F04, 0xBB8, 0x0)
    OP_4A(0x15, 255)
    Sleep(400)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BF5")
    OP_44(0x2, 0xFF)

    label("loc_1BF5")

    OP_8C(0x15, 270, 400)
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #80
        0x15,
        "Oh, that's a good idea.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    ChrTalk(    #81
        0x15,
        (
            "I'll go ahead and get\x01",
            "this straightened out.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CC7")

    ChrTalk(    #82
        0x13B,
        "#644FWe can help...\x02",
    )

    CloseMessageWindow()

    def lambda_1C96():
        TurnDirection(0x105, 0x13B, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1C96)
    TurnDirection(0x101, 0x13B, 400)

    ChrTalk(    #83
        0x105,
        "#040FThat's right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x13B, 400)
    Jump("loc_1D14")

    label("loc_1CC7")

    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #84
        0x101,
        "#000FOkay, let's see what we can do.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #85
        0x105,
        "#040FAll right.\x02",
    )

    CloseMessageWindow()

    label("loc_1D14")


    ChrTalk(    #86
        0x15,
        "I appreciate it.\x02",
    )

    CloseMessageWindow()

    def lambda_1D30():
        OP_8E(0x15, 0xD764, 0x0, 0x6054, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1D30)

    def lambda_1D4B():
        OP_8E(0x101, 0xDAFC, 0x0, 0x7CD8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D4B)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DA7")

    def lambda_1D74():
        OP_8E(0x13B, 0xD7AA, 0x0, 0x7D77, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_1D74)

    def lambda_1D8F():
        OP_8E(0x105, 0xDAD4, 0x0, 0x646E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1D8F)
    Jump("loc_1DC2")

    label("loc_1DA7")


    def lambda_1DAD():
        OP_8E(0x105, 0xD7AA, 0x0, 0x7D77, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1DAD)

    label("loc_1DC2")

    OP_6D(54350, 1500, 28820, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x15, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x105, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DFC")
    OP_44(0x13B, 0x1)

    label("loc_1DFC")

    OP_72(0x1A, 0x4)
    SetChrPos(0x101, 55720, 0, 29180, 270)
    SetChrPos(0x105, 55170, 0, 30090, 270)
    SetChrPos(0x15, 56700, 0, 27700, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E53")
    SetChrPos(0x13B, 57090, 0, 30560, 270)

    label("loc_1E53")

    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_28(0x27, 0x1, 0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2170")

    ChrTalk(    #87
        0x15,
        "...All right, that should do it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x101, 400)

    def lambda_1EB6():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1EB6)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EDA")

    def lambda_1ED2():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_1ED2)

    label("loc_1EDA")

    TurnDirection(0x101, 0x15, 400)
    OP_69(0x101, 0x5DC)

    ChrTalk(    #88
        0x15,
        (
            "Phew... That looks like the\x01",
            "last of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x15,
        "You kids have been a big help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#000FNo prob.\x02\x03",

            "We all want the festival\x01",
            "to go well, so helping out\x01",
            "isn't a big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x105,
        (
            "#040FThat's right.\x02\x03",

            "It's our festival, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2004")
    TurnDirection(0x13B, 0x105, 400)

    ChrTalk(    #92
        0x13B,
        "#644FThat's the spirit, Kloe.\x02",
    )

    CloseMessageWindow()

    label("loc_2004")


    ChrTalk(    #93
        0x15,
        "Ha ha. I suppose you're right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13B, 0x15, 400)

    ChrTalk(    #94
        0x15,
        "I'm looking forward to it myself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        "#006FJust leave it to us!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20A9")

    ChrTalk(    #96
        0x13B,
        "#649FHa ha...glad to hear it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_20C6")

    label("loc_20A9")


    ChrTalk(    #97
        0x105,
        "#040FWe'll do our best.\x02",
    )

    CloseMessageWindow()

    label("loc_20C6")


    ChrTalk(    #98
        0x15,
        (
            "Got my fingers crossed for\x01",
            "you, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x27, 0x1, 0x10)
    OP_28(0x3D, 0x1, 0x200)
    OP_2C(0x3D, 0x1F4)
    OP_2B(0x3D, 0x1)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #99
        (
            "\x07\x00Festival help quest\x01\x07\x02",
            "[Decorate the Campus] \x07\x00completed!\x02",
        )
    )

    OP_83(0x2, 0x2)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jump("loc_2225")

    label("loc_2170")


    ChrTalk(    #100
        0x15,
        "...All right, that should do it.\x02",
    )

    CloseMessageWindow()
    OP_69(0x101, 0x5DC)
    TurnDirection(0x15, 0x101, 400)

    def lambda_21AA():
        TurnDirection(0x105, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_21AA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21CE")

    def lambda_21C6():
        TurnDirection(0x13B, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_21C6)

    label("loc_21CE")

    TurnDirection(0x101, 0x15, 400)

    ChrTalk(    #101
        0x15,
        "Let me know if you see any more.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#006FSure thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x105,
        "#040FYes, sir.\x02",
    )

    CloseMessageWindow()

    label("loc_2225")


    def lambda_222B():

        label("loc_222B")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_222B")

    QueueWorkItem2(0x0, 1, lambda_222B)

    def lambda_223C():

        label("loc_223C")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_223C")

    QueueWorkItem2(0x1, 1, lambda_223C)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2266")

    def lambda_225B():

        label("loc_225B")

        TurnDirection(0xFE, 0x15, 0)
        OP_48()
        Jump("loc_225B")

    QueueWorkItem2(0x2, 1, lambda_225B)

    label("loc_2266")

    SetChrFlags(0x15, 0x40)
    OP_8E(0x15, 0xB0C2, 0x0, 0x6DCE, 0xBB8, 0x0)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3A)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2299")
    OP_44(0x2, 0xFF)

    label("loc_2299")

    SetChrPos(0x15, 47880, 0, 56070, 135)
    ClearChrFlags(0x15, 0x40)
    OP_4B(0x15, 255)
    OP_64(0x5, 0x1)
    EventEnd(0x0)

    label("loc_22B9")

    TalkEnd(0xFF)
    Return()

    # Function_3_179C end

    SaveToFile()

Try(main)
