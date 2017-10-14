from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1124   ._SN',
        MapName             = 'Bose',
        Location            = 'T1121.x',
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
        'Lugran',                               # 9
        'Mayor Maybelle',                       # 10
        'Scherazard',                           # 11
        'Olivier',                              # 12
        'Kloe',                                 # 13
        'Zin',                                  # 14
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


    AddCharChip(
        'ED6_DT07/CH02380 ._CH',             # 00
        'ED6_DT07/CH02360 ._CH',             # 01
        'ED6_DT07/CH00020 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00040 ._CH',             # 04
        'ED6_DT07/CH00070 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH02380P._CP',             # 00
        'ED6_DT07/CH02360P._CP',             # 01
        'ED6_DT07/CH00020P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00040P._CP',             # 04
        'ED6_DT07/CH00070P._CP',             # 05
    )

    DeclNpc(
        X                   = 180,
        Z                   = 0,
        Y                   = 4400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x114,
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_19B",          # 01, 1
        "Function_2_1C1",          # 02, 2
        "Function_3_186E",         # 03, 3
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Return()

    # Function_0_19A end

    def Function_1_19B(): pass

    label("Function_1_19B")

    OP_B1("T1121_2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1C0")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_1C0")

    Return()

    # Function_1_19B end

    def Function_2_1C1(): pass

    label("Function_2_1C1")

    EventBegin(0x0)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0xF8, 0x80)
    OP_6D(480, 0, 2930, 0)
    OP_67(0, 7230, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -70, 0, 2350, 0)
    SetChrPos(0xA, -1140, 0, 2340, 0)
    SetChrPos(0xD, -50, 0, 250, 0)
    SetChrPos(0xC, -320, 0, 1350, 0)
    SetChrPos(0xB, -1360, 0, 970, 0)
    SetChrPos(0x9, 970, 0, 1880, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x8,
        (
            "#634FSounds like you kids have had\x01",
            "a workout.\x02\x03",

            "#632FStill...to think Agate's past was that\x01",
            "terrible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        (
            "#618F#4PSadly, it makes sense. In some ways.\x02\x03",

            "#615FHearing this finally assembles all of the\x01",
            "pieces of the puzzle for me.\x02\x03",

            "It's no wonder Agate felt the way he did\x01",
            "back then...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3C0():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C0)
    Sleep(50)

    def lambda_3D3():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3D3)
    Sleep(50)

    def lambda_3E6():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3E6)
    Sleep(50)

    def lambda_3F9():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3F9)
    Sleep(50)
    OP_8C(0xB, 90, 400)

    ChrTalk(    #2
        0x101,
        "#1004FBack huh?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)
    Sleep(500)

    ChrTalk(    #3
        0x9,
        (
            "#612F#4PIt was ten years ago.\x02\x03",

            "Practically the day after the war ended,\x01",
            "Agate came to the mayor's house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1020FWhaaa...?! Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xC,
        "#044F#6PYou mean to YOUR house, Maybelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x9,
        (
            "#615F#4PYes, he barged in with...honestly, with\x01",
            "murder in his eyes, and came face to face\x01",
            "with my father, the mayor at the time.\x02\x03",

            "He demanded to know why the mayor of Bose,\x01",
            "the man responsible for the entire region...\x02\x03",

            "#612FHe demanded to know why he had abandoned\x01",
            "Ravennue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1026FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x9,
        (
            "#618F#4PI was just a child at the time, and it got to me\x01",
            "when I saw him arguing with Father for seemingly\x01",
            "no reason...\x02\x03",

            "So I, erm...leapt out and slapped him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1007FOh, MAN...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xA,
        (
            "#524F#3PI can see why he doesn't like\x01",
            "remembering THAT, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x9,
        (
            "#618F#4PYes...\x02\x03",

            "#612FThough, ultimately, Father never answered\x01",
            "Agate's question.\x02\x03",

            "He did say he was going to send financial aid\x01",
            "to help repairs.\x02\x03",

            "Agate grew even more livid when he heard that.\x01",
            "He even raised his fist to strike Father...\x02\x03",

            "#615F...But, then, he just left without throwing a blow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1015FSo THAT'S what happened...\x02\x03",

            "That's why the air between you two\x01",
            "seemed kind of...weird.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x9,
        (
            "#615F#4PYes. It's always hovered over us like\x01",
            "a cloud.\x02\x03",

            "#618FStill, to think Agate's sister died\x01",
            "in the war...\x02\x03",

            "I've been...terribly unfair to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1025FHe bears a bit of responsibility, too,\x01",
            "for not saying anything.\x02\x03",

            "You don't need to worry about it, Mayor Maybelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        (
            "#615F#4PI...suppose.\x02\x03",

            "#612FHow badly is Agate hurt?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1006FAh, don't worry, it's not too bad.\x02\x03",

            "He'll be up and surly again in two,\x01",
            "maybe three days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#630FHmph. Let's be thankful for\x01",
            "small mercies, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x9,
        (
            "#611F#4PYes, I'm glad to hear it's not serious.\x02\x03",

            "#618FYes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xC,
        (
            "#043F#6PThat, um...reminds me, Maybelle.\x02\x03",

            "How is Lila doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        (
            "#618F#4P...Well...\x02\x03",

            "Her injuries have been treated, but...\x01",
            "she hasn't come out of her coma yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xC,
        "#049F#6POh... I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xB,
        (
            "#032FHm. How despicable of our supposedly\x01",
            "lion-hearted fugitive.\x02\x03",

            "Lovely, refined ladies such as Lila are\x01",
            "treasures that ennoble the world simply\x01",
            "by existing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        (
            "#611F#4PHahaha... I'll tell Lila you said that\x01",
            "when she awakens.\x02\x03",

            "#610FOn the subject of good news...\x01",
            "I'm glad to hear that General Morgan\x01",
            "came to your aid.\x02\x03",

            "If the guild and army were to truly work\x01",
            "together, I'm convinced no force in the\x01",
            "world could stop you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xA,
        (
            "#026F#3PNothing's been decided yet, so we can't\x01",
            "make any promises...\x02\x03",

            "#027FBut just between you, me, and the desk...\x01",
            "we'll make it work.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 1880, 2000, 5270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC3, 0x1, 0x64)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_E49():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_E49)
    Sleep(50)

    def lambda_E5C():

        label("loc_E5C")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_E5C")

    QueueWorkItem2(0x101, 3, lambda_E5C)
    Sleep(50)

    def lambda_E72():

        label("loc_E72")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_E72")

    QueueWorkItem2(0xA, 3, lambda_E72)
    Sleep(50)

    def lambda_E88():

        label("loc_E88")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_E88")

    QueueWorkItem2(0xD, 3, lambda_E88)
    Sleep(50)

    def lambda_E9E():

        label("loc_E9E")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_E9E")

    QueueWorkItem2(0xC, 3, lambda_E9E)
    Sleep(50)

    def lambda_EB4():

        label("loc_EB4")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_EB4")

    QueueWorkItem2(0xB, 3, lambda_EB4)
    Sleep(50)

    def lambda_ECA():

        label("loc_ECA")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_ECA")

    QueueWorkItem2(0x9, 3, lambda_ECA)
    Sleep(100)

    def lambda_EE0():
        OP_6D(760, 0, 3570, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_EE0)
    OP_8E(0x8, 0x794, 0x0, 0x1252, 0x5DC, 0x0)
    OP_8C(0x8, 0, 400)
    OP_23(0xC3)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 1880, 2000, 5270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #25
        0x8,
        (
            "#630F#4PThis is the Bracer Guild,\x01",
            "Bose branch.\x02\x03",

            "#633FOh, General, sir! We've been waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1006F#6P(And here we go!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        (
            "#027F#6P(Now to see just how well Morgan\x01",
            "can set aside his pride.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#632F#4PHmmm... Oh, hmm?.\x02\x03",

            "#633FOh. So that's the plan, then!\x02\x03",

            "#630FI understand. Tomorrow at the landing port,\x01",
            "10 AM sharp.\x02\x03",

            "#631FI'll be sure to tell them.\x01",
            "Thank you, sir.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(500)
    OP_8C(0x8, 270, 400)

    def lambda_1105():
        OP_6D(480, 0, 2930, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1105)
    OP_8E(0x8, 0xB4, 0x0, 0x1130, 0x5DC, 0x0)
    OP_44(0x101, 0x3)
    OP_44(0xA, 0x3)
    OP_44(0xD, 0x3)
    OP_44(0xC, 0x3)
    OP_44(0x9, 0x3)
    OP_44(0xB, 0x3)

    def lambda_1149():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1149)

    def lambda_1157():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1157)

    def lambda_1165():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1165)

    def lambda_1173():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1173)

    def lambda_1181():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1181)
    OP_8C(0xB, 0, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #29
        0x101,
        "#1006FSo what's the word, Lugran?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "#632FThe Royal Army is going to execute a plan\x01",
            "to capture the dragon tomorrow, using\x01",
            "airships.\x02\x03",

            "They say they want you on one of the\x01",
            "airships as observers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#1004FThey're going to use airships? Whoa.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xB,
        (
            "#035F#2PTaking the battle to our foe in his\x01",
            "element, then?\x02\x03",

            "#030FAnd with the elite of the Liberlian\x01",
            "military...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xA,
        (
            "#026F#6PWell. If we're just 'observers' we won't be\x01",
            "able to actually DO anything...\x02\x03",

            "#027FEven so, I'm still grateful for a chance\x01",
            "to get a closer look at that dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xD,
        (
            "#070F#4PAnd it might just be up to us if\x01",
            "the army fails somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1006FNo rest for the weary then, huh?\x01",
            "I'm up for it!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)
    Sleep(500)

    ChrTalk(    #36
        0x9,
        (
            "#611F#4PHaha... At last, some light at\x01",
            "the end of the tunnel.\x02\x03",

            "#618F...Uhn...\x02",
        )
    )

    CloseMessageWindow()
    Fade(800)

    def lambda_149B():
        OP_6D(530, 0, 2880, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_149B)
    Sleep(400)

    def lambda_14B8():
        OP_6D(480, 0, 2930, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14B8)
    Sleep(400)
    OP_0D()
    Sleep(500)

    def lambda_14DB():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_14DB)
    Sleep(50)

    def lambda_14EE():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14EE)
    Sleep(50)

    def lambda_1501():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1501)
    Sleep(50)

    def lambda_1514():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1514)
    Sleep(50)
    OP_8C(0xB, 90, 400)

    ChrTalk(    #37
        0xC,
        "#043F#6PMaybelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#1020FMayor Maybelle, are you all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        "#617F#4PYes, it was nothing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xB,
        (
            "#032FYou looked dizzy enough to be a toy top, Mayor.\x01",
            "You must be exhausted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        "#618F#4PBut...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        (
            "#524F#3PI know what Estelle just said, Mayor,\x01",
            "but don't strain yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        (
            "#617F#4PHaha... Don't worry, really.\x01",
            "I'm hardly straining myself.\x02\x03",

            "#610FDuring the Hundred Days War, Father did\x01",
            "everything he could to protect Bose.\x02\x03",

            "One time, he even conducted extremely\x01",
            "dangerous negotiations in order to deceive\x01",
            "the Imperial Army.\x02\x03",

            "Compared to what he did...this is nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1026FMayor Maybelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xC,
        "#043F#6POh, Maybelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        (
            "#611F#4PEstelle, everyone.\x01",
            "Please take care of things.\x02\x03",

            "Please, dispel the fear that haunts the\x01",
            "people of Bose... and Ravennue!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1006FYeah... Leave it to us!\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1211   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1C1 end

    def Function_3_186E(): pass

    label("Function_3_186E")

    FadeToDark(0, 0, -1)
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1924"),
        (1, "loc_192A"),
        (SWITCH_DEFAULT, "loc_1930"),
    )


    label("loc_1924")

    OP_A2(0x1200)
    Jump("loc_1930")

    label("loc_192A")

    OP_A2(0x1201)
    Jump("loc_1930")

    label("loc_1930")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x3, 0x0, 0xFF, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_3_186E end

    SaveToFile()

Try(main)
