from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4144   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4144.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Erika Russell',                        # 9
        'Lt. Colonel Cid',                      # 10
        'Recluse Cube',                         # 11
        'Recluse Cube',                         # 12
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
        'ED6_DT27/CH03970 ._CH',             # 00
        'ED6_DT27/CH03590 ._CH',             # 01
        'ED6_DT26/CH20607 ._CH',             # 02
        'ED6_DT26/CH20622 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT27/CH03970P._CP',             # 00
        'ED6_DT27/CH03590P._CP',             # 01
        'ED6_DT26/CH20607P._CP',             # 02
        'ED6_DT26/CH20622P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_14A",          # 00, 0
        "Function_1_17D",          # 01, 1
        "Function_2_17E",          # 02, 2
        "Function_3_A6D",          # 03, 3
        "Function_4_3981",         # 04, 4
    )


    def Function_0_14A(): pass

    label("Function_0_14A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_169")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_17C")

    label("loc_169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_17C")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_17C")

    Return()

    # Function_0_14A end

    def Function_1_17D(): pass

    label("Function_1_17D")

    Return()

    # Function_1_17D end

    def Function_2_17E(): pass

    label("Function_2_17E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x109, -280, 0, 310, 0)
    SetChrPos(0x11, 460, 0, -2310, 0)
    SetChrPos(0x10, -780, 0, -1580, 0)
    OP_6D(-1630, -1000, 27520, 0)
    OP_67(0, 8029, -10000, 0)
    OP_6B(6000, 0)
    OP_6C(44000, 0)
    OP_6E(354, 0)

    def lambda_20F():
        OP_6B(7650, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_20F)
    FadeToBright(2000, 0)
    OP_0D()
    OP_C8(0x200, 0x46, "C_PLAC31._CH", 0x0, 0x3E8)

    def lambda_23E():
        OP_8E(0xFE, 0xFFFFFFBA, 0xFFFFFC18, 0x4722, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_23E)
    Sleep(50)

    def lambda_25E():
        OP_8E(0xFE, 0xFFFFFD30, 0xFFFFFC18, 0x3FAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_25E)
    Sleep(100)

    def lambda_27E():
        OP_8E(0xFE, 0x262, 0xFFFFFC18, 0x3F34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_27E)
    WaitChrThread(0x109, 0x2)
    Sleep(2000)
    Fade(1000)
    OP_6D(1280, -1000, 18410, 0)
    OP_67(0, 5460, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(45000, 0)
    OP_6E(226, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x10,
        "#1459F#6PWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x11,
        (
            "#703F#4PUnbelievable...\x02\x03",

            "#701FAll these years, I had no idea that such a place\x01",
            "lay hidden beneath Grancel Cathedral.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)

    ChrTalk(    #2
        0x109,
        (
            "#1060F#5PWell, it's not exactly something we publicize.\x01",
            "It was built in accordance with the agreements\x01",
            "between the church and royal family.\x02\x03",

            "#1065FIt has but one purpose:\x02\x03",

            "#1063FTo suppress the power of ancient artifacts and\x01",
            "keep their influence in check.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        "#1457F#6P...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x11,
        (
            "#701F#4PIts importance to you Gralsritter is quite clear, \x01",
            "then.\x02\x03",

            "I'd assume there are similar ones in places other\x01",
            "than Liberl, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x109,
        (
            "#1075F#5PWell, I won't deny it.\x02\x03",

            "#1060FAnyway, we call this place a 'primal ground.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#1458F#6PNow, there's a deep name if I ever heard one.\x02\x03",

            "#1456FIs the original ground the others are based on\x01",
            "in Arteria?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        "#1064F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        "#1450F#6PI'll take that as a 'yes.'\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x109,
        (
            "#1066F#5POh, I'm not confirming anything.\x02\x03",

            "I was just thinking about how much you take\x01",
            "after the other Professor Russell, 's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "#1457F#6PUgh. I'll thank you not to associate me with him.\x02\x03",

            "#1456FHe might trump me a little in the theoretical side\x01",
            "of things, but when it comes to the practical\x01",
            "side of orbal science, I could beat him in my sleep.\x02\x03",

            "And I WAS the one who designed the fundamental\x01",
            "systems of the Capel AND the Arseille, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x109,
        (
            "#1060F#5PReally? Nice.\x02\x03",

            "#1064F...Buuut I think we're getting off topic here.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)

    def lambda_869():
        OP_6D(1480, -1000, 24030, 2000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_869)

    def lambda_881():
        OP_67(0, 5460, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_881)

    def lambda_899():
        OP_6B(3850, 2000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_899)

    def lambda_8A9():
        OP_6E(254, 2000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_8A9)
    WaitChrThread(0x10, 0x0)
    Sleep(800)

    def lambda_8C3():
        OP_6D(1840, -1000, 29250, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8C3)

    def lambda_8DB():
        OP_67(0, 4570, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8DB)

    def lambda_8F3():
        OP_6B(3790, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_8F3)

    def lambda_903():
        OP_6E(229, 4000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_903)

    def lambda_913():
        OP_8E(0xFE, 0xFFFFFF10, 0xFFFFFC18, 0x6914, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_913)
    Sleep(150)

    def lambda_933():
        OP_8E(0xFE, 0xFFFFFC04, 0xFFFFFC18, 0x6194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_933)
    Sleep(300)

    def lambda_953():
        OP_8E(0xFE, 0x1C2, 0xFFFFFC18, 0x6252, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_953)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(300)

    ChrTalk(    #12
        0x109,
        "#1063F#6PThis is the object in question, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x11,
        (
            "#703F#4PThat's correct.\x02\x03",

            "#700FIt was pulled up three days ago from the area \x01",
            "where the Liber Ark sank, and we believe it to \x01",
            "be an artifact.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_20(0xBB8)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0900   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_2_17E end

    def Function_3_A6D(): pass

    label("Function_3_A6D")

    EventBegin(0x0)
    ClearMapFlags(0x2000000)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x109, -240, -1000, 26900, 0)
    SetChrPos(0x11, 450, -1000, 25170, 0)
    SetChrPos(0x10, -1020, -1000, 24980, 0)
    OP_DB(0x0, 0xE)
    OP_DC(0x2, 0xFF)
    OP_DC(0x1, 0x0, 0x8)
    OP_DC(0x1, 0x0, 0xE)
    ClearParty()
    AddParty(0x8, 0xEE, 0xFF)
    AddParty(0xE, 0xEF, 0xFF)
    Call(6, 9)
    ClearChrFlags(0x10F, 0x80)
    SetChrPos(0x10F, 240, -1000, 15420, 0)
    OP_A2(0x25D5)
    OP_6D(1930, -1000, 30500, 0)
    OP_67(0, 4900, -10000, 0)
    OP_6B(4000, 0)
    OP_6B(3800, 0)
    OP_6C(45000, 0)
    OP_6E(229, 0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #14
        0x109,
        (
            "#1065F#6PI see...\x02\x03",

            "#1067FStill, looking at it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#1457F#6PCorrect.\x02\x03",

            "There were orbal readings coming from the\x01",
            "artifact when we found it, but not anymore.\x02\x03",

            "#1452FAnd I'm sure I don't need to spell out the\x01",
            "significance of that, do I?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C46():
        OP_6D(1200, -1000, 27440, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C46)

    def lambda_C5E():
        OP_67(0, 4650, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C5E)

    def lambda_C76():
        OP_6B(4000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C76)

    def lambda_C86():
        OP_6E(229, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_C86)
    OP_8C(0x109, 180, 400)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #16
        0x109,
        (
            "#1065F#5PNo, it's plain as day why you decided to stay\x01",
            "and wait for me now.\x02\x03",

            "#1060FIf an artifact has lost its power, it's exempt from\x01",
            "the traditional agreements governing them and\x01",
            "doesn't need to be given to the church. That it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "#1456F#6PHeehee. You already understand me so well.\x01",
            "We can cut right to the chase, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x11,
        (
            "#703F#4PThe orbal readings disappeared just before we\x01",
            "handed the artifact over to the cathedral, as it\x01",
            "so happens.\x02\x03",

            "It's currently being looked after here, but the\x01",
            "formal procedures to transfer ownership have yet \x01",
            "to be completed, making its legal owner unclear.\x02\x03",

            "#700FSo, in your expert opinion, what should be done\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x109,
        (
            "#1067F#5PHmm... This is a tricky one...\x02\x03",

            "#1063FI'm assuming Liberl wants to assert ownership\x01",
            "of it in this scenario, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        (
            "#701F#4PIf anything, it's the professor here who\x01",
            "wants to do that.\x02\x03",

            "I'm merely here accompanying her as a \x01",
            "representative of the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        (
            "#1450F#6PThe only reason it's not lying at the bottom of\x01",
            "Valleria Lake right now is because of ZCF's\x01",
            "salvage efforts.\x02\x03",

            "I'd say we have every right to keep it, personally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x109,
        (
            "#1065F#5PFrom what I've heard, it's completely impossible to\x01",
            "analyze an artifact that's no longer active.\x02\x03",

            "I don't see how it'd be of any use to your research\x01",
            "as things stand now...\x02\x03",

            "#1840F...but you're sure you want it that badly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "#1450F#6POh, absolutely.\x02\x03",

            "#1457FWe're talking about an object found at the site\x01",
            "of where a massive flying city used to be.\x02\x03",

            "I might not have seen it happen, but it sounds  \x01",
            "like everything we thought we knew about the \x01",
            "world was more or less proven wrong.\x02\x03",

            "#1452FYou know, by the truth that you people in the\x01",
            "church have kept hidden for the past...oh, I don't\x01",
            "know...thousand years.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #24
        0x109,
        "#1063F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#1453F#6PAs for that Ouroboros group, they don't\x01",
            "make much more sense than you guys.\x02\x03",

            "The more I hear about their advances in\x01",
            "technology, the less I can work out how\x01",
            "it's even possible.\x02\x03",

            "#1457FI don't know what the truth is or what's\x01",
            "really happening here in this land...\x02\x03",

            "...but I can't stand by and feign disinterest\x01",
            "in knowing the answers anymore--and I'm far\x01",
            "from alone.\x02\x03",

            "#1459FSo long as there's the slightest chance that\x01",
            "artifact could shed light on all of what I want\x01",
            "to know, I want it. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        "#1067F#5P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 400)
    Sleep(300)

    ChrTalk(    #27
        0x11,
        (
            "#701F#2PI think you've made your point, Professor.\x02\x03",

            "It's not as though interrogating him will\x01",
            "achieve anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        "#1457F#6P...True enough.\x02",
    )

    CloseMessageWindow()

    def lambda_163B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_163B)
    Sleep(400)

    ChrTalk(    #29
        0x10,
        (
            "#1450F#6PWell, you've heard what I've got to say.\x02\x03",

            "It's now up to you to tell us what you're\x01",
            "going to do.\x02\x03",

            "Will you hand over that lump of metal?\x01",
            "Or won't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        "#1067F#5P#40WWell...\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    NpcTalk(    #31
        0x10F,
        "Girl's Voice",
        (
            "#1P'That brief hesitation was all it took to\x01",
            "spawn a great evil.'\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_17BA():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_17BA)
    Sleep(100)
    OP_8C(0x11, 180, 400)
    OP_1D(0xB7)
    Fade(1000)
    OP_6D(0, -1000, 223790, 0)
    OP_67(0, 5270, -10000, 0)
    OP_6B(2910, 0)
    OP_6C(180000, 0)
    OP_6E(294, 0)
    SetChrPos(0x10F, 0, -1000, 212020, 0)
    SetChrChipByIndex(0x10F, 2)
    SetChrSubChip(0x10F, 0)
    SetChrPos(0x109, -90, -1000, 227080, 180)
    SetChrPos(0x11, 610, -1000, 225560, 180)
    SetChrPos(0x10, -760, -1000, 225640, 180)

    def lambda_1866():
        OP_6D(0, -1000, 211000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1866)

    def lambda_187E():
        OP_67(0, 3600, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_187E)

    def lambda_1896():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1896)

    def lambda_18A6():
        OP_6E(294, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_18A6)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #32
        0x11,
        "#702F#5P...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        "#1454F#5PWho is she?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x109,
        "#1079F#5P(No...way...)\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #35
        0x10F,
        "Sister",
        (
            "#1446F#5P'It crawled through the fields, ran through the \x01",
            "hills, and spread disaster in the skies above.'\x02\x03",

            "An excerpt from the Book of Ezer, Verse 2,\x01",
            "'Disaster Unleashed.'\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 0x0)
    Sleep(200)
    SetChrSubChip(0x10F, 1)
    Sleep(200)
    SetChrSubChip(0x10F, 2)
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_6D(1650, -1000, 210300, 0)
    OP_67(0, 4080, -10000, 0)
    OP_6B(3020, 0)
    OP_6C(134000, 0)
    OP_6E(299, 0)

    def lambda_1A41():
        OP_8E(0xFE, 0xFFFFFFE2, 0xFFFFFC18, 0x3645C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1A41)

    def lambda_1A5C():
        OP_6D(1430, -1000, 222830, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1A5C)

    def lambda_1A74():
        OP_67(0, 4350, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1A74)

    def lambda_1A8C():
        OP_6B(2700, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1A8C)

    def lambda_1A9C():
        OP_6E(320, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1A9C)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    NpcTalk(    #36
        0x10F,
        "Sister",
        (
            "#1440F#11PI apologize for the delay in coming,\x01",
            "Father Graham.\x02\x03",

            "My name is Ries Argent, and I am a\x01",
            "squire of the Gralsritter.\x02\x03",

            "I look forward to working under you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x109,
        "#1064F#5P#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        (
            "#1452F#6PI didn't think we'd end up having more company.\x02\x03",

            "#1454FWait a second.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #39
        0x10F,
        "#1444F#11P...Is something the matter?\x02",
    )

    CloseMessageWindow()
    OP_9E(0x10, 0xF, 0x0, 0x12C, 0xBB8)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #40
        0x10,
        (
            "#1830F#6PSo that's how they think they can get me,\x01",
            "is it?!\x02\x03",

            "But they can't just bribe me so easily!\x01",
            "I'm better than that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10F,
        "#1802F#11P...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10,
        (
            "#1457F#6PM-Maybe I underestimated the Gralsritter...\x02\x03",

            "They think they can break my will to fight by\x01",
            "sending a girl like you my way, do they?\x02\x03",

            "#1834FBut I'm not going to go down so easily, because\x01",
            "I've got a secret weapon of my own!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #43
        0x10,
        (
            "#1455F#6P#4SBehold!\x01",
            "The most powerful force in the universe!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_22(0x8F, 0x0, 0x64)
    OP_AD(0x240102, 0x96, 0x78, 0x1F4)
    Sleep(1500)
    OP_8C(0x11, 270, 400)
    SetMessageWindowPos(100, 60, -1, -1)
    SetChrName("Lieutenant Colonel Cid")

    AnonymousTalk(    #44
        "\x07\x00#702FIsn't that...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(70, 300, -1, -1)
    SetChrName("Father Kevin")

    AnonymousTalk(    #45
        "\x07\x00#1064FThat's Tita isn't it...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 50, -1, -1)
    SetChrName("Sister Ries")

    AnonymousTalk(    #46
        "\x07\x00#1442F...How cute.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #47
        0x10,
        (
            "#1834F#6PIsn't she?! ISN'T SHE?!\x02\x03",

            "#1831FI bet you just want to jump into this photo and \x01",
            "squeeze her like a stuffed toy right now, don't\x01",
            "you?!\x02\x03",

            "I should've known a cutie-patootie like you would\x01",
            "be able to appreciate the same qualities in others!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1500)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x10, 90, 600)
    Sleep(400)
    OP_8C(0x10, 0, 600)
    Sleep(400)
    OP_8C(0x10, 90, 600)
    OP_8C(0x10, 180, 600)
    OP_63(0x109)
    OP_63(0x10F)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #48
        0x10,
        (
            "#1457F#6P*cough* A-Anyway!\x02\x03",

            "#1452FThat's why no matter how frickin' adorable\x01",
            "you may happen to be, you can't take ME\x01",
            "down, because I've got a natural immunity!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10F,
        (
            "#1802F#11PUmm... I beg your pardon, but I'm afraid\x01",
            "I'm not really following.\x02\x03",

            "You keep saying that someone is cute, but...\x01",
            "are you referring to me?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #50
        0x10,
        "#1451F#6P#4SWho else would I be talking about?!#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #51
        0x10,
        (
            "#1831F#6PYou've got such an aura of maturity about you,\x01",
            "and yet your features still have that irresistible\x01",
            "trace of innocence to them.\x02\x03",

            "And then they throw you into a sister's habit to\x01",
            "complement it all like a little cherry on top!\x01",
            "That's the most flattering habit I've ever SEEN!\x02\x03",

            "Ugh... If I didn't have my protective field, I'd be\x01",
            "in real danger here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10F,
        "#1805F#11P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #53
        0x10,
        (
            "#1836F#6PWh-Why are you looking at me like that?! \x01",
            "I-I'm just saying!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10F,
        (
            "#1446F#11P...Might I inquire as to the identities of the\x01",
            "people with you, Father Graham?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2471():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2471)
    Sleep(100)

    ChrTalk(    #55
        0x109,
        (
            "#1064F#6PS-Sure...\x02\x03",

            "#1065FThe lady's Professor Erika Russell of ZCF, while\x01",
            "the gentleman is Lieutenant Colonel Cid of the\x01",
            "Royal Army.\x02\x03",

            "#1063FSeriously, though. 'Father Graham'? Really?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10F,
        (
            "#1440F#11PAh, so you're the people who initially discovered\x01",
            "the artifact, then?\x02\x03",

            "#1446FThank you for your cooperation in our work.\x01",
            "We will take over looking after it from here on\x01",
            "out.\x02\x03",

            "That will be all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        "#1454F#6PWait a...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x11,
        "#702F#5P...What?\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #59
        0x109,
        (
            "#1064F#6PH-Hold on a minute! We hadn't finished deciding\x01",
            "what to do with it yet! \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10F,
        (
            "#1446F#11PPerhaps not, but my intention was to save you\x01",
            "the time and effort required to do so by making\x01",
            "the correct judgment myself.\x02\x03",

            "#1443FWhether it has lost its power or not, that is no\x01",
            "ordinary artifact. It is potentially related to one\x01",
            "of the Sept-Terrions.\x02\x03",

            "I'm surprised that you even humored the option\x01",
            "of letting an outsider take custody of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x109,
        "#1063F#6PI-I mean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        (
            "#1458F#6PWell, well. You sure know how to pick a fight.\x02\x03",

            "#1456FGo on, then. What legal basis do you have for\x01",
            "taking it from us? \x02\x03",

            "The agreements with the church quite clearly\x01",
            "say that artifacts that have lost their power\x01",
            "are exempt from the usual rules.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10F,
        (
            "#1447F#11PI have no legal basis, but you have no more of\x01",
            "one for keeping it.\x02\x03",

            "#1448FIf we are following the agreements to the letter, \x01",
            "no one is allowed to assert ownership of inactive\x01",
            "artifacts.\x02\x03",

            "It belongs to neither you nor me; it is simply an\x01",
            "abandoned object with no owner whatsoever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10,
        (
            "#1459F#6PWhat? So all you got is, 'I don't need a reason!\x01",
            "It's mine and that's final'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10F,
        "#1446F#11PTo put it bluntly, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        "#1457F#6PHmph. Well, if that's how you want to play it...\x02",
    )

    CloseMessageWindow()

    def lambda_2B1B():
        OP_6D(1430, -1000, 223800, 800)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2B1B)

    def lambda_2B33():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2B33)
    Sleep(100)
    OP_8C(0x11, 315, 400)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #67
        0x10,
        "#1455F#11PWhat's YOUR take on this, Kevin Graham?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x10F,
        "#1443F#11PWell? By all means.\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #69
        0x109,
        (
            "#1064F#6PM-Me?! I thought I'd been kicked out of this\x01",
            "conversation!\x02\x03",

            "#1068F...But, well, I can't say I don't want to take it\x01",
            "back to Arteria with us.\x02\x03",

            "#1066FBut after all the help Liberl's given us, I'd feel\x01",
            "kinda bad just snatching it from them without\x01",
            "even giving them a valid reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x11,
        (
            "#703F#5PHmm... Both arguments have a degree of merit,\x01",
            "but neither is clearly more correct.\x02\x03",

            "#701FI'm not quite sure how you'll solve this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x109,
        (
            "#1068F#6PYou, uh, DO know that you're smack dab\x01",
            "in the middle of this, too, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x0)
    OP_22(0x15F, 0x0, 0x64)
    OP_C4(0x0, 0x400)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #72
        0x109,
        "#1064F#6PWhoa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10F,
        "#1444F#11PMy...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_C4(0x1, 0x400)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10, 180, 400)

    ChrTalk(    #74
        0x11,
        "#702F#5PWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10,
        "#1452F#6PWhy do you both look so surprised?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x109,
        "#1067F#6PWhat do you mean, 'Why'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10F,
        "#1443F#11PDid the two of you not hear that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x10,
        "#1459F#6PHear what?\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10, 0, 400)
    Sleep(300)

    ChrTalk(    #79
        0x10,
        "#1454F#11PWait a...\x02",
    )

    CloseMessageWindow()

    def lambda_2F9C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2F9C)
    Sleep(100)
    OP_8C(0x11, 0, 400)

    ChrTalk(    #80
        0x10F,
        "#1444F#11POh...\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0xB8)
    LoadEffect(0x0, "map\\mp256_00.eff")
    LoadEffect(0x1, "map\\mp252_01.eff")
    LoadEffect(0x2, "map\\mp256_01.eff")
    OP_22(0x146, 0x1, 0x32)
    PlayEffect(0x2, 0x0, 0xFF, 0, 400, 230000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x1, 0xFF, 0, 400, 30000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_E5(0x0, 0xA, 0x0, 262144)
    OP_E5(0x0, 0xA, 0x1, 262144)
    OP_E5(0x0, 0xA, 0x2, 262144)
    OP_E5(0x0, 0xA, 0x3, 262144)
    OP_E5(0x0, 0xA, 0x4, 262144)
    OP_E5(0x0, 0xA, 0x5, 262144)
    OP_E5(0x0, 0xA, 0x6, 262144)
    OP_E5(0x0, 0xA, 0x7, 262144)
    OP_E5(0x0, 0xA, 0x8, 262144)
    OP_E5(0x0, 0xA, 0x9, 262144)
    OP_E5(0x0, 0xA, 0xA, 262144)
    OP_E5(0x0, 0xB, 0x0, 262144)
    OP_E5(0x0, 0xB, 0x1, 262144)
    OP_E5(0x0, 0xB, 0x2, 262144)
    OP_E5(0x0, 0xB, 0x3, 262144)
    OP_E5(0x0, 0xB, 0x4, 262144)
    OP_E5(0x0, 0xB, 0x5, 262144)
    OP_E5(0x0, 0xB, 0x6, 262144)
    OP_E5(0x0, 0xB, 0x7, 262144)
    OP_E5(0x0, 0xB, 0x8, 262144)
    OP_E5(0x0, 0xB, 0x9, 262144)
    OP_E5(0x0, 0xB, 0xA, 262144)
    OP_E5(0x2, 0xA, 0x0, 700)
    OP_E5(0x2, 0xA, 0x1, 700)
    OP_E5(0x2, 0xA, 0x2, 700)
    OP_E5(0x2, 0xA, 0x3, 700)
    OP_E5(0x2, 0xA, 0x4, 700)
    OP_E5(0x2, 0xA, 0x5, 700)
    OP_E5(0x2, 0xA, 0x6, 700)
    OP_E5(0x2, 0xA, 0x7, 700)
    OP_E5(0x2, 0xA, 0x8, 700)
    OP_E5(0x2, 0xA, 0xA, 700)
    OP_E5(0x2, 0xB, 0x0, 700)
    OP_E5(0x2, 0xB, 0x1, 700)
    OP_E5(0x2, 0xB, 0x2, 700)
    OP_E5(0x2, 0xB, 0x3, 700)
    OP_E5(0x2, 0xB, 0x4, 700)
    OP_E5(0x2, 0xB, 0x5, 700)
    OP_E5(0x2, 0xB, 0x6, 700)
    OP_E5(0x2, 0xB, 0x7, 700)
    OP_E5(0x2, 0xB, 0x8, 700)
    OP_E5(0x2, 0xB, 0xA, 700)
    Sleep(1000)
    Fade(1000)
    OP_6D(-130, -1000, 30000, 0)
    OP_67(0, 3500, -10000, 0)
    OP_6B(3870, 0)
    OP_6C(0, 0)
    OP_6E(208, 0)
    SetChrPos(0x109, -60, -1000, 25760, 0)
    SetChrPos(0x11, 670, -1000, 24300, 0)
    SetChrPos(0x10, -780, -1000, 23650, 0)
    SetChrPos(0x10F, -60, -1000, 20930, 0)

    def lambda_3251():
        OP_6D(0, -1650, 32000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3251)

    def lambda_3269():
        OP_67(0, 7700, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3269)

    def lambda_3281():
        OP_6B(3080, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3281)

    def lambda_3291():
        OP_6E(176, 8000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3291)
    Sleep(500)
    OP_B0(0xA, 0xF)
    OP_B0(0xB, 0xF)
    OP_6F(0xA, 1)
    OP_70(0xA, 0x69)
    OP_6F(0xB, 1)
    OP_70(0xB, 0x69)
    WaitChrThread(0x109, 0x0)
    OP_73(0xA)
    OP_73(0xB)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x4)
    Sleep(1000)
    OP_B0(0xA, 0xF)
    OP_B0(0xB, 0xF)
    OP_6F(0xA, 105)
    OP_70(0xA, 0xB4)
    OP_6F(0xB, 105)
    OP_70(0xB, 0xB4)

    def lambda_330B():
        OP_6D(0, -1050, 34120, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_330B)

    def lambda_3323():
        OP_67(0, 4700, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3323)

    def lambda_333B():
        OP_6B(2350, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_333B)
    OP_73(0xA)
    OP_73(0xB)
    OP_71(0x200A, 0x0)
    ExitThread()
    OP_71(0x200B, 0x0)
    ExitThread()
    OP_6F(0xA, 181)
    OP_70(0xA, 0x12C)
    OP_6F(0xB, 181)
    OP_70(0xB, 0x12C)
    Sleep(300)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 0, 1000, 230000, 30)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 0, 1000, 30000, 30)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(300)
    OP_22(0xC9, 0x0, 0x64)
    PlayEffect(0x1, 0x2, 0x12, 0, 0, 0, 30, 30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0x13, 0, 0, 0, 30, 30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)

    ChrTalk(    #81
        0x11,
        "#702F#5PWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10,
        (
            "#1455F#5POh, no WAY...\x02\x03",

            "That thing wasn't giving off any orbal readings\x01",
            "at all anymore! Zero! Zip!\x02\x03",

            "Why's it suddenly active again?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x10F,
        (
            "#1443F#5P...\x02\x03",

            "#1446FI believe that settles our dispute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x109,
        "#1065F#5PIt sure does.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-2130, -1000, 28840, 0)
    OP_67(0, 4570, -10000, 0)
    OP_6B(3780, 0)
    OP_6C(315000, 0)
    OP_6E(225, 0)
    OP_0D()

    def lambda_3582():
        OP_6D(-2050, -1000, 31170, 2000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_3582)

    def lambda_359A():
        OP_8E(0xFE, 0x0, 0xFFFFFC18, 0x6DBA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_359A)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    ChrTalk(    #85
        0x109,
        (
            "#1063F#6PSo the real artifact was inside, huh?\x02\x03",

            "I've never seen one quite like it.\x02\x03",

            "It looks like a box of some kind. Or a cube,\x01",
            "maybe.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_72(0x200A, 0x0)
    ExitThread()
    OP_72(0x200B, 0x0)
    ExitThread()
    OP_6F(0xA, 301)
    OP_70(0xA, 0x12D)
    OP_6F(0xB, 301)
    OP_70(0xB, 0x12D)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_22(0x8F, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x109, 270, 1250, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x109, 3)
    SetChrSubChip(0x109, 0)
    SetChrFlags(0x109, 0x20)

    def lambda_36D2():
        OP_6D(-1950, -1000, 30670, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_36D2)
    OP_0D()
    Sleep(1500)
    FadeToDark(300, 0, 100)
    OP_AD(0x240105, 0xBE, 0x82, 0x1F4)
    Sleep(1500)
    OP_56(0x2)
    OP_AE(0x1F4)
    FadeToBright(300, 0)
    Sleep(1000)
    Sleep(1000)
    Fade(1000)
    OP_82(0x1, 0x2)
    OP_23(0xC9)
    OP_E5(0x2, 0xA, 0x0, 0)
    OP_E5(0x2, 0xA, 0x1, 0)
    OP_E5(0x2, 0xA, 0x2, 0)
    OP_E5(0x2, 0xA, 0x3, 0)
    OP_E5(0x2, 0xA, 0x4, 0)
    OP_E5(0x2, 0xA, 0x5, 0)
    OP_E5(0x2, 0xA, 0x6, 0)
    OP_E5(0x2, 0xA, 0x7, 0)
    OP_E5(0x2, 0xA, 0x8, 0)
    OP_E5(0x2, 0xA, 0xA, 0)
    OP_E5(0x2, 0xB, 0x0, 0)
    OP_E5(0x2, 0xB, 0x1, 0)
    OP_E5(0x2, 0xB, 0x2, 0)
    OP_E5(0x2, 0xB, 0x3, 0)
    OP_E5(0x2, 0xB, 0x4, 0)
    OP_E5(0x2, 0xB, 0x5, 0)
    OP_E5(0x2, 0xB, 0x6, 0)
    OP_E5(0x2, 0xB, 0x7, 0)
    OP_E5(0x2, 0xB, 0x8, 0)
    OP_E5(0x2, 0xB, 0xA, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #86
        0x10,
        "#1454F#5POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x109,
        "#1065F#5P...\x02",
    )

    CloseMessageWindow()

    def lambda_37FD():
        OP_6D(-2050, -1000, 28810, 1000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_37FD)
    OP_8C(0x109, 180, 400)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    ChrTalk(    #88
        0x109,
        (
            "#1075F#11PI'd like to thank you two for your cooperation\x01",
            "in the recovery of this artifact.\x02\x03",

            "In accordance with the pacts of the church,\x01",
            "I, Kevin Graham, will be assuming custody of\x01",
            "it from here on out.\x02\x03",

            "#1060FYou, and all who aided you, have the Septian \x01",
            "Church's deepest appreciation.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3949():
        OP_6B(4200, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3949)
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    OP_3E(0x328, 1)
    OP_44(0x109, 0x0)
    OP_A2(0x2505)
    Sleep(3000)
    NewScene("ED6_DT21/T4152   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_3_A6D end

    def Function_4_3981(): pass

    label("Function_4_3981")

    OP_24(0x146, 0x28)
    Sleep(200)
    OP_24(0x146, 0x1E)
    Sleep(200)
    OP_24(0x146, 0x14)
    Sleep(200)
    OP_24(0x146, 0xA)
    Sleep(200)
    OP_24(0x146, 0x0)
    OP_23(0x146)
    Return()

    # Function_4_3981 end

    SaveToFile()

Try(main)
