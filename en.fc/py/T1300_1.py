from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1300_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
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
    )

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_A0B",          # 01, 1
        "Function_2_A26",          # 02, 2
        "Function_3_A55",          # 03, 3
        "Function_4_A84",          # 04, 4
        "Function_5_AB3",          # 05, 5
        "Function_6_B0F",          # 06, 6
    )


    def Function_0_66(): pass

    label("Function_0_66")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x0, -39200, 0, 31000, 0)
    SetChrPos(0x1, -39200, 0, 32200, 0)
    SetChrPos(0x2, -39200, 0, 33400, 0)
    SetChrPos(0xA, -39200, 0, 34600, 0)
    OP_43(0x0, 0x1, 0x1, 0x1)
    OP_43(0x1, 0x1, 0x1, 0x2)
    OP_43(0x2, 0x1, 0x1, 0x3)
    OP_43(0xA, 0x1, 0x1, 0x4)
    OP_A2(0x1)
    OP_A2(0x2)
    OP_A2(0x3)
    OP_A2(0x4)

    def lambda_DF():
        OP_6C(225000, 8000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_DF)

    def lambda_EF():
        OP_6B(2800, 8000)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_EF)
    OP_6D(-50000, 0, 6500, 8000)
    OP_A5(0x1)
    OP_44(0x1, 0xFF)
    OP_44(0x2, 0xFF)
    OP_44(0xA, 0xFF)
    Fade(1000)
    SetChrPos(0x101, -51000, 0, 18400, 180)
    SetChrPos(0x102, -50000, 0, 20000, 180)
    SetChrPos(0x103, -50000, 0, 17200, 180)
    SetChrPos(0xA, -48500, 0, 21500, 180)
    OP_69(0x101, 0x0)

    def lambda_16F():
        OP_8E(0x101, 0xFFFF38C8, 0x0, 0x43F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16F)

    def lambda_18A():
        OP_8E(0x102, 0xFFFF3CB0, 0x0, 0x4A38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18A)

    def lambda_1A5():
        OP_8E(0x103, 0xFFFF3CB0, 0x0, 0x3DB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A5)

    def lambda_1C0():
        OP_8E(0xA, 0xFFFF428C, 0x0, 0x43F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1C0)

    def lambda_1DB():
        OP_6D(-50000, 0, 17400, 2000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1DB)
    Sleep(1000)
    Sleep(2000)

    ChrTalk(    #0
        0xA,
        (
            "#5PWell, it looks like we finally\x01",
            "made it...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #1
        0x101,
        (
            "#007FWhew, that was a pretty rough\x01",
            "climb, huh?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #2
        0x102,
        "#010FWell, we can breathe easy now.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xA, 400)

    ChrTalk(    #3
        0x103,
        (
            "#020FI think your escort from Ruan should\x01",
            "be here any time now.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_8C(0x103, 180, 400)
    Sleep(800)

    ChrTalk(    #4
        0x103,
        (
            "#020F...And speak of the devil.\x01",
            "Look who's here.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xB, -50000, 500, 8700, 0)
    ClearChrFlags(0xB, 0x80)

    def lambda_35C():

        label("loc_35C")

        TurnDirection(0x101, 0xB, 400)
        OP_48()
        Jump("loc_35C")

    QueueWorkItem2(0x101, 1, lambda_35C)

    def lambda_36D():

        label("loc_36D")

        TurnDirection(0x102, 0xB, 400)
        OP_48()
        Jump("loc_36D")

    QueueWorkItem2(0x102, 1, lambda_36D)

    def lambda_37E():

        label("loc_37E")

        TurnDirection(0x103, 0xB, 400)
        OP_48()
        Jump("loc_37E")

    QueueWorkItem2(0x103, 1, lambda_37E)

    def lambda_38F():

        label("loc_38F")

        TurnDirection(0xA, 0xB, 400)
        OP_48()
        Jump("loc_38F")

    QueueWorkItem2(0xA, 1, lambda_38F)
    OP_70(0x1, 0x64)
    OP_73(0x1)
    OP_6F(0x1, 100)
    OP_70(0x1, 0x0)
    OP_8E(0xB, 0xFFFF3CB0, 0x1F4, 0x3390, 0xBB8, 0x0)
    OP_8E(0xB, 0xFFFF42F0, 0x1F4, 0x3DB8, 0xBB8, 0x0)
    TurnDirection(0xB, 0x103, 400)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_44(0xA, 0xFF)
    Sleep(800)

    ChrTalk(    #5
        0xB,
        "Good work, everyone!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xB,
        (
            "I'm junior bracer, Melvin, registered\x01",
            "with the Ruan branch!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x103,
        (
            "#020F#4PGood work, yourself. This is\x01",
            "your client, Mr. Hardt.\x02\x03",

            "Please make sure he gets to\x01",
            "Ruan safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xB,
        "Will do!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(    #9
        0xB,
        (
            "Just follow me, sir! I'll get you\x01",
            "where you need to go!\x01",
            "I'm your man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xA,
        (
            "#2PBy Aidios...\x01",
            "Just how much coffee have\x01",
            "you had, young man...?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xA,
        (
            "#2PBut whatever, I'm counting on you\x01",
            "to get me where I need to go.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #12
        0xA,
        (
            "All right, thanks for getting me up\x01",
            "here, everyone.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #13
        0x101,
        "#001FHave a good one!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xA, 400)

    ChrTalk(    #14
        0x102,
        "#010FGood luck with your work.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(    #15
        0xA,
        "#1PHa ha. Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xA,
        (
            "I'm already late as it is,\x01",
            "but I'll see what I can do.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x103, 400)

    ChrTalk(    #17
        0xB,
        (
            "Okay, have a good day,\x01",
            "fellow bracers!!\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xB, 0x1, 0x1, 0x5)
    OP_43(0xA, 0x1, 0x1, 0x6)
    OP_A2(0x5)
    OP_A2(0x6)

    def lambda_6E1():

        label("loc_6E1")

        TurnDirection(0x101, 0xA, 400)
        OP_48()
        Jump("loc_6E1")

    QueueWorkItem2(0x101, 1, lambda_6E1)

    def lambda_6F2():

        label("loc_6F2")

        TurnDirection(0x102, 0xA, 400)
        OP_48()
        Jump("loc_6F2")

    QueueWorkItem2(0x102, 1, lambda_6F2)

    def lambda_703():

        label("loc_703")

        TurnDirection(0x103, 0xA, 400)
        OP_48()
        Jump("loc_703")

    QueueWorkItem2(0x103, 1, lambda_703)
    OP_A5(0x5)
    OP_A5(0x7)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x103, 0xFF)
    OP_6F(0x1, 100)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    Sleep(1000)

    ChrTalk(    #18
        0x101,
        (
            "#004FThat guy was really over the\x01",
            "top energy-wise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#010FHe said he was a junior bracer,\x01",
            "right?\x02\x03",

            "Which means he's a trainee just\x01",
            "like us working out of a branch...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 400)

    ChrTalk(    #20
        0x103,
        (
            "#020FYep, you're not the only ones.\x01",
            "All junior bracers do that.\x02\x03",

            "They're working hard to become\x01",
            "senior bracers.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #21
        0x101,
        (
            "#002FOh man, it looks like I'm going\x01",
            "to have to work harder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        (
            "#010FThat's right.\x02\x03",

            "It wouldn't be right of us just to\x01",
            "rely on Schera all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x103,
        (
            "#021FHa ha. It looks like that bracer\x01",
            "stimulated your motivation a\x01",
            "bit, didn't he?\x02\x03",

            "Let's see now... How about we get\x01",
            "back and report to the guild?\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x10, 0x4, 0x10)
    OP_28(0x10, 0x3, 0x8)
    OP_28(0x10, 0x1, 0x20)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x00Quest \x07\x02[Escort Request] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    def Function_1_A0B(): pass

    label("Function_1_A0B")

    OP_A6(0x1)
    OP_8E(0x0, 0xFFFF3CB0, 0x0, 0x4650, 0x7D0, 0x0)
    OP_A3(0x1)
    Return()

    # Function_1_A0B end

    def Function_2_A26(): pass

    label("Function_2_A26")

    OP_A6(0x2)
    OP_8E(0x1, 0xFFFF66E0, 0x0, 0x7918, 0x7D0, 0x0)
    OP_8E(0x1, 0xFFFF3CB0, 0x0, 0x4650, 0x7D0, 0x0)
    OP_A3(0x2)
    Return()

    # Function_2_A26 end

    def Function_3_A55(): pass

    label("Function_3_A55")

    OP_A6(0x3)
    OP_8E(0x2, 0xFFFF66E0, 0x0, 0x7918, 0x7D0, 0x0)
    OP_8E(0x2, 0xFFFF3CB0, 0x0, 0x4650, 0x7D0, 0x0)
    OP_A3(0x3)
    Return()

    # Function_3_A55 end

    def Function_4_A84(): pass

    label("Function_4_A84")

    OP_A6(0x4)
    OP_8E(0xA, 0xFFFF66E0, 0x0, 0x7918, 0x7D0, 0x0)
    OP_8E(0xA, 0xFFFF3CB0, 0x0, 0x4650, 0x7D0, 0x0)
    OP_A3(0x4)
    Return()

    # Function_4_A84 end

    def Function_5_AB3(): pass

    label("Function_5_AB3")

    OP_A6(0x5)
    OP_8E(0xB, 0xFFFF3CB0, 0x1F4, 0x3390, 0x7D0, 0x0)
    OP_8E(0xB, 0xFFFF3CB0, 0x1F4, 0x28DA, 0x7D0, 0x0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x64)
    OP_73(0x1)
    OP_A2(0x7)
    OP_8E(0xB, 0xFFFF3CB0, 0x1F4, 0x1A2C, 0x7D0, 0x0)
    SetChrFlags(0xB, 0x80)
    OP_A3(0x5)
    Return()

    # Function_5_AB3 end

    def Function_6_B0F(): pass

    label("Function_6_B0F")

    OP_A6(0x6)
    OP_8E(0xA, 0xFFFF42F0, 0x1F4, 0x3DB8, 0x7D0, 0x0)
    OP_8E(0xA, 0xFFFF3CB0, 0x1F4, 0x3390, 0x7D0, 0x0)
    OP_8E(0xA, 0xFFFF3CB0, 0x1F4, 0x2C88, 0x3E8, 0x0)
    OP_A3(0x6)
    OP_A6(0x7)
    OP_8E(0xA, 0xFFFF3CB0, 0x1F4, 0x21FC, 0x7D0, 0x0)
    SetChrFlags(0xA, 0x80)
    OP_A3(0x7)
    Return()

    # Function_6_B0F end

    SaveToFile()

Try(main)
