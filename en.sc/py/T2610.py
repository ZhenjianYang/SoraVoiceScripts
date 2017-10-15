from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2610   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2610.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60032",
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
        'Gilbert',                              # 9
        'Richelle',                             # 10
        'Campanella',                           # 11
        'Sieg',                                 # 12
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -80200,
        TriggerZ            = 250,
        TriggerY            = 31450,
        TriggerRange        = 1000,
        ActorX              = -80240,
        ActorZ              = 250,
        ActorY              = 32100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_14E",          # 00, 0
        "Function_1_173",          # 01, 1
        "Function_2_1DA",          # 02, 2
        "Function_3_358",          # 03, 3
        "Function_4_361",          # 04, 4
        "Function_5_19C7",         # 05, 5
        "Function_6_2D9F",         # 06, 6
        "Function_7_2DDC",         # 07, 7
        "Function_8_2E5D",         # 08, 8
        "Function_9_2EA5",         # 09, 9
        "Function_10_2EED",        # 0A, 10
        "Function_11_2F35",        # 0B, 11
        "Function_12_2F7D",        # 0C, 12
        "Function_13_2FD5",        # 0D, 13
        "Function_14_301E",        # 0E, 14
        "Function_15_307E",        # 0F, 15
        "Function_16_30FC",        # 10, 16
        "Function_17_3112",        # 11, 17
        "Function_18_315A",        # 12, 18
    )


    def Function_0_14E(): pass

    label("Function_0_14E")

    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_172")
    Event(0, 3)
    Jump("loc_172")

    label("loc_172")

    Return()

    # Function_0_14E end

    def Function_1_173(): pass

    label("Function_1_173")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 1)), scpexpr(EXPR_END)), "loc_183")
    OP_10(0x5, 0x0)
    OP_10(0x17, 0x1)
    Jump("loc_189")

    label("loc_183")

    OP_10(0x5, 0x1)
    OP_10(0x17, 0x0)

    label("loc_189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x268, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B")
    OP_6F(0xB, 0)
    Jump("loc_1A2")

    label("loc_19B")

    OP_6F(0xB, 60)

    label("loc_1A2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0xF40), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BA")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D9")

    label("loc_1BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1C4")
    Jump("loc_1D9")

    label("loc_1C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_1D9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_1D9")

    Return()

    # Function_1_173 end

    def Function_2_1DA(): pass

    label("Function_2_1DA")

    OP_EA(0x2, 0xFE, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x268, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_24B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xF5\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1341)
    Jump("loc_2AF")

    label("loc_24B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xF5\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF5\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_2AF")

    Jump("loc_34A")

    label("loc_2B2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05No matter where you go or what events you\x01",
            "witness, you can rest easy knowing that this\x01",
            "chest will always be here for you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_34A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1DA end

    def Function_3_358(): pass

    label("Function_3_358")

    Call(0, 4)
    Call(0, 5)
    Return()

    # Function_3_358 end

    def Function_4_361(): pass

    label("Function_4_361")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    OP_D2(0x2601B4, 0x2601B9, 0x0)
    OP_D2(0x260068, 0x26006D, 0x1)
    OP_D2(0x704AA, 0x704AE, 0x2)
    OP_D2(0x2601BA, 0x2601BF, 0x3)
    OP_D2(0x70113, 0x70117, 0x4)
    OP_D2(0x2701DA, 0x2701DF, 0x5)
    OP_D2(0x70180, 0x70184, 0x6)
    OP_D2(0x270110, 0x270120, 0x7)
    OP_D2(0x270111, 0x270121, 0x8)
    OP_D2(0x270130, 0x270140, 0x9)
    OP_D2(0x270131, 0x270141, 0xA)
    OP_D2(0x70326, 0x7032D, 0xB)
    OP_D2(0x70327, 0x7032E, 0xC)
    OP_D2(0x70318, 0x7031F, 0xD)
    OP_D2(0x70319, 0x70320, 0xE)
    OP_D2(0x2701F8, 0x2701FD, 0xF)
    SetChrChipByIndex(0x8, 0)
    SetChrChipByIndex(0x9, 4)
    SetChrChipByIndex(0xA, 5)
    SetChrChipByIndex(0xB, 6)
    OP_6D(510, 0, 2770, 0)
    OP_67(0, 6890, -10000, 0)
    OP_6B(2450, 0)
    OP_6C(45000, 0)
    OP_6E(311, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x101, 0x1, 0x0, 0x8)
    Sleep(80)
    OP_43(0x102, 0x1, 0x0, 0x9)
    Sleep(200)
    OP_43(0x10A, 0x1, 0x0, 0xA)
    Sleep(70)
    OP_43(0x10E, 0x1, 0x0, 0xB)
    OP_6D(520, 0, 6900, 1500)
    SetChrPos(0x8, 30, 0, 16059, 180)

    NpcTalk(    #3
        0x8,
        "Man's Voice",
        "#4PExactly who I thought it was.\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x8, -190, 2000, 25350, 180)
    SetChrPos(0x9, 360, 2000, 25240, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_6D(-50, 2000, 24730, 2500)
    OP_1D(0x29)
    Sleep(1000)
    SetChrChipByIndex(0x101, 7)
    SetChrChipByIndex(0x102, 9)
    SetChrChipByIndex(0x10A, 11)
    SetChrChipByIndex(0x10E, 13)

    def lambda_5D8():
        OP_6D(50, 1800, 20880, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D8)

    def lambda_5F0():
        OP_67(0, 3650, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5F0)

    def lambda_608():
        OP_6B(2550, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_608)

    def lambda_618():
        OP_6E(405, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_618)

    def lambda_628():
        OP_8E(0xFE, 0xFFFFFDF8, 0xFFFFFFCE, 0x47AE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_628)
    Sleep(80)

    def lambda_648():
        OP_8E(0xFE, 0x3A2, 0xFFFFFFCE, 0x4736, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_648)
    Sleep(70)

    def lambda_668():
        OP_8E(0xFE, 0xFFFFFBE6, 0x0, 0x40CE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_668)
    Sleep(80)

    def lambda_688():
        OP_8E(0xFE, 0x24E, 0x0, 0x4042, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_688)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x10E, 0x1)

    ChrTalk(    #4
        0x101,
        "#1005F#2PGilbert!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#1221FThat's close enough, everyone.\x02\x03",

            "Unless you'd like to see this\x01",
            "young lady get hurt.\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x9, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #6
        0x9,
        "#7PN-No...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1020F#2P(Oh, no! Isn't that Kloe's friend?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        "#1042F#2P(The Fencing Club member, yes...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#1222FYou damnable wretches seem obsessed\x01",
            "with getting in my way...\x02\x03",

            "#1225FThis time, I WILL come out ahead!\x02\x03",

            "I will climb the ranks of Ouroboros\x01",
            "with this girl as my ladder!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#1004F#2PWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "#1226FThe Society of Ouroboros is far\x01",
            "larger than I'd ever imagined.\x02\x03",

            "Everything happening here in Liberl\x01",
            "is but the tip of the iceberg...\x02\x03",

            "Our plans extend across the continent,\x01",
            "across the centuries, across everything!\x02\x03",

            "#1221FHeh heh. It is the perfect path to\x01",
            "power. And the girl is all I need.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10A,
        "#814F#2PSo that's your plan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#1007F#2PSo you screw up in Liberl and decide to go down\x01",
            "the criminal organization's drain instead. Got'cha.\x01",
            "Great career 'advancement' there, champ.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#1225FSilence!\x02\x03",

            "A tiny little backwater like Liberl\x01",
            "was always too small for me!\x02\x03",

            "#1226FThe society, in all its glory,\x01",
            "meanwhile, is a fitting stage\x01",
            "for me to stand on!\x02\x03",

            "#1221FAnd you will not get in my way!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1007F#2PWell, I'd like to say 'good\x01",
            "luck with that'...\x02\x03",

            "#1019FBut you realize that girl won't\x01",
            "get you anywhere, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "#1226FHeh, poor, ignorant fool.\x02\x03",

            "#1221FThis girl is, in fact, the princess\x01",
            "of the von Auslese family in hiding!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #17
        0x9,
        (
            "#7PNO! I'm telling you,\x01",
            "IT ISN'T ME!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#1221FPlease.\x01",
            "The charade fools no one at this point.\x02\x03",

            "#1226FWitnesses say Klaudia von Auslese favors\x01",
            "rapiers in combat.\x02\x03",

            "And, right now, you are the only\x01",
            "female student in the Fencing Club.\x02\x03",

            "#1225FIt cannot be anyone but you!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    OP_63(0x102)
    OP_63(0x9)
    Sleep(500)

    ChrTalk(    #19
        0x9,
        "#7PBut, but, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1019F#2PY'know, it's sad.\x01",
            "I dunno how to break it to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        (
            "#1035F#2PHe's like a monument to\x01",
            "boneheaded assumptions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "#1224FWhat are you talking about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1007F#2POoookay, then.\x01",
            "From the top...\x02\x03",

            "#1019FYou wouldn't happen to remember when you\x01",
            "got captured at the lighthouse, would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#1225FHow could I ever forget?!\x02\x03",

            "Just remembering it makes my guts boil\x01",
            "with rage! The humiliation! The indignity!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        (
            "#1048F#2PThen you do remember the girl\x01",
            "who was accompanying us, right?\x02\x03",

            "It seemed like you knew her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#1221FYes, I remember her.\x01",
            "Kloe Rinz, as I recall.\x02\x03",

            "That's a good point, I didn't see her\x01",
            "among the captured...students...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x8)
    Sleep(500)

    ChrTalk(    #27
        0x8,
        "#1224F#3SWHAT?\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1006F#2PBiiiingo!\x02\x03",

            "Remember how Kloe used a fencing\x01",
            "sword at the lighthouse?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#1224FNow that you...\x02\x03",

            "#1225FNo... NO!\x01",
            "That bleeding heart orphan lover?!\x01",
            "That's ridiculous! ABSURD!\x02\x03",

            "Everything I've done can't have\x01",
            "been a waste...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10A,
        (
            "#819F#2PAnd now he's fleeing from reality.\x01",
            "That's not healthy, dude!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10E,
        "#843F#2P...Tragic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "#1227FS-SILENCE!!!\x02\x03",

            "#1225FYes, I have a hostage here regardless!\x01",
            "I still have the advantage!\x02\x03",

            "If you don't want to see her guts\x01",
            "covering the floor, throw down\x01",
            "your weapons!\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x9, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #33
        0x9,
        "#7PAaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1019F#2P(His face becomes more\x01",
            "kickable by the second.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        "#1043F#2P(We need some kind of opening.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "#1221FHah! Paralyzed with indecision, are we?\x02\x03",

            "Perhaps slicing open her face just\x01",
            "a little will make you pay atten--\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x1, "scraft\\\\sc000_11.eff")
    OP_22(0x197, 0x0, 0x64)
    OP_20(0x7D0)
    OP_22(0x8C, 0x0, 0x64)
    SetChrPos(0xB, -410, 5000, 5000, 0)
    SetChrFlags(0xB, 0x40)
    OP_7D(0x0, 0xB, 0x32, 0x1F4)
    ClearChrFlags(0xB, 0x80)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_22(0x8C, 0x0, 0x64)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 6)
    OP_43(0xB, 0x1, 0x0, 0x10)

    def lambda_145B():
        OP_6D(90, 3500, 13500, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_145B)

    def lambda_1473():
        OP_6E(343, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1473)
    WaitChrThread(0x101, 0x2)
    OP_1D(0x2C)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1493():
        OP_6D(430, 2000, 25000, 800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1493)

    def lambda_14AB():
        OP_6B(2300, 800)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_14AB)
    OP_8F(0xB, 0xC8, 0x960, 0x6270, 0x6590, 0x0)
    OP_7D(0x1, 0xB, 0x0, 0x0)
    PlayEffect(0x1, 0x0, 0x8, 0, 1600, 700, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)

    ChrTalk(    #37 op#A op#5
        0x8,
        "#1227F#20AGYAK!\x05\x02",
    )


    ChrTalk(    #38 op#A op#5
        0x9,
        "#4P#20AUwaaah!\x05\x02",
    )

    OP_44(0x101, 0x0)
    OP_44(0x102, 0x2)
    OP_44(0x10A, 0x2)
    OP_44(0x10E, 0x2)
    OP_8C(0x101, 0, 0)
    OP_8C(0x102, 0, 0)
    OP_8C(0x10A, 0, 0)
    OP_8C(0x10E, 0, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_8C(0x9, 0, 0)
    SetChrChipByIndex(0xB, 1)
    OP_44(0xB, 0x1)

    def lambda_1590():

        label("loc_1590")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_1590")

    QueueWorkItem2(0xB, 1, lambda_1590)

    def lambda_15A3():
        OP_8F(0xB, 0x1F4, 0x15E0, 0x6C98, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_15A3)

    def lambda_15BE():
        OP_8C(0xFE, 225, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_15BE)

    def lambda_15CC():
        OP_8F(0xFE, 0x3C0, 0x7D0, 0x6040, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_15CC)
    OP_43(0x8, 0x0, 0x0, 0xD)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_165E():
        OP_8C(0xFE, 225, 300)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_165E)

    def lambda_166C():
        OP_67(0, 3490, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_166C)

    def lambda_1684():
        OP_6B(2610, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1684)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x9, 0x2)

    ChrTalk(    #39
        0x101,
        "#1005F#2PRichelle! Over here!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)

    ChrTalk(    #40
        0x9,
        "#6PO-Okay!\x02",
    )

    CloseMessageWindow()

    def lambda_16DD():
        OP_6D(-340, 2000, 22200, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_16DD)

    def lambda_16F5():
        OP_67(0, 5880, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_16F5)

    def lambda_170D():
        OP_6B(2640, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_170D)

    def lambda_171D():
        OP_6E(360, 1500)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_171D)
    OP_22(0x8C, 0x0, 0x64)
    OP_43(0xB, 0x2, 0x0, 0xE)
    OP_43(0x9, 0x1, 0x0, 0xC)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #41
        0xB,
        "#310F#6PScreeee!\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x12C, 1500, 0x28, 0x2B, 0xC8, 0x0)
    Sleep(200)
    SetChrSubChip(0x8, 1)
    Sleep(1000)
    OP_63(0x8)

    ChrTalk(    #42
        0x8,
        "#1224F#8PWha-Wha-Wha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1018F#2PSieg! What are you doing here?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        "#1044F#2PKloe sent you, didn't she?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xB,
        "#311F#6PScree! ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10E,
        "#841F#2PHaha. How thoughtful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10A,
        "#811FThat is the COOLEST BIRD!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#1224F#8PNo, no, this can't be...\x02\x03",

            "#1227FTHIS IS MADNESS!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        (
            "#1035F#2PMadness? Perhaps it is.\x01",
            "Either way...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#1028F#2PTime for ul-tra-vi-o-lence. ♪\x02",
    )

    CloseMessageWindow()

    def lambda_18F7():
        OP_6D(370, 2000, 24910, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18F7)

    def lambda_190F():
        OP_6B(2000, 600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_190F)

    def lambda_191F():
        OP_8F(0xFE, 0xFFFFFDBC, 0x6D6, 0x640A, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_191F)
    Sleep(30)

    def lambda_193F():
        OP_8F(0xFE, 0x2A8, 0x6D6, 0x63D8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_193F)

    def lambda_195A():
        OP_8F(0xFE, 0xFFFFFDB2, 0x2EE, 0x646E, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_195A)
    Sleep(30)

    def lambda_197A():
        OP_8F(0xFE, 0x348, 0x2EE, 0x643C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_197A)
    WaitChrThread(0x101, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0x10E, 0xFF)
    OP_44(0x9, 0xFF)
    Battle(0xF40, 0x30000E, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_19C1"),
        (SWITCH_DEFAULT, "loc_19C6"),
    )


    label("loc_19C1")

    OP_B4(0x0)
    Jump("loc_19C6")

    label("loc_19C6")

    Return()

    # Function_4_361 end

    def Function_5_19C7(): pass

    label("Function_5_19C7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x10A, 0x1)
    OP_44(0x10E, 0x1)
    OP_D2(0x2601B4, 0x2601B9, 0x0)
    OP_D2(0x260068, 0x26006D, 0x1)
    OP_D2(0x704AA, 0x704AE, 0x2)
    OP_D2(0x2601BA, 0x2601BF, 0x3)
    OP_D2(0x70113, 0x70117, 0x4)
    OP_D2(0x2701DA, 0x2701DF, 0x5)
    OP_D2(0x70180, 0x70184, 0x6)
    OP_D2(0x270110, 0x270120, 0x7)
    OP_D2(0x270111, 0x270121, 0x8)
    OP_D2(0x270130, 0x270140, 0x9)
    OP_D2(0x270131, 0x270141, 0xA)
    OP_D2(0x70326, 0x7032D, 0xB)
    OP_D2(0x70327, 0x7032E, 0xC)
    OP_D2(0x70318, 0x7031F, 0xD)
    OP_D2(0x70319, 0x70320, 0xE)
    OP_D2(0x26021E, 0x260223, 0x10)
    OP_D2(0x26021F, 0x260224, 0x11)
    OP_D2(0x2600C1, 0x2600C6, 0x12)
    OP_D2(0x2600D2, 0x2600D7, 0x13)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x101, -680, 1000, 22880, 0)
    SetChrPos(0x102, 620, 1000, 22880, 0)
    SetChrPos(0x10A, -750, 0, 21730, 0)
    SetChrPos(0x10E, 650, 0, 21730, 0)
    SetChrPos(0x8, 240, 2000, 27150, 180)
    SetChrPos(0x9, 130, 0, 16730, 0)
    SetChrChipByIndex(0x101, 7)
    SetChrChipByIndex(0x102, 9)
    SetChrChipByIndex(0x10A, 11)
    SetChrChipByIndex(0x10E, 13)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x10A, 0)
    SetChrSubChip(0x10E, 0)
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)
    SetChrFlags(0x8, 0x800)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -3900, 5400, 25090, 90)
    SetChrChipByIndex(0xB, 2)
    SetChrSubChip(0xB, 0)
    OP_6D(270, 2000, 24030, 0)
    OP_67(0, 3150, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(32000, 0)
    OP_6E(337, 0)
    LoadEffect(0x0, "map\\mp055_00.eff")
    LoadEffect(0x1, "map\\mp093_00.eff")
    LoadEffect(0x2, "map\\mp093_01.eff")
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #51
        0x8,
        "#1224F#3POh, Aidios, the PAIN!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 17)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_22(0x218, 0x0, 0x64)
    OP_99(0x8, 0x0, 0x6, 0x5DC)
    OP_43(0x8, 0x1, 0x0, 0x6)

    ChrTalk(    #52
        0x8,
        (
            "#1227F#3PPlease, I beg you!\x01",
            "Spare my miserable life!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1007F#2PFor the love of...why do you have\x01",
            "to be such a coward NOW?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10A,
        (
            "#819F#2PHaha, it sorta feels like we're\x01",
            "bullying him at this point...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10E,
        (
            "#843F#2PHis choices led him to this end.\x02\x03",

            "#842FGilbert. In accordance with the laws\x01",
            "of the Bracer Guild, you are--\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #56
        (
            "\x07\x05That won't do.\x01",
            "Arresting him would be a problem.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_44(0x8, 0x1)
    SetChrSubChip(0x8, 7)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0xA, 190, 2000, 25290, 180)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    OP_1D(0x6F)
    Sleep(500)

    def lambda_1E6A():
        OP_6B(2100, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1E6A)

    def lambda_1E7A():
        OP_6D(870, 2000, 26560, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1E7A)

    def lambda_1E92():
        OP_67(0, 4830, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E92)

    def lambda_1EAA():
        OP_6E(391, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1EAA)
    PlayEffect(0x0, 0x1, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x101, 0x0, 0x0, 0x7)
    WaitChrThread(0x101, 0x0)
    OP_22(0x99, 0x0, 0x64)

    def lambda_1F75():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1F75)
    Sleep(1500)
    OP_82(0x1, 0x2)
    OP_43(0xA, 0x3, 0x0, 0x11)
    SetChrSubChip(0x8, 8)
    Sleep(200)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x102, 0x3)

    ChrTalk(    #57
        0x101,
        "#1005F#5PYou...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10A,
        (
            "#815F#5PThe one who showed up\x01",
            "at the mine!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        "#1042F#5PCampanella.\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 19)
    SetChrSubChip(0xA, 0)
    OP_99(0xA, 0x0, 0x3, 0x5DC)
    Sleep(500)

    ChrTalk(    #60
        0xA,
        "#853F#6PHeheh... Good day!\x02",
    )

    CloseMessageWindow()
    OP_99(0xA, 0x3, 0x0, 0x5DC)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    Sleep(500)

    ChrTalk(    #61
        0xA,
        (
            "#854F#6PI've been watching ever since\x01",
            "you entered the academy.\x02\x03",

            "#851FOh, what a show, what a show!\x01",
            "It was a delight to watch!\x02\x03",

            "I didn't think there would be a\x01",
            "last-second addition to the cast,\x01",
            "either. And such timing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xB,
        "#310F#6PScree?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "#1221F#6PSir Campanella...have you come\x01",
            "to save me?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    def lambda_21A7():
        OP_6D(920, 2000, 27360, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_21A7)
    Sleep(500)
    OP_63(0xA)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #64
        0xA,
        (
            "#850F#5PYou know, Gilbert.\x02\x03",

            "I don't seem to remember ordering\x01",
            "you to capture anyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        "#1224F#6P*gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "#853F#5PI mean, of course you have to take\x01",
            "advantage of opportunities as they come.\x02\x03",

            "You're on the ground, you have\x01",
            "to make 'the call,' as they say.\x01",
            "I won't stop you from doing that.\x02\x03",

            "#854FBut if you fail...there really wasn't\x01",
            "much of a point, was there?\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #67
        0x8,
        "#1224F#6PNo... No, please...\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrFlags(0x8, 0x20)
    OP_8F(0x8, 0x64, 0x7D0, 0x6C34, 0x3E8, 0x0)
    ClearChrFlags(0x8, 0x20)
    Sleep(300)
    Fade(250)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 18)
    SetChrSubChip(0xA, 0)
    OP_0D()
    OP_99(0xA, 0x1, 0x2, 0x5DC)
    OP_22(0xBC, 0x0, 0x64)
    Sleep(500)
    Fade(500)
    OP_6D(-90, 2500, 26730, 0)
    OP_67(0, 3870, -10000, 0)
    OP_6B(2170, 0)
    OP_6C(1000, 0)
    OP_6E(391, 0)
    SetChrPos(0x101, -1090, 0, 18620, 0)
    SetChrPos(0x102, 180, -50, 18470, 0)
    SetChrPos(0x10A, -1290, 0, 16900, 0)
    SetChrPos(0x10E, -40, 0, 16760, 0)
    SetChrPos(0x9, -220, 0, 15100, 0)
    SetChrPos(0x8, -500, 2000, 26910, 180)
    SetChrPos(0xA, 0, 2000, 24750, 180)
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 5)
    SetChrSubChip(0xA, 0)
    OP_0D()
    OP_22(0x87, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x8, 0, 0, 0, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x1)
    ClearChrFlags(0x8, 0x800)
    SetChrChipByIndex(0x8, 16)
    SetChrSubChip(0x8, 0)

    def lambda_24FC():

        label("loc_24FC")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_24FC")

    QueueWorkItem2(0x8, 3, lambda_24FC)
    OP_8F(0x8, 0xFFFFFE0C, 0x834, 0x68B0, 0x1F40, 0x0)
    Sleep(500)

    ChrTalk(    #68
        0x8,
        "#1227F#6PGYAAAAAAAAAH!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #69
        0x101,
        "#1020F#5PWhat the hell?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x102,
        (
            "#1035F#5PThe Flame Tongue attack illusion.\x02\x03",

            "#1042FJust like what Luciola uses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        (
            "#851F#5PHeehee!\x01",
            "Mind, I'm not nearly as good as she is.\x02\x03",

            "#854FI can still roast a bad steak, though.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x1)

    def lambda_2634():
        OP_6D(-90, 3500, 26730, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2634)
    OP_82(0x1, 0x0)
    OP_22(0x87, 0x0, 0x64)
    PlayEffect(0x2, 0x2, 0x8, 0, 0, 0, 0, 0, 0, 1100, 1200, 1100, 0xFF, 0, 0, 0, 0)

    def lambda_2689():

        label("loc_2689")

        OP_9E(0xFE, 0x32, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_2689")

    QueueWorkItem2(0x8, 3, lambda_2689)
    OP_8F(0x8, 0xFFFFFE0C, 0xC80, 0x68B0, 0x1F40, 0x0)
    Sleep(500)

    ChrTalk(    #72
        0x8,
        "#1227F#6PYEAAAAAAAAAAAAAAAAARGH!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #73
        0xA,
        (
            "#851F#5PI did enjoy watching Gilbert make\x01",
            "such a fool of himself.\x02\x03",

            "I suppose I can leave off the punishment\x01",
            "for that...this time.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x2, 0x2)
    OP_23(0x87)

    def lambda_2781():
        OP_6D(0, 2000, 26730, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2781)
    OP_44(0x8, 0x3)
    OP_8F(0x8, 0xFFFFFE0C, 0x7D0, 0x68B0, 0x1F40, 0x0)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)
    SetChrFlags(0x8, 0x1)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)

    ChrTalk(    #74
        0x8,
        "#5PAuuuuugh...\x02",
    )

    CloseMessageWindow()
    PlayEffect(0x0, 0x1, 0xA, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x10A, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #75
        0x101,
        "#1005F#5PWait a second!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10A,
        "#815F#5PYou running again?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xA,
        (
            "#851F#6PHahaha! Well, anyway!\x01",
            "Let me apologize for all this.\x02\x03",

            "You have my word that the Society of\x01",
            "Ouroboros will not lay another finger\x01",
            "on this academy.\x02\x03",

            "#854FWell, then, ladies and gentlemen.\x01",
            "Good day and...farewell!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x99, 0x0, 0x64)

    def lambda_294A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_294A)

    def lambda_295C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_295C)
    Sleep(1500)
    OP_82(0x1, 0x2)
    OP_43(0xA, 0x3, 0x0, 0x11)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x80)
    Sleep(1000)
    Fade(1000)
    OP_20(0x7D0)
    OP_6D(170, 2000, 25490, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(2330, 0)
    OP_6C(45000, 0)
    OP_6E(353, 0)
    SetChrPos(0x101, -730, 0, 18400, 0)
    SetChrPos(0x102, 790, 0, 18470, 0)
    SetChrPos(0x10A, -1130, 0, 16880, 0)
    SetChrPos(0x10E, 530, -50, 16790, 0)
    SetChrPos(0x9, -300, 0, 15300, 0)
    OP_0D()
    OP_43(0xB, 0x2, 0x0, 0xF)

    def lambda_2A30():
        OP_6D(1020, -50, 18700, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A30)

    def lambda_2A48():
        OP_67(0, 5500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A48)

    def lambda_2A60():
        OP_6B(2310, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2A60)
    Sleep(2500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10A, 65535)
    SetChrChipByIndex(0x10E, 65535)
    Sleep(500)

    ChrTalk(    #78
        0x101,
        "#1003F#4PAgain with the running...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10A,
        (
            "#1316F#2PAre we ever gonna\x01",
            "nail them down...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x10E,
        (
            "#844F#4PCampanella the Fool...\x01",
            "Quite the enigma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x102,
        "#1043F#4PThat's barely half of it.\x02",
    )

    CloseMessageWindow()

    def lambda_2B4C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B4C)
    Sleep(100)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #82
        0x102,
        (
            "#1040F#6PI do think we can take his\x01",
            "word on this, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x10E,
        "#845F#4POne can hope.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1007F#6PWell, while I am kinda sad he got away...\x02\x03",

            "#1025FI guess that pretty much\x01",
            "settles things here, huh?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2C33():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C33)
    Sleep(100)
    TurnDirection(0x10E, 0x101, 400)

    ChrTalk(    #85
        0x10A,
        "#816F#2PPretty much!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 0x2)

    ChrTalk(    #86
        0xB,
        "#311F#6PScreee. ♪\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #87
        (
            "\x07\x05And so the occupation of Jenis Royal Academy\x01",
            "came to an end.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #88
        (
            "\x07\x05By the time the Royal Army detachment arrived,\x01",
            "the jaegers at the academy had retreated...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #89
        (
            "\x07\x05And thanks to the dean and Jill's group,\x01",
            "the students had calmed down.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T2500   ._SN", 122, 0, 0)
    IdleLoop()
    Return()

    # Function_5_19C7 end

    def Function_6_2D9F(): pass

    label("Function_6_2D9F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DDB")
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_6_2D9F")

    label("loc_2DDB")

    Return()

    # Function_6_2D9F end

    def Function_7_2DDC(): pass

    label("Function_7_2DDC")


    def lambda_2DE2():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2DE2)
    Sleep(50)

    def lambda_2E02():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_2E02)
    Sleep(200)

    def lambda_2E22():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E22)
    Sleep(50)

    def lambda_2E42():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF060, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2E42)
    WaitChrThread(0x101, 0x1)
    Return()

    # Function_7_2DDC end

    def Function_8_2E5D(): pass

    label("Function_8_2E5D")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -470, 0, -1270, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2E84():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E84)
    OP_8E(0xFE, 0xFFFFFE52, 0x0, 0x19FA, 0x1388, 0x0)
    Return()

    # Function_8_2E5D end

    def Function_9_2EA5(): pass

    label("Function_9_2EA5")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 630, 0, -1270, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2ECC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2ECC)
    OP_8E(0xFE, 0x2BC, 0x0, 0x1996, 0x1388, 0x0)
    Return()

    # Function_9_2EA5 end

    def Function_10_2EED(): pass

    label("Function_10_2EED")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -470, 0, -1270, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2F14():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F14)
    OP_8E(0xFE, 0xFFFFFBF0, 0x0, 0x14C8, 0x1388, 0x0)
    Return()

    # Function_10_2EED end

    def Function_11_2F35(): pass

    label("Function_11_2F35")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 630, 0, -1270, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_2F5C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F5C)
    OP_8E(0xFE, 0x1D6, 0x0, 0x14B4, 0x1388, 0x0)
    Return()

    # Function_11_2F35 end

    def Function_12_2F7D(): pass

    label("Function_12_2F7D")

    OP_8E(0xFE, 0x226, 0x0, 0x5230, 0x1388, 0x0)
    OP_8E(0xFE, 0x88E, 0x0, 0x4C5E, 0x1388, 0x0)
    OP_8E(0xFE, 0x758, 0x0, 0x396C, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFFFBA, 0x0, 0x396C, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_12_2F7D end

    def Function_13_2FD5(): pass

    label("Function_13_2FD5")

    OP_8C(0xFE, 180, 0)

    def lambda_2FE2():
        OP_96(0xFE, 0xFFFFFFA6, 0x7D0, 0x65EA, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2FE2)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 0)
    Return()

    # Function_13_2FD5 end

    def Function_14_301E(): pass

    label("Function_14_301E")

    SetChrChipByIndex(0xB, 6)
    OP_97(0xB, 0xFFFFFAB0, 0x6A7C, 0x27100, 0x1770, 0x1)
    SetChrChipByIndex(0xB, 1)
    OP_8C(0xFE, 90, 300)
    OP_8F(0xFE, 0xFFFFF0C4, 0x13EC, 0x6202, 0x3E8, 0x0)
    Fade(250)
    OP_44(0xB, 0x1)
    SetChrPos(0xB, -3900, 5400, 25090, 90)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 2)
    OP_0D()
    Return()

    # Function_14_301E end

    def Function_15_307E(): pass

    label("Function_15_307E")

    OP_22(0x8C, 0x0, 0x64)
    SetChrChipByIndex(0xB, 1)

    def lambda_308E():

        label("loc_308E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_308E")

    QueueWorkItem2(0xB, 1, lambda_308E)
    OP_8F(0xFE, 0xFFFFF4AC, 0x1770, 0x6202, 0x3E8, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFFF830, 0x60E, 0x55E6, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 300)
    Sleep(100)
    Fade(250)
    OP_44(0xB, 0x1)
    SetChrPos(0xB, -2000, 1750, 21990, 135)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 2)
    OP_0D()
    Return()

    # Function_15_307E end

    def Function_16_30FC(): pass

    label("Function_16_30FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3111")
    OP_99(0xFE, 0x0, 0x7, 0xBB8)
    Jump("Function_16_30FC")

    label("loc_3111")

    Return()

    # Function_16_30FC end

    def Function_17_3112(): pass

    label("Function_17_3112")

    Sleep(300)
    OP_24(0x10A, 0x5A)
    Sleep(300)
    OP_24(0x10A, 0x50)
    Sleep(300)
    OP_24(0x10A, 0x46)
    Sleep(300)
    OP_24(0x10A, 0x3C)
    Sleep(300)
    OP_24(0x10A, 0x32)
    Sleep(300)
    OP_24(0x10A, 0x28)
    Sleep(300)
    OP_24(0x10A, 0x1E)
    Sleep(300)
    OP_23(0x10A)
    Return()

    # Function_17_3112 end

    def Function_18_315A(): pass

    label("Function_18_315A")

    NewScene("ED6_DT21/T2611   ._SN", 120, 0, 0)
    IdleLoop()
    Return()

    # Function_18_315A end

    SaveToFile()

Try(main)
