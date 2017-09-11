from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R0302_1 ._SN',
        MapName             = 'rolent',
        Location            = 'R0302.x',
        MapIndex            = 21,
        MapDefaultBGM       = "ed60022",
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
        "Function_1_4D6",          # 01, 1
        "Function_2_132D",         # 02, 2
        "Function_3_1375",         # 03, 3
        "Function_4_13BD",         # 04, 4
        "Function_5_1405",         # 05, 5
        "Function_6_1438",         # 06, 6
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D5")
    SetMapFlags(0x8000000)
    EventBegin(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1A1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B")
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(    #0
        0x102,
        (
            "#014FEstelle, that way leads to\x01",
            "the Malga Mine.\x02\x03",

            "#014FLet's go report to Freddy first.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 0)

    ChrTalk(    #1
        0x101,
        "#000FOh yeah. I forgot about that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_19E")

    label("loc_12B")


    ChrTalk(    #2
        0x102,
        (
            "#010FThis goes to the Malga Mine,\x01",
            "huh?\x02\x03",

            "#010FI think we'd better report to\x01",
            "Freddy before we do anything\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E")

    Jump("loc_4B2")

    label("loc_1A1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_365")
    OP_A2(0x5)
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(    #3
        0x102,
        (
            "#014FEstelle, that way leads to\x01",
            "the Malga Mine.\x02\x03",

            "#014FWe need to replace the orbment\x01",
            "in the road lamp on the Milch Main\x01",
            "Road before doing anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#004FOh, right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#018FYou didn't forget already...\x01",
            "did you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 0)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #6
        0x101,
        (
            "#008FCome on, Joshua.\x02\x03",

            "Of course I wouldn't forget something\x01",
            "as important as a job from a client.\x01",
            "Never! ...Ha...ha... (Whoops)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        "#017FI sure hope not.\x02",
    )

    CloseMessageWindow()
    Jump("loc_40A")

    label("loc_365")

    TurnDirection(0x102, 0x101, 0)

    ChrTalk(    #8
        0x102,
        (
            "#014FEstelle, that way leads to\x01",
            "the Malga Mine.\x02\x03",

            "#014FWe need to replace the orbment\x01",
            "in the road lamp on the Milch Main\x01",
            "Road before doing anything else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40A")

    Jump("loc_4B2")

    label("loc_40D")


    ChrTalk(    #9
        0x102,
        (
            "#010FThis goes to the Malga Mine,\x01",
            "huh?\x02\x03",

            "#010FWe'd better replace the orbment in the\x01",
            "road lamp on the Milch Main Road before\x01",
            "thinking about doing anything else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B2")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    ClearMapFlags(0x8000000)
    Jump("loc_4D5")

    label("loc_4D5")

    Return()

    # Function_0_66 end

    def Function_1_4D6(): pass

    label("Function_1_4D6")

    SetMapFlags(0x8000000)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -113140, 5930, 66530, 208)
    SetChrPos(0x102, -113990, 5950, 67470, 179)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_534")
    SetChrPos(0x2, -112370, 5890, 67560, 236)
    SetChrPos(0x3, -112920, 5990, 68310, 224)

    label("loc_534")

    OP_6D(-112920, 5990, 68310, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)

    ChrTalk(    #10
        0x101,
        "#2P#004FAh-HA!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    ChrTalk(    #11
        0x102,
        (
            "#014FWhat's with the sudden\x01",
            "outburst?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #12
        0x101,
        (
            "#2P#502FI've found it!\x02\x03",

            "#001FNow to claim our prize!\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x384, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #13
        "\x07\x00Found \x07\x02Firefly Fungus\x07\x00!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TurnDirection(0x102, 0x101, 400)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    PlayEffect(0x0, 0x0, 0x101, 0, 1000, 250, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    ChrTalk(    #14
        0x102,
        "#014FIsn't that...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #15
        0x101,
        (
            "#2P#508FYou think so, too?\x02\x03",

            "The place it's growing seems\x01",
            "about right, and it's got that\x01",
            "soft green glow.\x02\x03",

            "#001FThis has got to be that Firefly Fungus\x01",
            "that what's-his-face was talking about!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        "#017FYou mean, Orvid, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#2P#000FYeah, that's who I meant.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #18
        0x101,
        (
            "#2P#000FIt doesn't look all that tasty, but\x01",
            "it sure is pretty for a mushroom.\x02\x03",

            "#000FAlmost like the glow of septium,\x01",
            "if you ask me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8D7")
    TurnDirection(0x110, 0x101, 400)

    ChrTalk(    #19
        0x110,
        (
            "#151FWhen you put it that way,\x01",
            "it certainly does seem to\x01",
            "have that sort of aura.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D7")

    Sleep(400)

    ChrTalk(    #20
        0x102,
        "#014F...Septium?\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    TurnDirection(0x101, 0x102, 400)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #21
        0x101,
        "#2P#501FWhat's up, Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        (
            "#012FI may be worrying too much, but I think\x01",
            "you'd better put that mushroom in your\x01",
            "bag quickly, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #23
        0x101,
        "#2P#004F...What the--?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A5B")
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x102, 180, 400)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x110, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_A49():
        OP_8C(0x10F, 180, 400)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_A49)
    OP_8C(0x110, 180, 400)
    Jump("loc_A79")

    label("loc_A5B")

    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x102, 180, 400)

    label("loc_A79")

    Sleep(400)
    Fade(1000)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, -113010, 5920, 53930, 130)
    SetChrPos(0x9, -113010, 5920, 53930, 130)
    SetChrPos(0xA, -113010, 5920, 53930, 130)
    SetChrChipByIndex(0x8, 1)
    SetChrChipByIndex(0x9, 1)
    SetChrChipByIndex(0xA, 1)
    OP_6B(3300, 0)
    OP_6D(-115560, 6020, 58870, 0)
    OP_6C(270000, 0)
    OP_8C(0x101, 225, 0)
    OP_8C(0x102, 225, 0)
    OP_82(0x0, 0x0)
    OP_84(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B26")
    OP_8C(0x2, 225, 0)
    OP_8C(0x3, 225, 0)

    label("loc_B26")


    def lambda_B2C():
        OP_6D(-114970, 6000, 64120, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B2C)

    def lambda_B44():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_B44)
    OP_0D()

    def lambda_B55():
        OP_97(0x8, 0xFFFE4B8E, 0xF172, 0x124F8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B55)

    def lambda_B71():

        label("loc_B71")

        TurnDirection(0x8, 0x101, 0)
        OP_48()
        Jump("loc_B71")

    QueueWorkItem2(0x8, 2, lambda_B71)
    Sleep(400)

    def lambda_B87():
        OP_97(0x9, 0xFFFE4B8E, 0xF172, 0xFDE8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B87)

    def lambda_BA3():

        label("loc_BA3")

        TurnDirection(0x9, 0x101, 0)
        OP_48()
        Jump("loc_BA3")

    QueueWorkItem2(0x9, 2, lambda_BA3)
    Sleep(400)

    def lambda_BB9():
        OP_97(0xA, 0xFFFE4B8E, 0xF172, 0xD6D8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_BB9)

    def lambda_BD5():

        label("loc_BD5")

        TurnDirection(0xA, 0x101, 0)
        OP_48()
        Jump("loc_BD5")

    QueueWorkItem2(0xA, 2, lambda_BD5)
    WaitChrThread(0xA, 0x1)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrChipByIndex(0xA, 0)
    WaitChrThread(0x8, 0x1)
    OP_43(0x8, 0x0, 0x0, 0x2)
    SetChrChipByIndex(0x8, 0)
    Sleep(100)
    OP_43(0x9, 0x0, 0x0, 0x2)
    SetChrChipByIndex(0x9, 0)
    Sleep(1000)

    ChrTalk(    #24
        0x102,
        "#012FJust like I figured.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        "#004FThis mushroom attracts...?!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 3)
    TurnDirection(0x102, 0x8, 0)

    ChrTalk(    #26
        0x102,
        "#016FEstelle, look out!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 2)
    TurnDirection(0x101, 0x8, 0)

    def lambda_C98():

        label("loc_C98")

        TurnDirection(0x101, 0x8, 0)
        OP_48()
        Jump("loc_C98")

    QueueWorkItem2(0x101, 1, lambda_C98)

    def lambda_CA9():

        label("loc_CA9")

        TurnDirection(0x102, 0x8, 0)
        OP_48()
        Jump("loc_CA9")

    QueueWorkItem2(0x102, 1, lambda_CA9)
    OP_44(0xA, 0x0)
    OP_44(0x9, 0x0)
    OP_44(0x8, 0x0)

    def lambda_CC6():
        OP_6D(-113290, 5960, 66180, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_CC6)

    def lambda_CDE():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_CDE)
    SetChrChipByIndex(0x8, 1)

    def lambda_CF3():
        OP_97(0x8, 0xFFFE340A, 0x10234, 0xFFFE7960, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_CF3)
    Sleep(100)
    SetChrChipByIndex(0x9, 1)

    def lambda_D19():
        OP_97(0x9, 0xFFFE340A, 0x10234, 0xFFFEC780, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D19)
    Sleep(100)
    SetChrChipByIndex(0xA, 1)

    def lambda_D3F():
        OP_97(0xA, 0xFFFE340A, 0x10234, 0xFFFF15A0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D3F)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DBD")
    OP_62(0x10F, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x110, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_D8D():
        OP_8E(0x10F, 0xFFFE408A, 0x1748, 0x10AB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_D8D)

    def lambda_DA8():
        OP_8E(0x110, 0xFFFE3BEE, 0x1752, 0x10A2C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x110, 1, lambda_DA8)

    label("loc_DBD")

    WaitChrThread(0x8, 0x1)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DEC")
    OP_44(0x2, 0xFF)
    OP_44(0x3, 0xFF)

    label("loc_DEC")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0x3EA, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_E0E"),
        (SWITCH_DEFAULT, "loc_E11"),
    )


    label("loc_E0E")

    OP_B4(0x0)
    Return()

    label("loc_E11")

    EventBegin(0x0)
    SetChrPos(0x101, -113140, 5930, 66530, 208)
    SetChrPos(0x102, -113990, 5950, 67470, 179)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E65")
    SetChrPos(0x2, -112370, 5890, 67560, 236)
    SetChrPos(0x3, -112920, 5990, 68310, 224)

    label("loc_E65")

    OP_6D(-112920, 5990, 68310, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_64(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EB7")
    OP_8C(0x2, 180, 0)
    OP_8C(0x3, 180, 0)

    label("loc_EB7")

    OP_0D()
    OP_28(0x5, 0x1, 0x2)

    ChrTalk(    #27
        0x101,
        (
            "#2P#007FNow that was a surprise,\x01",
            "I tell ya.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 65535)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #28
        0x102,
        "#012FDid you put that thing away?\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #29
        0x101,
        "#2P#006FYep. It's all taken care of.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_108F")
    TurnDirection(0x10F, 0x102, 400)

    ChrTalk(    #30
        0x10F,
        (
            "#143FWhat was that all about?\x02\x03",

            "And why did a bunch of monsters\x01",
            "suddenly attack us?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10F, 400)

    ChrTalk(    #31
        0x102,
        (
            "#012FThe light emitted by raw septium\x01",
            "has the power to attract monsters...\x02\x03",

            "This mushroom also seems to\x01",
            "have the same effect.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x110, 0x102, 400)

    ChrTalk(    #32
        0x110,
        (
            "#153FThat's one far-out mushroom,\x01",
            "if you ask me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1112")

    label("loc_108F")


    ChrTalk(    #33
        0x102,
        (
            "#012FThe light emitted by raw septium\x01",
            "has the power to attract monsters...\x02\x03",

            "This mushroom also seems to\x01",
            "have the same effect.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1112")

    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #34
        0x101,
        (
            "#2P#009FThat sneaky merchant!\x02\x03",

            "#009FHe never mentioned a\x01",
            "single thing about this!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12A1")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #35
        0x102,
        (
            "#017FI'm pretty sure we'll be all right\x01",
            "carrying it around as long as\x01",
            "it's well packed away.\x02\x03",

            "Once we get back to town, I think\x01",
            "it would be best if we passed this\x01",
            "on to the client ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10F,
        (
            "#142F...\x02\x03",

            "Make sure you keep that thing\x01",
            "tucked in there good...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1325")

    label("loc_12A1")


    ChrTalk(    #37
        0x102,
        "#012FAnyway, let's hurry back to town.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#2P#005FRight!\x02\x03",

            "#005FJust wait till I get my hands on you,\x01",
            "you conniving merchant!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1325")

    EventEnd(0x0)
    ClearMapFlags(0x8000000)
    Return()

    # Function_1_4D6 end

    def Function_2_132D(): pass

    label("Function_2_132D")

    OP_A6(0x0)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFE3310, 0x1770, 0xE100, 0xBB8, 0x0)
    OP_43(0xFE, 0x2, 0x0, 0x2)
    OP_8C(0xFE, 315, 0)
    OP_A3(0x0)
    OP_A6(0x0)
    OP_8E(0xFE, 0xFFFE2F8C, 0x1770, 0xEA60, 0x1B58, 0x0)
    OP_A3(0x0)
    Return()

    # Function_2_132D end

    def Function_3_1375(): pass

    label("Function_3_1375")

    OP_A6(0x2)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFE3A18, 0x1770, 0xE290, 0xBB8, 0x0)
    OP_43(0xFE, 0x2, 0x0, 0x2)
    OP_8C(0xFE, 315, 0)
    OP_A3(0x2)
    OP_A6(0x2)
    OP_8E(0xFE, 0xFFFE3504, 0x1770, 0xEB28, 0x1B58, 0x0)
    OP_A3(0x2)
    Return()

    # Function_3_1375 end

    def Function_4_13BD(): pass

    label("Function_4_13BD")

    OP_A6(0x1)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFE4058, 0x1770, 0xE7A4, 0xBB8, 0x0)
    OP_43(0xFE, 0x2, 0x0, 0x2)
    OP_8C(0xFE, 315, 0)
    OP_A3(0x1)
    OP_A6(0x1)
    OP_8E(0xFE, 0xFFFE37C0, 0x1770, 0xEFD8, 0x1B58, 0x0)
    OP_A3(0x1)
    Return()

    # Function_4_13BD end

    def Function_5_1405(): pass

    label("Function_5_1405")

    OP_A6(0x4)
    Sleep(200)
    OP_8C(0x102, 225, 0)
    Sleep(400)
    OP_8E(0x102, 0xFFFE2EC4, 0x170C, 0xF6AE, 0xBB8, 0x0)
    OP_8C(0x102, 225, 0)
    OP_A3(0x4)
    Return()

    # Function_5_1405 end

    def Function_6_1438(): pass

    label("Function_6_1438")

    OP_6D(-120100, 5900, 62700, 800)
    Return()

    # Function_6_1438 end

    SaveToFile()

Try(main)
