from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R0201_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T0131.x',
        MapIndex            = 22,
        MapDefaultBGM       = "ed60020",
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
        "Function_1_677",          # 01, 1
        "Function_2_D3F",          # 02, 2
        "Function_3_119F",         # 03, 3
        "Function_4_1C6C",         # 04, 4
        "Function_5_2111",         # 05, 5
        "Function_6_211B",         # 06, 6
        "Function_7_216F",         # 07, 7
        "Function_8_21C3",         # 08, 8
        "Function_9_2217",         # 09, 9
        "Function_10_226B",        # 0A, 10
        "Function_11_2292",        # 0B, 11
        "Function_12_22B9",        # 0C, 12
        "Function_13_22E1",        # 0D, 13
        "Function_14_2305",        # 0E, 14
        "Function_15_2329",        # 0F, 15
        "Function_16_2351",        # 10, 16
        "Function_17_2372",        # 11, 17
    )


    def Function_0_66(): pass

    label("Function_0_66")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetMapFlags(0x8000000)
    Fade(1000)
    OP_6C(260000, 0)

    def lambda_86():
        OP_6B(2500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_86)
    SetChrPos(0x101, -205210, 0, -19200, 135)
    SetChrPos(0x102, -206190, 20, -20420, 135)
    OP_6D(-205750, 20, -20780, 3000)
    OP_0D()

    ChrTalk(    #0
        0x101,
        (
            "#000FFrom what Freddy said, I think\x01",
            "this is the road lamp...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#010FI'm fairly certain this is the\x01",
            "right one, too.\x02\x03",

            "#010FIt says 'Road Lamp No. 6'\x01",
            "on the panel, as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#006FYou're right, it does.\x02\x03",

            "All-righty then.\x01",
            "Let's get to work\x01",
            "and finish this job.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_8C(0x102, 180, 400)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #3
        0x102,
        (
            "#012F...Unfortunately, it may\x01",
            "not be that easy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #4
        0x101,
        "#004FWhat do you mean...?\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, -202100, 0, -35820, 0)
    SetChrPos(0x9, -199870, 1000, -36700, 0)
    SetChrPos(0xA, -197980, 0, -35450, 0)
    SetChrPos(0xB, -196350, 0, -33810, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    def lambda_2B1():
        OP_90(0x8, 0xFFFFFC18, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2B1)
    Sleep(150)

    def lambda_2D1():
        OP_90(0x9, 0xFFFFFC18, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2D1)
    Sleep(100)

    def lambda_2F1():
        OP_90(0xA, 0xFFFFFC18, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2F1)
    Sleep(120)

    def lambda_311():
        OP_90(0xB, 0xFFFFFC18, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_311)

    def lambda_32C():
        OP_6C(225000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_32C)

    def lambda_33C():
        OP_6D(-202310, 0, -28900, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_33C)
    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 8)
    OP_43(0x8, 0x0, 0x0, 0x2)

    def lambda_365():

        label("loc_365")

        TurnDirection(0x8, 0x101, 0)
        OP_48()
        Jump("loc_365")

    QueueWorkItem2(0x8, 1, lambda_365)
    WaitChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 8)
    OP_43(0x9, 0x0, 0x0, 0x2)

    def lambda_387():

        label("loc_387")

        TurnDirection(0x9, 0x101, 0)
        OP_48()
        Jump("loc_387")

    QueueWorkItem2(0x9, 1, lambda_387)
    WaitChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 8)
    OP_43(0xA, 0x0, 0x0, 0x2)

    def lambda_3A9():

        label("loc_3A9")

        TurnDirection(0xA, 0x101, 0)
        OP_48()
        Jump("loc_3A9")

    QueueWorkItem2(0xA, 1, lambda_3A9)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 8)
    OP_43(0xB, 0x0, 0x0, 0x2)

    def lambda_3CB():

        label("loc_3CB")

        TurnDirection(0xB, 0x101, 0)
        OP_48()
        Jump("loc_3CB")

    QueueWorkItem2(0xB, 1, lambda_3CB)
    WaitChrThread(0x0, 0x1)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrPos(0xC, -206450, 50, -21160, 141)
    SetChrPos(0xD, -206450, 50, -21160, 141)
    SetChrFlags(0xD, 0x1000)
    SetChrFlags(0xC, 0x1000)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrChipByIndex(0xD, 5)
    SetChrChipByIndex(0xC, 4)

    def lambda_43F():
        OP_8E(0xD, 0xFFFCE06E, 0xFFFFFFBA, 0xFFFF9EC6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_43F)
    OP_8E(0xC, 0xFFFCE4A6, 0xFFFFFFE2, 0xFFFFA060, 0x1388, 0x0)
    WaitChrThread(0xD, 0x1)
    OP_8C(0xD, 180, 0)
    OP_8C(0xC, 180, 0)
    SetChrChipByIndex(0xD, 7)
    SetChrChipByIndex(0xC, 6)
    OP_6D(-202010, 10, -26160, 1000)

    ChrTalk(    #5
        0xC,
        (
            "#002FWhere'd all these monsters\x01",
            "come from?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xD,
        (
            "#012FIt looks like the orbment\x01",
            "really has burned out.\x02\x03",

            "#012FAnyway, one of us will need to\x01",
            "fend off these monsters while\x01",
            "the other replaces the orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xC,
        (
            "#002FYeah, you're right.\x02\x03",

            "Well then...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_591")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_651")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Leave these monsters to me!]\x01",             # 0
            "[How about you handle them, Joshua!]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_626"),
        (1, "loc_63A"),
        (SWITCH_DEFAULT, "loc_64E"),
    )


    label("loc_626")

    Call(1, 1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_64E")

    label("loc_63A")

    Call(1, 2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_64E")

    label("loc_64E")

    Jump("loc_591")

    label("loc_651")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_64(0x0, 0x1)
    OP_28(0x6, 0x1, 0x8)
    ClearChrFlags(0x102, 0x40)
    ClearChrFlags(0x101, 0x40)
    EventEnd(0x0)
    ClearMapFlags(0x8000000)
    Return()

    # Function_0_66 end

    def Function_1_677(): pass

    label("Function_1_677")

    RemoveParty(0x1, 0x0)

    ChrTalk(    #8
        0xC,
        "#002FLeave these monsters to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xD,
        (
            "#012FOkay.\x02\x03",

            "I'll open the maintenance panel,\x01",
            "so hold them off until then,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xC,
        "#005FGot it!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xD, 18)
    SetChrChipByIndex(0xC, 4)
    SetChrChipByIndex(0x8, 9)
    SetChrChipByIndex(0x9, 9)
    SetChrChipByIndex(0xA, 9)
    SetChrChipByIndex(0xB, 9)

    def lambda_72E():
        OP_92(0x8, 0x101, 0x11F8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_72E)

    def lambda_743():
        OP_92(0x9, 0x101, 0x11F8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_743)

    def lambda_758():
        OP_92(0xA, 0x101, 0x11F8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_758)

    def lambda_76D():
        OP_92(0xB, 0x101, 0x11F8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_76D)

    def lambda_782():
        OP_8E(0xD, 0xFFFCDB64, 0x3C, 0xFFFFABA0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_782)
    OP_8E(0xC, 0xFFFCE82A, 0x0, 0xFFFF9868, 0x1770, 0x0)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x3EB, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_7E5"),
        (SWITCH_DEFAULT, "loc_7EA"),
    )


    label("loc_7E5")

    OP_B4(0x0)
    Jump("loc_7EA")

    label("loc_7EA")

    EventBegin(0x0)
    OP_1D(0x14)
    AddParty(0x1, 0x1)
    OP_6D(-203550, -30, -24610, 0)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x101, 0x8)
    SetChrChipByIndex(0x101, 6)
    SetChrPos(0x101, -202010, 10, -26160, 180)
    SetChrPos(0x102, -204100, 0, -20750, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    OP_0D()
    Sleep(500)

    ChrTalk(    #11
        0x101,
        (
            "#002FWhew. So have you monsters\x01",
            "had enough?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        "#014F(There she goes again...)\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #13
        0x101,
        (
            "#002FHow's everything on your\x01",
            "side, Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        (
            "#010FI'm putting in the combination\x01",
            "right now.\x02\x03",

            "Let's see...it was 544818,\x01",
            "I think...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#002FI'm okay here, so just focus\x01",
            "on the work.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    OP_22(0x83, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #16
        0x102,
        (
            "#012FAll right, it's open!\x02\x03",

            "Now all we need to do is\x01",
            "replace the orbment...\x02",
        )
    )

    CloseMessageWindow()
    OP_3F(0x327, 1)

    ChrTalk(    #17
        0x101,
        "#502FOh baby, I'm on a roll!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 6)
    OP_8C(0x101, 0, 400)
    OP_8C(0x101, 45, 400)
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    OP_22(0x7E, 0x1, 0x64)
    SetChrChipByIndex(0x101, 16)

    def lambda_A3F():

        label("loc_A3F")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_A3F")

    QueueWorkItem2(0x101, 0, lambda_A3F)

    def lambda_A52():
        OP_6D(-202010, 10, -26160, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A52)
    SetChrFlags(0x102, 0x40)

    def lambda_A6F():
        OP_8E(0x102, 0xFFFCE64A, 0xFFFFFFF6, 0xFFFFAF2E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A6F)
    WaitChrThread(0x102, 0x1)

    def lambda_A8F():
        OP_8E(0x102, 0xFFFCEC44, 0xFFFFFFE2, 0xFFFFA7F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A8F)
    WaitChrThread(0x102, 0x1)

    def lambda_AAF():
        OP_92(0x102, 0x101, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AAF)
    OP_23(0x7E)
    OP_44(0x101, 0x0)
    SetChrChipByIndex(0x101, 6)
    OP_8C(0x101, 180, 400)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #18
        0x101,
        (
            "#005FCome on, come on,\x01",
            "come on, you monsters!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #19
        0x102,
        (
            "#010FSorry to have kept you waiting,\x01",
            "Estelle. Our work is done here.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)
    Sleep(400)
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x102, 400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #20
        0x101,
        (
            "#000FHuh...?\x02\x03",

            "#004FD-Done...?\x02\x03",

            "Wait, so you've already replaced\x01",
            "the orbment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        (
            "#010FYep. I don't think we'll need to\x01",
            "worry about any more monsters.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 45, 400)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #22
        0x101,
        "#007FSheesh, that's it?\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)

    ChrTalk(    #23
        0x102,
        (
            "#018F...\x02\x03",

            "You sound like that's\x01",
            "a bad thing.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #24
        0x101,
        (
            "#506FAh...ha ha ha... ☆\x02\x03",

            "Must be your imagination!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        "#017FYou are really something else...\x02",
    )

    CloseMessageWindow()
    OP_2B(0x6, 0x1)
    Sleep(400)
    Return()

    # Function_1_677 end

    def Function_2_D3F(): pass

    label("Function_2_D3F")

    RemoveParty(0x0, 0x0)

    ChrTalk(    #26
        0xC,
        (
            "#002FHow about you handle them,\x01",
            "Joshua!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #27
        0xD,
        (
            "#014FDo you really know how to\x01",
            "replace one of those things?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xC,
        (
            "#009FCome on, Joshua. \x01",
            "How hard could it be?\x02\x03",

            "Even I can do something as simple\x01",
            "as replacing an orbment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xD,
        (
            "#012FSays the girl who glued her\x01",
            "hand to her head once...\x01",
            "But, all right. If you say so.\x02\x03",

            "I'm counting on you, Estelle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xC,
        "#005FGot it!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xD, 5)
    SetChrChipByIndex(0xC, 17)
    SetChrChipByIndex(0x8, 9)
    SetChrChipByIndex(0x9, 9)
    SetChrChipByIndex(0xA, 9)
    SetChrChipByIndex(0xB, 9)

    def lambda_EED():
        OP_92(0x8, 0x101, 0x11F8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EED)

    def lambda_F02():
        OP_92(0x9, 0x101, 0x11F8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F02)

    def lambda_F17():
        OP_92(0xA, 0x101, 0x11F8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F17)

    def lambda_F2C():
        OP_92(0xB, 0x101, 0x11F8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F2C)

    def lambda_F41():
        OP_8E(0xC, 0xFFFCDB64, 0x3C, 0xFFFFABA0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_F41)
    OP_8E(0xD, 0xFFFCE82A, 0x0, 0xFFFF9868, 0x1770, 0x0)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x3EB, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_FA4"),
        (SWITCH_DEFAULT, "loc_FA9"),
    )


    label("loc_FA4")

    OP_B4(0x0)
    Jump("loc_FA9")

    label("loc_FA9")

    EventBegin(0x0)
    OP_1D(0x14)
    AddParty(0x0, 0x0)
    OP_6D(-203550, -30, -24610, 0)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x101, 0x8)
    SetChrChipByIndex(0x102, 7)
    SetChrPos(0x102, -202010, 10, -26160, 180)
    SetChrPos(0x101, -204100, 0, -20750, 180)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_0D()
    Sleep(500)

    ChrTalk(    #31
        0x102,
        "#012FThat takes care of the first wave...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #32
        0x102,
        "#012FHow's it coming, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#002FI'm entering the combination for\x01",
            "the maintenance panel right now.\x02\x03",

            "#505FUmm...\x01",
            "I'm pretty sure the code was...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_118F")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "'545818'\x01",      # 0
            "'554818'\x01",      # 1
            "'544818'\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1164"),
        (1, "loc_116E"),
        (2, "loc_1178"),
        (SWITCH_DEFAULT, "loc_118C"),
    )


    label("loc_1164")

    Call(1, 3)
    OP_5F(0x0)
    Jump("loc_118C")

    label("loc_116E")

    Call(1, 3)
    OP_5F(0x0)
    Jump("loc_118C")

    label("loc_1178")

    Call(1, 4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jump("loc_118C")

    label("loc_118C")

    Jump("loc_10F3")

    label("loc_118F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)
    Return()

    # Function_2_D3F end

    def Function_3_119F(): pass

    label("Function_3_119F")

    OP_28(0x6, 0x1, 0x4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1201")

    ChrTalk(    #34
        0x101,
        (
            "#002FOkay, 545818...\x02\x03",

            "...\x02\x03",

            "#509F...Huh?\x02\x03",

            "Why isn't this thing opening?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_124D")

    label("loc_1201")


    ChrTalk(    #35
        0x101,
        (
            "#002FOkay, 554818...\x02\x03",

            "...\x02\x03",

            "#509F...Huh?\x02\x03",

            "Why isn't this thing opening?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_124D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #36
        0x102,
        (
            "#017F(I should have known\x01",
            "this would happen.)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrChipByIndex(0x102, 7)
    OP_8C(0x102, 180, 400)
    Sleep(400)
    SetChrPos(0x8, -202100, 0, -35820, 0)
    SetChrPos(0xA, -197980, 0, -35450, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)

    def lambda_1300():
        OP_6D(-202310, 0, -28900, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1300)

    def lambda_1318():
        OP_90(0x8, 0xFFFFFC18, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1318)
    Sleep(150)

    def lambda_1338():
        OP_90(0xA, 0xFFFFFC18, 0x0, 0x1388, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1338)
    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 8)
    OP_43(0x8, 0x0, 0x0, 0x2)

    def lambda_1364():

        label("loc_1364")

        TurnDirection(0x8, 0x102, 0)
        OP_48()
        Jump("loc_1364")

    QueueWorkItem2(0x8, 1, lambda_1364)
    WaitChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 8)
    OP_43(0xA, 0x0, 0x0, 0x2)

    def lambda_1386():

        label("loc_1386")

        TurnDirection(0xA, 0x102, 0)
        OP_48()
        Jump("loc_1386")

    QueueWorkItem2(0xA, 1, lambda_1386)
    WaitChrThread(0x0, 0x2)

    ChrTalk(    #37
        0x102,
        "#013FMore of them, huh...?\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xD, -202010, 10, -26160, 180)
    SetChrChipByIndex(0xD, 7)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x102, 0x8)
    SetChrChipByIndex(0x8, 9)
    SetChrChipByIndex(0xA, 9)

    def lambda_13EB():
        OP_92(0x8, 0xD, 0xE10, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_13EB)

    def lambda_1400():
        OP_92(0xA, 0xD, 0xE10, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1400)
    WaitChrThread(0xA, 0x1)
    OP_44(0x8, 0xFF)
    OP_44(0xA, 0xFF)
    RemoveParty(0x0, 0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x3EC, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1441"),
        (SWITCH_DEFAULT, "loc_1446"),
    )


    label("loc_1441")

    OP_B4(0x0)
    Jump("loc_1446")

    label("loc_1446")

    EventBegin(0x0)
    OP_1D(0x14)
    AddParty(0x0, 0x0)
    OP_6D(-203550, -30, -24610, 0)
    SetChrChipByIndex(0x102, 7)
    SetChrPos(0x102, -202010, 10, -26160, 180)
    SetChrPos(0x101, -204100, 0, -20750, 180)
    OP_6D(-203320, -20, -24970, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x102, 0x80)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #38
        0x101,
        (
            "#009FAaahh! Why won't this\x01",
            "dang thing open?!\x02\x03",

            "I'm getting really mad now!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 2000)
    OP_8C(0x101, 45, 2000)
    OP_8C(0x101, 180, 2000)
    SetChrChipByIndex(0x101, 6)

    ChrTalk(    #39
        0x101,
        (
            "#005FIf you don't wanna open, then I'm\x01",
            "gonna have to MAKE you open...\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #40
        0x102,
        (
            "#012FWait, Estelle!\x02\x03",

            "The combination is 544818!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #41
        0x101,
        "#501F...Really?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x101, 65535)
    OP_8C(0x101, 135, 400)

    ChrTalk(    #42
        0x101,
        (
            "#004FAll right, give me a second!\x01",
            "I'll give it another shot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x102,
        "#017F544...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #44
        0x101,
        "#002FUmm, 544...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x102,
        "#017F...818.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#002FOkay, now 818...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_22(0x83, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #47
        0x101,
        (
            "#004F...It opened.\x02\x03",

            "#502FHa!\x01",
            "Well, if we've come this far\x01",
            "then we're as good as done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x102,
        "#018F(We'll aren't you the carefree one.)\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #49
        0x101,
        (
            "#006FNow for the orbment...\x02\x03",

            "...which goes in like that\x01",
            "and...voila!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#001FPerfect!\x02\x03",

            "This job turned out to be\x01",
            "pretty rough.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_17F3():
        OP_6D(-203230, -10, -20760, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17F3)
    OP_8E(0x102, 0xFFFCE924, 0xFFFFFFF6, 0xFFFFAEF2, 0x7D0, 0x0)
    TurnDirection(0x102, 0x101, 400)
    OP_3F(0x327, 1)

    ChrTalk(    #51
        0x102,
        (
            "#010FGood work, Estelle.\x02\x03",

            "All the monsters seem to\x01",
            "have gone, too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 800)

    ChrTalk(    #52
        0x101,
        (
            "#007FSorry about that, Joshua.\x02\x03",

            "I ran into a bit of trouble with\x01",
            "the combination and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        "#010FDon't sweat it.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 225, 400)

    ChrTalk(    #54
        0x102,
        (
            "#017FAnyway, I'm just relieved that\x01",
            "this road lamp isn't broken.\x02\x03",

            "When I saw you raise your staff like that\x01",
            "I was worried you were going to try and\x01",
            "'fix' it the way you usually do things...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #55
        0x101,
        (
            "#008FOh, th-that? I only did that to...\x01",
            "...to regain my concentration.\x01",
            "Yes! It's a concentration technique!\x02\x03",

            "Your flower petal of a sister\x01",
            "would never do such a barbaric\x01",
            "thing as that.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #56
        0x102,
        (
            "#018FI don't know...\x01",
            "You still look like you want\x01",
            "to punch the lights out of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #57
        0x101,
        (
            "#009FI do not!\x02\x03",

            "A-Anyway, our job is done here,\x01",
            "so let's just think about something\x01",
            "else.\x02\x03",

            "#508FAll's well that has a good end or\x01",
            "whatever it is that people say, right?\x01",
            "The little things don't really matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        (
            "#010FI'll just leave it at that.\x02\x03",

            "All right, how about we head\x01",
            "back to town?\x02\x03",

            "We'd better go report to Freddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        "#001FAll right, let's go.\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_3_119F end

    def Function_4_1C6C(): pass

    label("Function_4_1C6C")

    OP_2B(0x6, 0x1)

    ChrTalk(    #60
        0x101,
        "#002FOkay, 544818...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_22(0x83, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #61
        0x101,
        (
            "#000F...It's open!\x02\x03",

            "#502FSometimes, I'm too smart\x01",
            "for my own good!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #62
        0x102,
        (
            "#010FI'm okay here, Estelle.\x02\x03",

            "#010FSo just focus on fixing\x01",
            "the lamp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        (
            "#000FGot it!\x02\x03",

            "Now for the orbment...which\x01",
            "goes in like that and...voila!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #64
        0x101,
        "#001FPerfect!\x02",
    )

    CloseMessageWindow()

    def lambda_1DB6():
        OP_6D(-203230, -10, -20760, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1DB6)
    OP_8E(0x102, 0xFFFCE924, 0xFFFFFFF6, 0xFFFFAEF2, 0x7D0, 0x0)
    TurnDirection(0x102, 0x101, 400)
    OP_3F(0x327, 1)

    ChrTalk(    #65
        0x102,
        (
            "#010FGood work, Estelle.\x02\x03",

            "All the monsters seem to\x01",
            "have gone, too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #66
        0x101,
        (
            "#007FWhew...\x02\x03",

            "I sure got all stressed out\x01",
            "over this job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x102,
        (
            "#010FConsidering the circumstances,\x01",
            "it seemed pretty reasonable to\x01",
            "me.\x02\x03",

            "But the thing that surprises me\x01",
            "the most is that you remembered\x01",
            "the combination.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #68
        0x101,
        (
            "#001FDo you want to know the truth?\x02\x03",

            "I actually just saw a jumble of numbers\x01",
            "in my head, and the buttons I happened\x01",
            "to press were the right ones.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #69
        0x102,
        (
            "#017FI should have figured as much.\x02\x03",

            "You're something else...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#006FA-Anyway, our job is done here,\x01",
            "so let's just think about something\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x102,
        (
            "#010FI guess you're right.\x02\x03",

            "#010FAll right, how about we head\x01",
            "back to town?\x02\x03",

            "#010FWe'd better go report to Freddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#001FAll right, let's go.\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_4_1C6C end

    def Function_5_2111(): pass

    label("Function_5_2111")

    OP_6C(270000, 2000)
    Return()

    # Function_5_2111 end

    def Function_6_211B(): pass

    label("Function_6_211B")

    OP_A6(0x0)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCE708, 0x0, 0xFFFF793C, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 0)
    OP_43(0x8, 0x2, 0x0, 0x2)
    OP_A3(0x0)
    OP_A6(0x0)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCE578, 0x0, 0xFFFF874C, 0x1B58, 0x0)
    OP_8C(0xFE, 0, 0)
    OP_A3(0x0)
    Return()

    # Function_6_211B end

    def Function_7_216F(): pass

    label("Function_7_216F")

    OP_A6(0x1)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCF194, 0x0, 0xFFFF7C5C, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 0)
    OP_43(0x9, 0x2, 0x0, 0x2)
    OP_A3(0x1)
    OP_A6(0x1)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCEE74, 0x0, 0xFFFF88DC, 0x1B58, 0x0)
    OP_8C(0xFE, 315, 0)
    OP_A3(0x1)
    Return()

    # Function_7_216F end

    def Function_8_21C3(): pass

    label("Function_8_21C3")

    OP_A6(0x2)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCF2C0, 0x0, 0xFFFF7554, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 0)
    OP_43(0xA, 0x2, 0x0, 0x2)
    OP_A3(0x2)
    OP_A6(0x2)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCEAF0, 0x0, 0xFFFF84F4, 0x1B58, 0x0)
    OP_8C(0xFE, 0, 0)
    OP_A3(0x2)
    Return()

    # Function_8_21C3 end

    def Function_9_2217(): pass

    label("Function_9_2217")

    OP_A6(0x3)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCFD4C, 0x0, 0xFFFF7874, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 0)
    OP_43(0xB, 0x2, 0x0, 0x2)
    OP_A3(0x3)
    OP_A6(0x3)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCF194, 0x0, 0xFFFF842C, 0x1B58, 0x0)
    OP_8C(0xFE, 315, 0)
    OP_A3(0x3)
    Return()

    # Function_9_2217 end

    def Function_10_226B(): pass

    label("Function_10_226B")

    OP_A6(0x4)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCE384, 0x0, 0xFFFF99A8, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 0)
    OP_A3(0x4)
    Return()

    # Function_10_226B end

    def Function_11_2292(): pass

    label("Function_11_2292")

    OP_A6(0x5)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCEA8C, 0x0, 0xFFFF9AD4, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 0)
    OP_A3(0x5)
    Return()

    # Function_11_2292 end

    def Function_12_22B9(): pass

    label("Function_12_22B9")

    OP_A6(0x4)
    SetChrChipByIndex(0xC, 4)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCE7D0, 0x0, 0xFFFF8BFC, 0x1770, 0x0)
    OP_A3(0x4)
    OP_A3(0x5)
    Return()

    # Function_12_22B9 end

    def Function_13_22E1(): pass

    label("Function_13_22E1")

    OP_A6(0x5)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCE60E, 0x0, 0xFFFFA902, 0x1770, 0x0)
    OP_8C(0xFE, 315, 0)
    Return()

    # Function_13_22E1 end

    def Function_14_2305(): pass

    label("Function_14_2305")

    OP_A6(0x4)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCE60E, 0x0, 0xFFFFA902, 0x1770, 0x0)
    OP_8C(0xFE, 315, 0)
    Return()

    # Function_14_2305 end

    def Function_15_2329(): pass

    label("Function_15_2329")

    OP_A6(0x5)
    SetChrChipByIndex(0xD, 5)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFCE7D0, 0x0, 0xFFFF8BFC, 0x1770, 0x0)
    OP_A3(0x5)
    OP_A3(0x4)
    Return()

    # Function_15_2329 end

    def Function_16_2351(): pass

    label("Function_16_2351")

    OP_A6(0x5)
    SetChrFlags(0xFE, 0x40)
    OP_92(0x102, 0xE, 0x3E8, 0xBB8, 0x0)
    TurnDirection(0x102, 0xE, 0)
    OP_A3(0x5)
    Return()

    # Function_16_2351 end

    def Function_17_2372(): pass

    label("Function_17_2372")

    OP_A6(0x5)
    SetChrFlags(0xFE, 0x40)
    OP_92(0x102, 0x101, 0x3E8, 0xBB8, 0x0)
    TurnDirection(0x102, 0x101, 0)
    OP_A3(0x5)
    Return()

    # Function_17_2372 end

    SaveToFile()

Try(main)
