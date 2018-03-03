from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3100   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        'Private Samuel',                       # 9
        'Royal Army Officer',                   # 10
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01310 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -3230,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_FA",           # 00, 0
        "Function_1_123",          # 01, 1
        "Function_2_129",          # 02, 2
        "Function_3_C14",          # 03, 3
        "Function_4_C30",          # 04, 4
        "Function_5_C58",          # 05, 5
    )


    def Function_0_FA(): pass

    label("Function_0_FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_122")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_122")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_122")

    Return()

    # Function_0_FA end

    def Function_1_123(): pass

    label("Function_1_123")

    OP_22(0x1CD, 0x1, 0x5A)
    Return()

    # Function_1_123 end

    def Function_2_129(): pass

    label("Function_2_129")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10A, 420, 0, -55520, 0)
    OP_6D(250, 3770, -2820, 0)
    OP_67(0, 8930, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(435, 0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00Three days later...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(1000)
    OP_1D(0x65)

    def lambda_1D0():
        OP_6D(250, 3770, -42460, 6000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1D0)

    def lambda_1E8():
        OP_8E(0xFE, 0x140, 0x0, 0xFFFF5E48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1E8)
    FadeToBright(2000, 0)
    OP_0D()
    OP_C8(0x200, 0x46, "C_PLAC10._CH", 0x0, 0x7D0)
    WaitChrThread(0x10A, 0x0)
    Fade(500)
    OP_6D(1120, 0, -40520, 0)
    OP_67(0, 7410, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(45000, 0)
    OP_6E(307, 0)
    OP_0D()
    WaitChrThread(0x10A, 0x1)
    Sleep(500)

    ChrTalk(    #1
        0x10A,
        (
            "#810F#5PWhew... So this is Leiston Fortress.\x02\x03",

            "It definitely looks the part, at least. It's huge.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_2DF():
        OP_8E(0xFE, 0x10E, 0x0, 0xFFFFEA7A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_2DF)
    Sleep(3000)
    Fade(1000)
    OP_6D(1190, 0, -3550, 0)
    OP_67(0, 7940, -10000, 0)
    OP_6B(2810, 0)
    OP_6C(44000, 0)
    OP_6E(274, 0)
    OP_0D()
    OP_44(0x10A, 0x0)
    SetChrPos(0x10A, 150, 250, -14360, 0)
    Sleep(500)

    def lambda_35C():
        OP_8E(0xFE, 0x10E, 0x0, 0xFFFFEA7A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_35C)
    WaitChrThread(0x10A, 0x0)

    ChrTalk(    #2
        0x10,
        "#5PHmm? Can I help you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10A,
        (
            "#810FUmm... Well, I'd like to meet with Brigadier\x01",
            "General Bright, if that's possible...\x02\x03",

            "He wouldn't happen to be free now, would he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#5PUnfortunately not. He's a very busy man, as you\x01",
            "can imagine.\x02\x03",

            "Don't expect to be able to meet with him any time\x01",
            "soon without getting touch in advance to arrange\x01",
            "an appointment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10A,
        (
            "#810FWhat, really? Aww...\x02\x03",

            "I took time off to come all the way here, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#5PThat's unfortunate, but there really is nothing\x01",
            "I can do here.\x02\x03",

            "Still, while I can't imagine it doing any good,\x01",
            "I suppose I can at least pass on that you're\x01",
            "here and what you came for.\x02\x03",

            "So, do you mind if I ask what business you\x01",
            "have with the general?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10A,
        (
            "#810FO-Oh, thank you...\x02\x03",

            "Well, you see...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrPos(0x10A, 3380, 250, -9200, 90)
    OP_6D(4950, 250, -8010, 0)
    OP_67(0, 5710, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(44000, 0)
    OP_6E(294, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #8
        0x10A,
        (
            "#810F#5PWhew...\x02\x03",

            "I really don't want to have to go back empty\x01",
            "handed after coming all the way here...\x02\x03",

            "...I suppose if I can't meet with Cassius, I could\x01",
            "at least go shopping in the department store over\x01",
            "in Grancel.\x02\x03",

            "...Yeah! Let's go with that!\x02\x03",

            "Nothing cures a depressive slump like\x01",
            "some shopping.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x10, 0x334, 0x0, 0xFFFFEB88, 0x7D0, 0x0)

    ChrTalk(    #9
        0x10,
        (
            "#2PHey, young lady.\x02\x03",

            "It looks like he can meet you after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10A, 0, 400)

    ChrTalk(    #10
        0x10A,
        "#810F#2PReally?\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 70, 0, 4000, 180)
    OP_22(0x6C, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1C2)
    Fade(500)
    OP_6D(40, 2450, -2700, 0)
    OP_67(0, 2060, -10000, 0)
    OP_6B(3580, 0)
    OP_6C(0, 0)
    OP_6E(365, 0)
    OP_8C(0x10, 0, 400)
    OP_0D()
    Sleep(1000)

    def lambda_8EF():
        OP_6D(570, 0, -3080, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_8EF)

    def lambda_907():
        OP_67(0, 4600, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_907)

    def lambda_91F():
        OP_6B(2580, 5000)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_91F)

    def lambda_92F():
        OP_6E(327, 5000)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_92F)
    OP_43(0x10, 0x0, 0x0, 0x4)
    Sleep(1000)
    OP_43(0x10A, 0x0, 0x0, 0x3)
    OP_73(0x0)
    OP_8F(0x11, 0x19A, 0x0, 0xFFFFF222, 0xBB8, 0x0)
    WaitChrThread(0x10A, 0x3)

    ChrTalk(    #11
        0x10,
        "#2PGood day, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        (
            "#5PVery good.\x02\x03",

            "You're Anelace, I take it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10A,
        "#810FY-Yes, I am...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        (
            "#5PWow... It's hard to believe you're the\x01",
            "granddaughter of a legendary swordsman...\x02\x03",

            "...but I suppose this isn't the time to be talking\x01",
            "about this.\x02\x03",

            "The general's waiting for you. Follow me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10A,
        "#810FWhat, I can really meet him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x11,
        (
            "#5PYes. He kindly agreed to take time out of his\x01",
            "schedule specially to meet you.\x02\x03",

            "So let's hurry along. We don't want to keep him\x01",
            "waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10A,
        "#810FR-Right!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 400)

    def lambda_B62():
        OP_6D(80, 0, 4520, 5000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_B62)

    def lambda_B7A():
        OP_67(0, 4000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B7A)

    def lambda_B92():
        OP_6B(3010, 5000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_B92)

    def lambda_BA2():
        OP_6E(347, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_BA2)

    def lambda_BB2():
        OP_8E(0xFE, 0x46, 0x0, 0x222E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_BB2)
    Sleep(400)

    def lambda_BD2():
        OP_8E(0xFE, 0x46, 0x0, 0x222E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_BD2)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x2)
    OP_44(0x10, 0x3)
    OP_A2(0x2506)
    NewScene("ED6_DT21/C3110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_129 end

    def Function_3_C14(): pass

    label("Function_3_C14")

    OP_8E(0xFE, 0x12C, 0xD2, 0xFFFFE3D6, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_3_C14 end

    def Function_4_C30(): pass

    label("Function_4_C30")


    def lambda_C36():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C36)
    OP_8F(0xFE, 0x82A, 0x0, 0xFFFFEB88, 0x5DC, 0x0)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_4_C30 end

    def Function_5_C58(): pass

    label("Function_5_C58")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10A, 420, 0, -55520, 0)
    OP_6D(250, 3770, -2820, 0)
    OP_67(0, 8930, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(435, 0)
    OP_1D(0x65)
    OP_C8(0x200, 0x46, "C_PLAC10._CH", 0x0, 0x7D0)

    def lambda_CD4():
        OP_6D(250, 3770, -42460, 6000)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_CD4)

    def lambda_CEC():
        OP_8E(0xFE, 0x140, 0x0, 0xFFFF5E48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_CEC)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10A, 0x0)
    Fade(500)
    OP_6D(1120, 0, -40520, 0)
    OP_67(0, 7410, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(45000, 0)
    OP_6E(307, 0)
    OP_0D()
    WaitChrThread(0x10A, 0x1)
    Sleep(500)

    ChrTalk(    #18
        0x10A,
        (
            "#1316F#6PWhew... I'm finally here.\x02\x03",

            "#816FRight on time, too. Okay! Let's go bug\x01",
            "Cassius!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DC1():
        OP_8E(0xFE, 0x10E, 0x0, 0xFFFFEA7A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_DC1)
    Sleep(3000)
    Fade(1000)
    OP_6D(1190, 0, -2550, 0)
    OP_67(0, 7940, -10000, 0)
    OP_6B(2810, 0)
    OP_6C(44000, 0)
    OP_6E(274, 0)
    OP_44(0x10A, 0x0)
    SetChrPos(0x10A, 150, 250, -12360, 0)
    OP_0D()
    Sleep(500)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #19
        0x10,
        "#5PHmm? Can I help you?\x02",
    )

    CloseMessageWindow()

    def lambda_E77():
        OP_8E(0xFE, 0x10E, 0x0, 0xFFFFEA7A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_E77)
    OP_6D(1190, 0, -3550, 2300)
    WaitChrThread(0x10A, 0x0)
    Sleep(500)

    ChrTalk(    #20
        0x10A,
        (
            "#1310F#12PUmm... Well, I'm Anelace Elfead, a bracer with\x01",
            "the guild.\x02\x03",

            "I've come to meet with Brigadier General Bright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        "#5PAh, I see. I believe we've been expecting you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        "#5PI'll pass on that you've arrived, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "#5PYou might have to wait a little while before you\x01",
            "can meet with the general, though, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10A,
        (
            "#814F#12PHuh? But I'm right on time...\x02\x03",

            "Did something throw his schedule off?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#5PSomething must have. I can't pretend to know\x01",
            "much more than you do...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "#5P...but the general is a very busy man, so it's not\x01",
            "at all unusual for things like this to happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "#5PAnyway, like I said, I'll pass on that you've\x01",
            "arrived, but I'm going to have to ask you to\x01",
            "wait out here for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10A,
        "#816F#12PSure. No problem...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    SetChrPos(0x10A, 3380, 250, -9200, 90)
    OP_6D(4950, 250, -8010, 0)
    OP_67(0, 5710, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(44000, 0)
    OP_6E(294, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #29
        0x10A,
        (
            "#813F#5PThis is taking ages...\x02\x03",

            "I hope the meeting isn't going to end up getting\x01",
            "canceled or something.\x02\x03",

            "#1316F*sigh* I really don't want to have come all this\x01",
            "way for nothing...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10A)
    Sleep(500)

    ChrTalk(    #30
        0x10A,
        (
            "#816F#5PI suppose if I can't meet with Cassius, I could\x01",
            "at least go shopping in Grancel.\x02\x03",

            "They should probably be getting the new lineup\x01",
            "of stuffed toys around now...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #31
        0x10A,
        (
            "#1311F#5PI wonder which one I should get?\x01",
            "Maybe the bear? Or a crocodile\x01",
            "once in a while would be nice... ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x10, 0x334, 0x0, 0xFFFFEB88, 0x7D0, 0x0)
    Sleep(300)

    ChrTalk(    #32
        0x10,
        "#2PExcuse me, young lady.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        "#2PThe general can meet with you now.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10A, 0, 400)
    Sleep(300)

    ChrTalk(    #34
        0x10A,
        "#814F#11PReally?\x02",
    )

    CloseMessageWindow()
    OP_59()
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 0, 0, 4000, 180)
    OP_22(0x6C, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1C2)
    Fade(500)
    OP_6D(40, 2450, -2700, 0)
    OP_67(0, 2060, -10000, 0)
    OP_6B(3580, 0)
    OP_6C(0, 0)
    OP_6E(365, 0)
    OP_8C(0x10, 0, 400)
    OP_0D()
    Sleep(1000)

    def lambda_153F():
        OP_6D(570, 0, -3080, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_153F)

    def lambda_1557():
        OP_67(0, 4600, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_1557)

    def lambda_156F():
        OP_6B(2580, 5000)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_156F)

    def lambda_157F():
        OP_6E(327, 5000)
        ExitThread()

    QueueWorkItem(0x10A, 3, lambda_157F)
    OP_43(0x10, 0x0, 0x0, 0x4)
    Sleep(1500)
    OP_43(0x10A, 0x0, 0x0, 0x3)
    OP_73(0x0)
    OP_8F(0x11, 0x0, 0x0, 0xFFFFF222, 0xBB8, 0x0)
    WaitChrThread(0x10A, 0x3)

    ChrTalk(    #35
        0x10,
        "#2PGood day, sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x11,
        "#5PThank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x11,
        "#5PAnd you must be Anelace, I assume?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10A,
        "#814F#6PY-Yes, I am...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x11,
        "#5PWelcome to Leiston Fortress.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x11,
        "#5PThe general is waiting. Please follow me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10A,
        (
            "#1310F#6POh, thank goodness!\x02\x03",

            "#811FI seriously thought I was going to have to\x01",
            "go home without getting to see him!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x11,
        "#5PI'm terribly sorry for the wait.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x11,
        "#5PWell, please follow me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10A,
        "#816F#6PYou got it, sir!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 400)

    def lambda_176B():
        OP_6D(80, 0, 4520, 5000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_176B)

    def lambda_1783():
        OP_67(0, 4000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1783)

    def lambda_179B():
        OP_6B(3010, 5000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_179B)

    def lambda_17AB():
        OP_6E(347, 5000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_17AB)

    def lambda_17BB():
        OP_8E(0xFE, 0x46, 0x0, 0x222E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_17BB)
    Sleep(400)

    def lambda_17DB():
        OP_8E(0xFE, 0x46, 0x0, 0x222E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_17DB)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x1)
    OP_44(0x10, 0x2)
    OP_44(0x10, 0x3)
    SetMapFlags(0x2000000)
    OP_A2(0x2506)
    NewScene("ED6_DT21/C3110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_C58 end

    SaveToFile()

Try(main)
