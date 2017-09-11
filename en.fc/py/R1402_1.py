from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R1402_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'R1402.x',
        MapIndex            = 58,
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
    )


    def Function_0_66(): pass

    label("Function_0_66")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    RemoveParty(0xD, 0xFF)
    ClearChrFlags(0x8, 0x80)
    OP_28(0xF, 0x4, 0x10)
    SetChrPos(0x101, 2200, 4000, 17880, 270)
    SetChrPos(0x102, 3120, 4000, 16810, 270)
    SetChrPos(0x103, 3250, 4000, 17800, 285)
    SetChrPos(0x8, -200, 4000, 17880, 90)
    OP_6D(20070, 0, 19800, 0)
    OP_6C(315000, 0)
    OP_6B(4000, 0)
    FadeToBright(2000, 0)

    def lambda_F0():
        OP_69(0x101, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F0)

    def lambda_FE():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_FE)

    def lambda_10E():
        OP_6B(3000, 6000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_10E)
    Sleep(7000)
    OP_44(0x9, 0xFF)

    ChrTalk(    #0
        0x8,
        (
            "#130F#3POh, goodness, you helped me out\x01",
            "of a mess again.\x02\x03",

            "If you hadn't come along when you\x01",
            "did, I might have been done for\x01",
            "good this time.\x02\x03",

            "I've managed to get a little funding for\x01",
            "my research, so I'll send a payment to\x01",
            "the guild as a token of my gratitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#007FLike I told you before, hire a\x01",
            "bracer to escort you around!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #2
        0x8,
        (
            "#130F#3PFunds permitting, I will seriously\x01",
            "look into that next time.\x02\x03",

            "Anyway, I must be going now.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x3E8, 0xFA0, 0x3EE4, 0x7D0, 0x0)

    def lambda_2F8():

        label("loc_2F8")

        TurnDirection(0x101, 0x8, 0)
        OP_48()
        Jump("loc_2F8")

    QueueWorkItem2(0x101, 1, lambda_2F8)

    def lambda_309():

        label("loc_309")

        TurnDirection(0x102, 0x8, 0)
        OP_48()
        Jump("loc_309")

    QueueWorkItem2(0x102, 1, lambda_309)

    def lambda_31A():

        label("loc_31A")

        TurnDirection(0x103, 0x8, 0)
        OP_48()
        Jump("loc_31A")

    QueueWorkItem2(0x103, 1, lambda_31A)
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x103, 0x8, 400)

    ChrTalk(    #3
        0x103,
        (
            "#023FAre you sure you don't need to\x01",
            "be escorted back to town?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(    #4
        0x8,
        (
            "#130FAh ha ha ha, if I did that then my\x01",
            "wallet would truly be barren.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #5
        0x8,
        (
            "#132FFarewell, everyone...I hope we\x01",
            "can meet again someplace.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_423():
        OP_6D(2910, 4000, 17460, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_423)
    OP_8E(0x8, 0x424, 0x4B0, 0x253A, 0x7D0, 0x0)
    SetChrFlags(0x8, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x103, 0x1)
    OP_44(0x8, 0x2)

    ChrTalk(    #6
        0x102,
        "#014F#6PHe certainly is a strange one...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #7
        0x101,
        (
            "#501FYou think so?\x02\x03",

            "He seems like the typical academic\x01",
            "to me.\x02\x03",

            "You know, the type that gets lost\x01",
            "in whatever they're doing.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #8
        0x102,
        (
            "#018FYou're definitely not one of those\x01",
            "people, that's for sure...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #9
        0x101,
        (
            "#009FHey! \x02\x03",

            "Even I know better than to come\x01",
            "waltzing into a place like this\x01",
            "alone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x103,
        (
            "#026FBut, for a scholar, he may just be\x01",
            "more than meets the eye.\x02\x03",

            "For one, he came here by himself.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #11
        0x101,
        (
            "#007FMaybe you're right...\x02\x03",

            "But we're the ones who ended up\x01",
            "having to save his behind.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #12
        0x103,
        (
            "#020F#4PWell, that's just part of the bracer\x01",
            "line of work.\x02\x03",

            "Anyway, how about we get going?\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x00Quest \x07\x02[Amberl Tower Mystery] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    SaveToFile()

Try(main)
